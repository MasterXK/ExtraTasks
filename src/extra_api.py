import os
import logging
import requests
from datetime import datetime
from dotenv import load_dotenv
from data import PATH_DATA

load_dotenv()

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(os.path.join(PATH_DATA, 'api_log.log'), 'w')
file_formatter = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
file_handler.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

logger.addHandler(console_handler)
logger.addHandler(file_handler)


def get_transaction_sum(transaction: dict) -> float | None:
    """
    Функция выводит транзакцию в рублях
    :param transaction: транзакция
    :return: сумма транзакции
    """
    target_currency = transaction["operationAmount"]["currency"]["code"]

    if target_currency == "RUB":
        logger.info('Транзакция в рублях, вывожу сумму...')
        return float(transaction["operationAmount"]["amount"])

    else:
        logger.info(f'Транзакция в валюте {target_currency}, запрашиваю курс к рублю...')
        key = os.getenv("API_EXC")

        try:
            response = requests.get(
                f"https://v6.exchangerate-api.com/v6/{key}/latest/{target_currency}"
            )
            data = response.json()
            logger.debug('Данные курса получены.')

        except requests.exceptions.RequestException as e:
            logger.debug(f'Не удалось получить данные: {e}', exc_info=True)
            return None

        logger.info('Курс валюты получен, вывожу сумму транзакции...')
        return round(
            data["conversion_rates"]["RUB"]
            * float(transaction["operationAmount"]["amount"]),
            2,
        )


def log_messages(level: str, message: str) -> None:
    time_now = datetime.now()
    today = time_now.strftime('%Y-%m-%d.log')
    file_path = os.path.join(PATH_DATA, 'logs', today)

    sh = logging.StreamHandler()
    fh = logging.FileHandler(file_path)
    logging.basicConfig(handlers=(fh, sh),
                        level=getattr(logging, level.upper()),
                        format='%(asctime)s - %(levelname)s - %(message)s')

    if level.upper() == 'DEBUG':
        logging.debug(message)

    elif level.upper() == 'INFO':
        logging.info(message)

    elif level.upper() == 'WARNING':
        logging.warning(message)

    elif level.upper() == 'ERROR':
        logging.error(message)

    else:
        logging.critical(message)


def download_photos(album_id: int, limit: int=100):
    logging.basicConfig(level=logging.INFO)
    logging.info('Starting app...')

    url = 'https://jsonplaceholder.typicode.com/photos'

    try:
        response = requests.get(url)
        data = response.json()

    except requests.exceptions.RequestException as e:
        logging.info(f'An error has occurred: {e}', exc_info=True)
        return e

    i = 0
    while True:
        if data[i]['albumId'] == album_id:

            logging.info(f'Downloading album {album_id} images...')
            for j in range(limit):
                if data[i + j]['albumId'] != album_id:
                    logging.info(f'Finished downloading images. Total images downloaded: {j}')
                    break

                pic = requests.get(data[j - 1]['url'])

                logging.info(f'Saving image {j + 1} to data/photos/{album_id}-{j + 1}.jpg')
                with open(os.path.join(PATH_DATA, 'photos', f'{album_id}-{j + 1}.jpg'), 'wb') as p:
                    p.write(pic.content)

            logging.info(f'Finished downloading images. Total images downloaded: {j + 1}')
            break

        i += 1


download_photos(2, 5)

import os

import requests
from dotenv import load_dotenv

load_dotenv()


def get_transaction_sum(transaction: dict) -> float:
    """
    Функция выводит транзакцию в рублях
    :param transaction: транзакция
    :return: сумма транзакции
    """
    target_currency = transaction["operationAmount"]["currency"]["code"]

    if target_currency == "RUB":
        return float(transaction["operationAmount"]["amount"])

    else:
        key = os.getenv("API_EXC")
        response = requests.get(
            f"https://v6.exchangerate-api.com/v6/{key}/latest/{target_currency}"
        )
        data = response.json()

        return float(
            data["conversion_rates"]["RUB"]
            * float(transaction["operationAmount"]["amount"])
        )


print(
    get_transaction_sum(
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "100",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        }
    )
)

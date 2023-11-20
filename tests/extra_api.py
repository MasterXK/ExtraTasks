from unittest.mock import patch

import pytest

from src.extra_api import get_transaction_sum


@pytest.fixture()
def transaction() -> dict:
    return {
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


@patch("requests.get")
@patch("os.getenv")
def test_get_transaction_sum(mock_env, mock_get, transaction):
    mock_get.return_value.json.return_value = {"conversion_rates": {"RUB": 90}}
    mock_env.return_value = "key"
    assert get_transaction_sum(transaction) == 9000.00
    mock_get.assert_called_once_with(
        f'https://v6.exchangerate-api.com/v6/key/latest/{transaction["operationAmount"]["currency"]["code"]}'
    )

import pytest

from src.processing import *


@pytest.fixture
def products():
    return [
        {"name": "", "price": 10, "category": "q", "quantity": 1},
        {"name": "", "price": 25, "category": "w", "quantity": 2},
        {"name": "", "price": 12, "category": "q", "quantity": 3},
        {"name": "", "price": 55, "category": "e", "quantity": 4},
        {"name": "", "price": 6, "category": "q", "quantity": 5},
    ]


@pytest.fixture
def orders():
    return [
        {
            "id": "1",
            "date": "2019-04-03T18:35:29.512364",
            "items": [
                {"name": "", "price": 1, "quantity": 2},
                {"name": "", "price": 3, "quantity": 3},
                {"name": "", "price": 4, "quantity": 5},
            ],
        },
        {
            "id": "2",
            "date": "2019-05-03T18:35:29.512364",
            "items": [{"name": "", "price": 2, "quantity": 3}],
        },
        {
            "id": "3",
            "date": "2019-05-06T18:35:29.512364",
            "items": [{"name": "", "price": 3, "quantity": 3}],
        },
        {
            "id": "4",
            "date": "2019-07-10T18:35:29.512364",
            "items": [{"name": "", "price": 3, "quantity": 2}],
        },
        {
            "id": "5",
            "date": "2019-07-12T18:35:29.512364",
            "items": [{"name": "", "price": 10, "quantity": 1}],
        },
    ]


def test_sort_by_price(products):
    assert sort_by_price(products) == [
        {"name": "", "price": 55, "category": "e", "quantity": 4},
        {"name": "", "price": 25, "category": "w", "quantity": 2},
        {"name": "", "price": 12, "category": "q", "quantity": 3},
        {"name": "", "price": 10, "category": "q", "quantity": 1},
        {"name": "", "price": 6, "category": "q", "quantity": 5},
    ]
    assert sort_by_price(products, category="q") == [
        {"name": "", "price": 12, "category": "q", "quantity": 3},
        {"name": "", "price": 10, "category": "q", "quantity": 1},
        {"name": "", "price": 6, "category": "q", "quantity": 5},
    ]


def test_get_months_statistic(orders):
    assert get_months_statistic(orders) == {
        "2019.04": {"average_order_value": 20.0, "order_count": 1},
        "2019.05": {"average_order_value": 7.5, "order_count": 2},
        "2019.07": {"average_order_value": 8.0, "order_count": 2},
    }

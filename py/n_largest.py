import heapq
import random
import pytest


#@pytest.fixture
def portfolio():
    portfolio = [
        {"name": "IBM", "shares": 100, "price": 91.1},
        {"name": "AAPL", "shares": 50, "price": 543.22},
        {"name": "FB", "shares": 200, "price": 21.09},
        {"name": "HPQ", "shares": 35, "price": 31.75},
        {"name": "YHOO", "shares": 45, "price": 16.35},
    ]
    return portfolio

print(heapq.nsmallest(3, portfolio(), key=lambda s: s["price"]))
print(heapq.nlargest(3, portfolio(), key=lambda s: s["price"]))

def test_nsmallest(portfolio):
    assert heapq.nsmallest(3, portfolio, key=lambda s: s["price"]) == 1
    assert heapq.nlargest(3, portfolio, key=lambda s: s["price"]) == 1

import pytest


def test_market_index(market_index):
    pass


def test_tick(market_index):
    assert market_index.current_tick == 0
    market_index.tick()
    assert market_index.current_tick == 1

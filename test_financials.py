import pytest

from financials import Money, CashRate


def test_money():
    # Invalid case - try and create with a non-int argument
    # We block this as it will cause problems down the line
    with pytest.raises(TypeError):
        invalid_money = Money("100")

    # Valid case - create valid money
    no_money = Money(0)
    some_money = Money(1000)


def test_money_comparators():
    no_money = Money(0)
    some_money = Money(1000)
    some_money_2 = Money(1000)

    # Test comparators
    assert some_money == some_money_2
    assert some_money > no_money
    assert no_money < some_money
    assert (no_money + some_money) == some_money_2
    assert (some_money_2 - some_money) == no_money


def test_money_is_negative():
    negative_money = Money(-1)
    no_money = Money(0)
    positive_money = Money(1)
    assert negative_money.is_negative()
    assert not no_money.is_negative()
    assert not positive_money.is_negative()


def test_cashrate():
    zero_rate = CashRate(0)
    one_percent = CashRate(100)
    assert one_percent > zero_rate

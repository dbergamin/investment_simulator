from financials import CashRate, Money
from datetime import date


class Account:
    # Source data for index values at a given
    # Balance should be expressed in cents
    # Rate should be expressed in basis points, annualised
    # Interest paid on the first of each month
    def __init__(self, initial_balance: Money,
                 annual_interest_rate: CashRate,
                 opening_date: date = None):
        self._balance = initial_balance
        self._annual_interest_rate = annual_interest_rate
        self._monthly_interest_rate = annual_interest_rate / 12
        self._current_tick = 0

        if opening_date is None:
            self._opening_date = date.today()
        else:
            self._opening_date = opening_date

    def deposit(self, amount: Money):
        if amount.is_negative:
            raise ValueError("Cannot deposit a negative amount of money")

        self._balance += amount

    def withdraw(self, amount: Money):
        if amount.is_negative:
            raise ValueError("Cannot withdraw a negative amount of money")

        self._balance -= amount

    def balance(self) -> Money:
        return self._balance

    # For now you get full interest for the month even if you opened a day earlier :)
    def tick(self):
        self._balance.amount * self._monthly_interest_rate
        self.current_tick += 1

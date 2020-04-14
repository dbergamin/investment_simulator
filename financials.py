class CashRate:
    # An cash rate expressed in basis points
    def __init__(self, rate: int):
        if not isinstance(rate, int):
            raise TypeError("Expected an integer representing cash rate in bps")

        self.rate = rate

    def __eq__(self, other: 'CashRate') -> bool:
        if not isinstance(other, CashRate):
            raise TypeError("Expecting to compare Cash Rate with other Cash Rate")

        return self.rate == other.rate

    def __gt__(self, other: 'CashRate') -> bool:
        if not isinstance(other, CashRate):
            raise TypeError("Expecting to compare Cash Rate with other Cash Rate")

        return self.rate > other.rate


class Money:
    # An amount of money in cents
    def __init__(self, amount: int):
        if not isinstance(amount, int):
            raise TypeError("Expected an integer representing money value in cents")
        self.amount = amount

    def is_negative(self) -> bool:
        if self.amount < 0:
            return True

    def __eq__(self, other: 'Money') -> bool:
        if not isinstance(other, Money):
            raise TypeError("Expecting to compare Money with Money")

        return self.amount == other.amount

    def __gt__(self, other: 'Money') -> bool:
        if not isinstance(other, Money):
            raise TypeError("Expecting to compare Money with Money")

        return self.amount > other.amount

    def __add__(self, other: 'Money') -> 'Money':
        if not isinstance(other, Money):
            raise TypeError("Expecting to add Money with Money")

        return Money(self.amount + other.amount)

    def __sub__(self, other: 'Money') -> 'Money':
        if not isinstance(other, Money):
            raise TypeError("Expecting to add Money with Money")

        return Money(self.amount - other.amount)
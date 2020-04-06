class CashRate:
    # An amount of money in cents
    def __init__(self, rate: int):
        self.rate = rate

    def __gt__(self, other: 'CashRate') -> bool:
        if not isinstance(other, Money):
            raise TypeError("Expecting to compare Cash Rate with other Cash Rate")

        return self.rate > other.rate


class Money:
    # An amount of money in cents
    def __init__(self, amount: int):
        self.amount = amount

    def is_negative(self) -> bool:
        if self.amount < 0:
            return True

    def __gt__(self, other: 'Money') -> bool:
        if not isinstance(other, Money):
            raise TypeError("Expecting to compare Money with Money")

        return self.amount > other.amount

    def __add__(self, other: 'Money') -> 'Money':
        if not isinstance(other, Money):
            raise TypeError("Expecting to add Money with Money")

        return self.amount + other.amount

    def __sub__(self, other: 'Money') -> 'Money':
        if not isinstance(other, Money):
            raise TypeError("Expecting to add Money with Money")

        return self.amount - other.amount
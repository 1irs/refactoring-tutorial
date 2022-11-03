from abc import abstractmethod


class PricingStrategy:
    @abstractmethod
    def discount(self, price: float, qty: int) -> float:
        ...


class NoDiscount(PricingStrategy):
    def discount(self, price: float, qty: int) -> float:
        return 0.0


class FiveOrMoreMinus5Percent(PricingStrategy):
    def discount(self, price: float, qty: int) -> float:
        return price * qty * 0.05 if qty >= 5 else price * qty


class EachThirdFree(PricingStrategy):
    def discount(self, price: float, qty: int) -> float:
        return (qty // 3) * price


class CouponMinusTen(PricingStrategy):
    def discount(self, price: float, qty: int) -> float:
        return 10.0 if price * qty >= 10.0 else price * qty

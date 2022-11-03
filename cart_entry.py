# First Institute of Reliable Software
# Refactoring of Shopping Cart Business Logic
# https://1irs.net
# Special for PyCon Poland 2022
# Author: Dr. Vladimir Obrizan
# Presenter: Ihor Harahatyi


from enum import Enum

from pricing_strategy import NoDiscount, CouponMinusTen, FiveOrMoreMinus5Percent, EachThirdFree
from product import Product


class DiscountType(Enum):
    NO_DISCOUNT = 1
    FIVE_OR_MORE_MINUS_5_PERCENT = 2
    EACH_THIRD_FREE = 3
    COUPON_MINUS_TEN = 4


class CartEntry:
    def __init__(
        self,
        product: Product,
        qty: int,
        discount_type: DiscountType = DiscountType.NO_DISCOUNT,
    ):
        assert qty > 0
        self.product = product
        self.qty = qty
        self.set_discount_type(discount_type)

    def discount(self) -> float:
        return self.pricing_strategy.discount(self.product.price, self.qty)

    def price(self):
        return self.product.price * self.qty

    def set_discount_type(self, discount_type: DiscountType) -> None:
        match discount_type:
            case DiscountType.NO_DISCOUNT:
                self.pricing_strategy = NoDiscount()
            case DiscountType.COUPON_MINUS_TEN:
                self.pricing_strategy = CouponMinusTen()
            case DiscountType.FIVE_OR_MORE_MINUS_5_PERCENT:
                self.pricing_strategy = FiveOrMoreMinus5Percent()
            case DiscountType.EACH_THIRD_FREE:
                self.pricing_strategy = EachThirdFree()

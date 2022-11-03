# First Institute of Reliable Software
# Refactoring of Shopping Cart Business Logic
# https://1irs.net
# Special for PyCon Poland 2022
# Author: Dr. Vladimir Obrizan
# Presenter: Ihor Harahatyi


from enum import Enum

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
        self.discount_type = discount_type

    def discount(self) -> float:
        entry_discount: float = 0.0
        match self.discount_type:
            case DiscountType.NO_DISCOUNT:
                # Do nothing.
                pass
            case DiscountType.COUPON_MINUS_TEN:
                # Make sure we don't give discount higher than the cost.
                # E.g. cost is 9, and the coupon is 10.
                entry_discount = (
                    10.0
                    if self.product.price * self.qty >= 10.0
                    else self.product.price * self.qty
                )
            case DiscountType.FIVE_OR_MORE_MINUS_5_PERCENT:
                if self.qty >= 5:
                    entry_discount = self.product.price * self.qty * 0.05
            case DiscountType.EACH_THIRD_FREE:
                entry_discount = (self.qty // 3) * self.product.price
        return entry_discount

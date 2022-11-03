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

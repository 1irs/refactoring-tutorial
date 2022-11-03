from cart_entry import CartEntry, DiscountType
from product import ProductCategory


class ShoppingCart:
    def __init__(self):
        self.entries: list[CartEntry] = []

    def add_entry(self, entry: CartEntry) -> None:
        self.entries.append(entry)

    def description(self) -> str:
        """Gets a text representation of a cart."""
        total_cost: float = 0.0
        total_tax: float = 0.0
        total_discount: float = 0.0

        # Print header.
        result: str = "Cart contents:\n"

        for entry in self.entries:
            total_cost += entry.product.price * entry.qty
            entry_discount: float = 0.0
            entry_tax: float = 0.0

            # Calculate discount.
            match entry.discount_type:
                case DiscountType.NO_DISCOUNT:
                    # Do nothing.
                    pass
                case DiscountType.COUPON_MINUS_TEN:
                    # Make sure we don't give discount higher than the cost.
                    # E.g. cost is 9, and the coupon is 10.
                    entry_discount = (
                        10.0
                        if entry.product.price * entry.qty >= 10.0
                        else entry.product.price * entry.qty
                    )
                case DiscountType.FIVE_OR_MORE_MINUS_5_PERCENT:
                    if entry.qty >= 5:
                        entry_discount = entry.product.price * entry.qty * 0.05
                case DiscountType.EACH_THIRD_FREE:
                    entry_discount = (entry.qty // 3) * entry.product.price

            total_discount += entry_discount

            # Calculate tax.
            match entry.product.category:
                case ProductCategory.ALCOHOL | ProductCategory.CLOTHES | ProductCategory.FOOD:
                    entry_tax = (entry.product.price * entry.qty - entry_discount) * 0.20
                case ProductCategory.PHARMA:
                    entry_tax = (entry.product.price * entry.qty - entry_discount) * 0.08
                case ProductCategory.FIRST_NEED:
                    entry_tax = (entry.product.price * entry.qty - entry_discount) * 0.0

            total_tax += entry_tax

            # Print each cart entry line.
            result += f"* {entry.product.name} X {entry.qty} = {round(entry.product.price * entry.qty, 2)} "
            result += f"(discount {round(entry_discount, 2)}, tax {round(entry_tax, 2)})\n"

        # Print footer.
        result += f"Total cost: {round(total_cost, 2)}\n"
        result += f"Discount: {round(total_discount, 2)}\n"
        result += f"Final cost: {round(total_cost-total_discount, 2)}\n"
        result += f"Taxes: {round(total_tax, 2)}\n"

        return result

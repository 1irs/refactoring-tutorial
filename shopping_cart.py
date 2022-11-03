# First Institute of Reliable Software
# Refactoring of Shopping Cart Business Logic
# https://1irs.net
# Special for PyCon Poland 2022
# Author: Dr. Vladimir Obrizan
# Presenter: Ihor Harahatyi


from cart_entry import CartEntry, DiscountType


class ShoppingCart:
    def __init__(self):
        self.entries: list[CartEntry] = []

    def add_entry(self, entry: CartEntry) -> None:
        self.entries.append(entry)

    def description(self) -> str:
        """Gets a text representation of a cart."""
        total_cost: float = 0.0
        total_discount: float = 0.0

        # Print header.
        result: str = "Cart contents:\n"

        for entry in self.entries:
            total_cost += entry.product.price * entry.qty

            # Calculate discount_for_entry.
            entry_discount = self.discount_for_entry(entry)

            total_discount += entry_discount

            # Print each cart entry line.
            result += f"* {entry.product.name} X {entry.qty} = {round(entry.product.price * entry.qty, 2)} "
            result += f"(discount {round(entry_discount, 2)})\n"

        # Print footer.
        result += f"Total cost: {round(total_cost, 2)}\n"
        result += f"Discount: {round(total_discount, 2)}\n"
        result += f"Final cost: {round(total_cost-total_discount, 2)}\n"

        return result

    def discount_for_entry(self, entry: CartEntry) -> float:
        entry_discount: float = 0.0
        match entry.discount_type:
            case DiscountType.NO_DISCOUNT:
                # Do nothing.
                pass
            case DiscountType.COUPON_MINUS_TEN:
                # Make sure we don't give discount_for_entry higher than the cost.
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
        return entry_discount

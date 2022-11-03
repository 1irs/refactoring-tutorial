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

            # Calculate discount.
            entry_discount = entry.discount()

            total_discount += entry_discount

            # Print each cart entry line.
            result += f"* {entry.product.name} X {entry.qty} = {round(entry.product.price * entry.qty, 2)} "
            result += f"(discount {round(entry_discount, 2)})\n"

        # Print footer.
        result += f"Total cost: {round(total_cost, 2)}\n"
        result += f"Discount: {round(total_discount, 2)}\n"
        result += f"Final cost: {round(total_cost-total_discount, 2)}\n"

        return result

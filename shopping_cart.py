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
        # Print header.
        result: str = "Cart contents:\n"

        for entry in self.entries:
            # Print each cart entry line.
            result += f"* {entry.product.name} X {entry.qty} = {round(entry.price(), 2)} "
            result += f"(discount {round(entry.discount(), 2)})\n"

        # Print footer.
        result += f"Total cost: {round(self.get_total_cost(), 2)}\n"
        result += f"Discount: {round(self.get_total_discount(), 2)}\n"
        result += f"Final cost: {round(self.get_total_cost()-self.get_total_discount(), 2)}\n"

        return result

    def get_total_cost(self) -> float:
        total_cost: float = 0.0
        for entry in self.entries:
            total_cost += entry.price()
        return total_cost

    def get_total_discount(self) -> float:
        total_discount: float = 0.0
        for entry in self.entries:
            total_discount += entry.discount()
        return total_discount

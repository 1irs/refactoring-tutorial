# First Institute of Reliable Software
# Refactoring of Shopping Cart Business Logic
# https://1irs.net
# Special for PyCon Poland 2022
# Author: Dr. Vladimir Obrizan
# Presenter: Ihor Harahatyi


from cart_entry import CartEntry
from description import TextDescription


class ShoppingCart:
    def __init__(self):
        self.entries: list[CartEntry] = []

    def add_entry(self, entry: CartEntry) -> None:
        self.entries.append(entry)

    def description(self) -> str:
        """Gets a text representation of a cart."""
        # Print header.
        return TextDescription(self).get()

    def html_description(self) -> str:
        """Gets an HTML representation of a cart."""
        # Print header.
        result: str = "<h1>Cart contents:</h1>\n"
        result += "<ul>\n"

        for entry in self.entries:
            # Print each cart entry line.
            result += f"<li>{entry.product.name} X {entry.qty} = <b>{round(entry.price(), 2)}</b> "
            result += f"(discount {round(entry.discount(), 2)})</li>\n"

        # Print footer.
        result += "</ul>\n"
        result += f"<p>Total cost: <b>{round(self.get_total_cost(), 2)}</b></p>\n"
        result += f"<p>Discount: <b>{round(self.get_total_discount(), 2)}</b></p>\n"
        result += f"<p>Final cost: <b>{round(self.get_total_cost()-self.get_total_discount(), 2)}</b></p>\n"

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

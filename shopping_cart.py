# First Institute of Reliable Software
# Refactoring of Shopping Cart Business Logic
# https://1irs.net
# Special for PyCon Poland 2022
# Author: Dr. Vladimir Obrizan
# Presenter: Ihor Harahatyi


from cart_entry import CartEntry
from description import TextDescription, HtmlDescription


class ShoppingCart:
    def __init__(self):
        self.entries: list[CartEntry] = []

    def add_entry(self, entry: CartEntry) -> None:
        self.entries.append(entry)

    def description(self) -> str:
        return TextDescription(self).get()

    def html_description(self) -> str:
        return HtmlDescription(self).get()

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

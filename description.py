from abc import abstractmethod

from cart_entry import CartEntry
from shopping_cart import ShoppingCart


class Description:

    def __init__(self, cart: ShoppingCart):
        self.cart = cart

    def get(self) -> str:
        result = self.get_header()
        for entry in self.cart.entries:
            result += self.get_entry_string(entry)
        result += self.get_footer()
        return result

    @abstractmethod
    def get_header(self) -> str:
        ...

    @abstractmethod
    def get_entry_string(self, entry: CartEntry) -> str:
        ...

    @abstractmethod
    def get_footer(self) -> str:
        ...


class TextDescription(Description):

    @abstractmethod
    def get_header(self) -> str:
        return "Cart contents:\n"

    @abstractmethod
    def get_entry_string(self, entry: CartEntry) -> str:
        result = f"* {entry.product.name} X {entry.qty} = {round(entry.price(), 2)} "
        result += f"(discount {round(entry.discount(), 2)})\n"
        return result

    @abstractmethod
    def get_footer(self) -> str:
        result = f"Total cost: {round(self.cart.get_total_cost(), 2)}\n"
        result += f"Discount: {round(self.cart.get_total_discount(), 2)}\n"
        result += f"Final cost: {round(self.cart.get_total_cost() - self.cart.get_total_discount(), 2)}\n"
        return result

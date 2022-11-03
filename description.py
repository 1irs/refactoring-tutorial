from abc import abstractmethod

from cart_entry import CartEntry

# do not import ShoppingCart due to cyclic import.


class Description:
    def __init__(self, cart):
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


class HtmlDescription(Description):
    @abstractmethod
    def get_header(self) -> str:
        return "<h1>Cart contents:</h1>\n<ul>\n"

    @abstractmethod
    def get_entry_string(self, entry: CartEntry) -> str:
        result = f"<li>{entry.product.name} X {entry.qty} = <b>{round(entry.price(), 2)}</b> "
        result += f"(discount {round(entry.discount(), 2)})</li>\n"
        return result

    @abstractmethod
    def get_footer(self) -> str:
        result = "</ul>\n"
        result += f"<p>Total cost: <b>{round(self.cart.get_total_cost(), 2)}</b></p>\n"
        result += f"<p>Discount: <b>{round(self.cart.get_total_discount(), 2)}</b></p>\n"
        result += f"<p>Final cost: <b>{round(self.cart.get_total_cost()-self.cart.get_total_discount(), 2)}</b></p>\n"
        return result

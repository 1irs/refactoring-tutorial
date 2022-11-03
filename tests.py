from cart_entry import CartEntry, DiscountType
from product import Product, ProductCategory
from shopping_cart import ShoppingCart


def test_empty() -> None:
    cart = ShoppingCart()
    assert cart.description() == (
        "Cart contents:\n"
        "Total cost: 0.0\n"
        "Discount: 0.0\n"
        "Final cost: 0.0\n"
        "Taxes: 0.0\n"
    )


def test_single_product() -> None:
    cart = ShoppingCart()
    cart.add_entry(CartEntry(Product("T-shirt", 20.0, ProductCategory.CLOTHES), 2))
    assert cart.description() == (
        "Cart contents:\n"
        "* T-shirt X 2 = 40.0 (discount 0.0, tax 8.0)\n"
        "Total cost: 40.0\n"
        "Discount: 0.0\n"
        "Final cost: 40.0\n"
        "Taxes: 8.0\n"
    )


def test_two_products() -> None:
    cart = ShoppingCart()
    cart.add_entry(CartEntry(Product("T-shirt", 20.0, ProductCategory.CLOTHES), 2))
    cart.add_entry(CartEntry(Product("Coca-cola", 15.0, ProductCategory.FOOD), 1))
    assert cart.description() == (
        "Cart contents:\n"
        "* T-shirt X 2 = 40.0 (discount 0.0, tax 8.0)\n"
        "* Coca-cola X 1 = 15.0 (discount 0.0, tax 3.0)\n"
        "Total cost: 55.0\n"
        "Discount: 0.0\n"
        "Final cost: 55.0\n"
        "Taxes: 11.0\n"
    )


def test_five_or_more_discount() -> None:
    cart = ShoppingCart()
    cart.add_entry(
        CartEntry(
            Product("T-shirt", 20.0, ProductCategory.CLOTHES),
            5,
            DiscountType.FIVE_OR_MORE_MINUS_5_PERCENT,
        )
    )
    assert cart.description() == (
        "Cart contents:\n"
        "* T-shirt X 5 = 100.0 (discount 5.0, tax 19.0)\n"
        "Total cost: 100.0\n"
        "Discount: 5.0\n"
        "Final cost: 95.0\n"
        "Taxes: 19.0\n"
    )


def test_each_third_free_discount() -> None:
    cart = ShoppingCart()
    cart.add_entry(
        CartEntry(
            Product("T-shirt", 20.0, ProductCategory.CLOTHES),
            7,
            DiscountType.EACH_THIRD_FREE,
        )
    )
    assert cart.description() == (
        "Cart contents:\n"
        "* T-shirt X 7 = 140.0 (discount 40.0, tax 20.0)\n"
        "Total cost: 140.0\n"
        "Discount: 40.0\n"
        "Final cost: 100.0\n"
        "Taxes: 20.0\n"
    )


def test_minus_10_coupon() -> None:
    cart = ShoppingCart()
    cart.add_entry(
        CartEntry(
            Product("T-shirt", 20.0, ProductCategory.CLOTHES),
            7,
            DiscountType.COUPON_MINUS_TEN,
        )
    )
    assert cart.description() == (
        "Cart contents:\n"
        "* T-shirt X 7 = 140.0 (discount 10.0, tax 26.0)\n"
        "Total cost: 140.0\n"
        "Discount: 10.0\n"
        "Final cost: 130.0\n"
        "Taxes: 26.0\n"
    )


def test_minus_10_coupon_less_than_10() -> None:
    cart = ShoppingCart()
    cart.add_entry(
        CartEntry(
            Product("T-shirt", 9.0, ProductCategory.CLOTHES),
            1,
            DiscountType.COUPON_MINUS_TEN,
        )
    )
    assert cart.description() == (
        "Cart contents:\n"
        "* T-shirt X 1 = 9.0 (discount 9.0, tax 0.0)\n"
        "Total cost: 9.0\n"
        "Discount: 9.0\n"
        "Final cost: 0.0\n"
        "Taxes: 0.0\n"
    )

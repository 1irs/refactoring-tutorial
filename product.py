from enum import Enum


class ProductCategory(Enum):
    FOOD = 1
    BOOK = 2
    ALCOHOL = 3
    PHARMA = 4
    CLOTHES = 5
    FIRST_NEED = 6


class Product:
    def __init__(self, name: str, price: float, category: ProductCategory):
        self.name = name
        self.price = price
        self.category = category

# First Institute of Reliable Software
# Refactoring of Shopping Cart Business Logic
# https://1irs.net
# Special for PyCon Poland 2022
# Author: Dr. Vladimir Obrizan
# Presenter: Ihor Harahatyi


class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

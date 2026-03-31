from abc import ABC, abstractmethod

from project.products.base_products import BaseProduct


class BaseStore(ABC):
    def __init__(self, name:str, location:str, capacity:int):
        self.name = name
        self.location = location
        self.capacity = capacity
        self.products:list[BaseProduct] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Store name cannot be empty!")
        self.__name = value

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, value):
        if len(value) != 3 or " " in value:
            raise ValueError("Store location must be 3 chars long!")
        self.__location = value


    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError("Store capacity must be a positive number or 0!")
        self.__capacity = value


    def get_estimated_profit(self):
        est_profit = 0.10
        total_price = sum(p.price for p in self.products)
        profit = total_price * est_profit
        return f"Estimated future profit for {len(self.products)} products is {profit:.2f}"


    @property
    @abstractmethod
    def store_type(self)-> str:
        pass


    def store_stats(self):
        products_summary = {}
        for product in self.products:
            if product.model not in products_summary:
                products_summary[product.model] = {"count": 0, "total_price": 0.0}
            products_summary[product.model]["count"] += 1
            products_summary[product.model]["total_price"] += product.price


        stats = [
            f"Store: {self.name}, location: {self.location}, available capacity: {self.capacity}",
            self.get_estimated_profit(),
            self._product_section_text,
        ]

        for model in sorted(products_summary.keys()):
            count = products_summary[model]["count"]
            avg_price = products_summary[model]["total_price"] / count
            stats.append(f"{model}: {count}pcs, average price: {avg_price:.2f}")

        return "\n".join(stats).strip()

    @property
    @abstractmethod
    def _product_section_text(self):
        pass


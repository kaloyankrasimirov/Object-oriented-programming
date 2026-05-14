from project.clients.base_client import BaseClient
from project.clients.business_client import BusinessClient
from project.clients.regular_client import RegularClient
from project.plants.base_plant import BasePlant
from project.plants.flower import Flower
from project.plants.leaf_plant import LeafPlant
from collections import Counter


class FlowerShopManager:
    VALID_PLANTS = (Flower.__name__, LeafPlant.__name__)
    VALID_CLIENTS = (RegularClient.__name__, BusinessClient.__name__)
    def __init__(self):
        self.income = 0
        self.plants:list[BasePlant] = []
        self.clients:list[BaseClient] = []

    def add_plant(self, plant_type: str, plant_name: str, plant_price: float, plant_water_needed: int, plant_extra_data: str):
        if plant_type not in FlowerShopManager.VALID_PLANTS:
            raise ValueError("Unknown plant type!")

        if plant_type == LeafPlant.__name__:
            new_plant = LeafPlant(plant_name, plant_price, plant_water_needed, plant_extra_data)
        elif plant_type == Flower.__name__:
            new_plant = Flower(plant_name, plant_price, plant_water_needed, plant_extra_data)
        self.plants.append(new_plant)
        return f"{plant_name} is added to the shop as {plant_type}."

    def add_client(self, client_type: str, client_name: str, client_phone_number: str):
        if client_type not in FlowerShopManager.VALID_CLIENTS:
            raise ValueError("Unknown client type!")
        elif any(client.phone_number == client_phone_number for client in self.clients):
            raise ValueError("This phone number has been used!")

        if client_type == RegularClient.__name__:
            new_client = RegularClient(client_name, client_phone_number)
        elif client_type == BusinessClient.__name__:
            new_client = BusinessClient(client_name, client_phone_number)
        self.clients.append(new_client)
        return f"{client_name} is successfully added as a {client_type}."

    def sell_plants(self, client_phone_number: str, plant_name: str, plant_quantity: int):
        client = next((c for c in self.clients if c.phone_number == client_phone_number), None)
        if not client:
            raise ValueError("Client not found!")
        matching_plants = [p for p in self.plants if p.name == plant_name]
        if not matching_plants:
            raise ValueError("Plants not found!")
        if len(matching_plants) < plant_quantity:
            raise ValueError("Not enough plant quantity.")

        for plant in range(plant_quantity):
            plant_to_remove = matching_plants.pop(0)
            self.plants.remove(plant_to_remove)
        client.update_total_orders()
        order_amount = (plant_to_remove.price * plant_quantity) * (1 - client.discount / 100)
        self.income += order_amount
        client.update_discount()
        return f"{plant_quantity}pcs. of {plant_name} plant sold for {order_amount:.2f}"

    def remove_plant(self, plant_name:str):
        plant_to_remove = next((p for p in self.plants if p.name == plant_name), None)
        if not plant_to_remove:
            return "No such plant name."
        self.plants.remove(plant_to_remove)
        return f"Removed {plant_to_remove.plant_details()}"

    def remove_clients(self):
        clients_count = len(self.clients)
        clients_to_keep = []
        for client in self.clients:
            if client.total_orders > 0:
                clients_to_keep.append(client)
        self.clients = clients_to_keep
        return f"{clients_count - len(clients_to_keep)} client/s removed."

    def shop_report(self):

        plant_counts = Counter(p.name for p in self.plants)
        sorted_plants = sorted(plant_counts.items(), key=lambda x: (-x[1], x[0]))
        sorted_clients = sorted(self.clients, key=lambda c: (-c.total_orders, c.phone_number))
        total_orders_count = sum(c.total_orders for c in self.clients)
        report_lines = [
            "~Flower Shop Report~",
            f"Income: {self.income:.2f}",
            f"Count of orders: {total_orders_count}",
            f"~~Unsold plants: {len(self.plants)}~~"
        ]

        for name, count in sorted_plants:
            report_lines.append(f"{name}: {count}")

        report_lines.append(f"~~Clients number: {len(self.clients)}~~")
        for client in sorted_clients:
            report_lines.append(client.client_details())

        return "\n".join(report_lines)















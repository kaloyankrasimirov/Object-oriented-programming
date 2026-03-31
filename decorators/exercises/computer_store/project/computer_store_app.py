from project.computer_types.computer import Computer
from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:
    def __init__(self):
        self.warehouse:list[Computer] = []
        self.profits:int = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        valid_computer_types = ["Desktop Computer", "Laptop"]

        if type_computer not in valid_computer_types:
            raise ValueError(f"{type_computer} is not a valid type computer!")
        if type_computer == "Desktop Computer":
            computer = DesktopComputer(manufacturer, model)
        elif type_computer == "Laptop":
            computer = Laptop(manufacturer, model)

        result = computer.configure_computer(processor, ram)
        self.warehouse.append(computer)
        return result


    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        computer_to_sell = next((c for c in self.warehouse if c.processor == wanted_processor and c.ram >= wanted_ram
                               and c.price <= client_budget), None)

        if not computer_to_sell:
            raise Exception("Sorry, we don't have a computer for you.")
        self.profits += client_budget - computer_to_sell.price
        self.warehouse.remove(computer_to_sell)
        return f"{computer_to_sell} sold for {client_budget}$."
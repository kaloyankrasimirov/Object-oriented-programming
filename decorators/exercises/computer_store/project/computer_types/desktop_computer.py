from project.computer_types.computer import Computer

class DesktopComputer(Computer):
    def __init__(self, manufacturer: str, model: str):
        super().__init__(manufacturer, model)

    def configure_computer(self, processor:str, ram:int):
        cpu_list = {
            "AMD Ryzen 7 5700G": 500,
            "Intel Core i5-12600K": 600,
            "Apple M1 Max": 1800
        }

        ram_list = {
            2: 100,
            4: 200,
            8: 300,
            16: 400,
            32: 500,
            64: 600,
            128: 700
        }

        if processor not in cpu_list:
            raise ValueError(f"{processor} is not compatible with desktop computer {self.manufacturer} {self.model}!")

        if ram not in ram_list:
            raise ValueError(f"{ram}GB RAM is not compatible with desktop computer {self.manufacturer} {self.model}!")

        self.processor = processor
        self.ram = ram

        self.price = cpu_list[processor] + ram_list[ram]

        return f"Created {self.manufacturer} {self.model} with {processor} and {ram}GB RAM for {self.price}$."


class Smartphone:

    def __init__(self, memory:int):
        self.memory = memory
        self.apps = []
        self.is_on:bool = False


    def power(self):
        if not self.is_on:
            self.is_on = True
        return self.is_on

    def install(self, app:str, app_memory:int):
        if not self.is_on:
            return f"Turn on your phone to install {app}"

        if app_memory > self.memory and self.is_on:
            return f"Not enough memory to install {app}"
        self.apps.append(app)
        self.memory -= app_memory
        return f"Installing {app}"

    def status(self):
        return f"Total apps: {len(self.apps)}. Memory left: {self.memory}"

smartphone = Smartphone(100)
print(smartphone.install("Facebook", 60))
smartphone.power()
print(smartphone.install("Facebook", 60))
print(smartphone.install("Messenger", 20))
print(smartphone.install("Instagram", 40))
print(smartphone.status())

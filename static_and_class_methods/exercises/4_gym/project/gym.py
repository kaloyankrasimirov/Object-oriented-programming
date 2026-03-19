
from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers:list[Customer] = []
        self.trainers:list[Trainer] = []
        self.equipment:list[Equipment] = []
        self.plans:list[ExercisePlan] = []
        self.subscriptions:list[Subscription] = []


    def add_customer(self, customer: Customer)->None:
        self.__add_obj(customer, self.customers)

    def add_trainer(self, trainer: Trainer)->None:
        self.__add_obj(trainer, self.trainers)

    def add_equipment(self, equipment: Equipment)->None:
        self.__add_obj(equipment, self.equipment)

    def add_plan(self, plan: ExercisePlan)->None:
        self.__add_obj(plan, self.plans)

    def add_subscription(self, subscription: Subscription)->None:
        self.__add_obj(subscription, self.subscriptions)

    def subscription_info(self, subscription_id:int)->str|None:
        subscription = next(s for s in self.subscriptions if s.id == subscription_id)
        customer = next(c for c in self.customers if c.id == subscription.customer_id)
        trainer = next(t for t in self.trainers if t.id == subscription.trainer_id)
        plan = next(p for p in self.plans if p.id == subscription.exercise_id)
        equipment = next(e for e in self.equipment if e.id == plan.equipment_id)
        if subscription:
            return (f"{subscription}\n"
                    f"{customer}\n"
                    f"{trainer}\n"
                    f"{equipment}\n"
                    f"{plan}")

    @staticmethod
    def __add_obj(obj, col):
        if obj not in col:
            col.append(obj)
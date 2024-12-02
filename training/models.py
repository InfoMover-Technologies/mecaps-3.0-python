from abc import ABC, abstractmethod
from typing import TypeVar, Type

# Create a type variable for Customer
T = TypeVar('T', bound='Customer')

class Customer(ABC):
    def __init__(self):
        self._id: int = 0
        self._name: str = ""
        self._customer_type: str = ""  # E [ExportCustomer] | L [LocalCustomer]

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, value: int):
        self._id = value

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def customer_type(self) -> str:
        return self._customer_type

    @customer_type.setter
    def customer_type(self, value: str):
        self._customer_type = value

    def print_customer_details(self):
        print(f"Id: {self._id} -- name: {self._name} -- {self.__class__.__name__}")

    @abstractmethod
    def generate_credit_balance(self):
        pass

    def __lt__(self, other: 'Customer') -> bool:
        return self._id < other._id


class ExportCustomer(Customer):
    def __init__(self):
        super().__init__()
        self._customer_type = "E"

    def generate_credit_balance(self):
        print(f"Generating creditBalance for Export Customer in: {self.__class__.__name__}")


class LocalCustomer(Customer):
    def __init__(self):
        super().__init__()
        self._customer_type = "L"

    def generate_credit_balance(self):
        print(f"Generating creditBalance for Local Customer in: {self.__class__.__name__}")


class CustomerFactory:
    @staticmethod
    def new_customer(customer_type: str) -> Customer:
        if customer_type == "E":
            return ExportCustomer()
        elif customer_type == "L":
            return LocalCustomer()
        else:
            raise ValueError(f"Invalid customer type: {customer_type}")
import shelve
from abc import ABC, abstractmethod

from store.domains import Client, Manager, Admin, Product


class ClientsRepository(ABC):
    """
    Абстрактный репозиторий для клиентов.
    От него нужно наследоваться в случае, когда нужно сделать другое хранилище, старое переписывать не нужно.
    """

    @abstractmethod
    def get_clients(self, username: str | None = None, password: str | None = None
                    ) -> list[Client]:
        pass


class MemoryClientsRepository(ClientsRepository):
    """
    Реализация клиентского хранилища в оперативной памяти.
    Клиенты инициализируются во время инициализации репозитория
    """

    def __init__(self):
        self.clients = [
            Manager(
                id="29ae7ebf-4445-42f2-9548-a3a54f095220",
                username="manager",
                password="best_manager$$$",
            ),
            Admin(
                id="29ae7ebf-4445-42f2-9548-a3a54f095220",
                username="admin",
                password="Admin_krutoi_007",
            ),
        ]

    def get_clients(self, username: str | None = None, password: str | None = None
                    ) -> tuple[list[Manager | Admin], list[Manager | Admin]]:
        """
        :param username: фильтр по логину
        :param password: фильтр по паролю
        :return: отфильтрованные пользователи
        """
        managers, admins = [], []  # отфильтрованные клиенты

        for client in self.clients:  # оставляем клиентов, которые прошли фильтры
            if username is not None and client.username != username:
                continue
            if password is not None and client.password != password:
                continue
            if client.username == "admin":
                admins.append(client)
            elif client.username == "manager":
                managers.append(client)
        return managers, admins


class ProductsRepository(ABC):
    """
    Абстрактный репозиторий для товаров.
    Он содержит методы, которые нужно реализовать в случае если захочется сделать новую реализацию репозитория.
    Принцип такой же как и у клиентов.
    """

    @abstractmethod
    def add_product(self):  # добавление товара
        pass

    def remove_product(self):  # удаление товара
        pass

    def change_price(self):  # изменить цену
        pass

    def change_content(self):  # изменить описание
        pass

    def get_products(self):
        pass


class ShelveProductsRepository(ProductsRepository, ABC):
    def __init__(self):
        self.db_name = "product"

    def get_products(self) -> list[Product]:
        with shelve.open(self.db_name) as db:
            return list(db.values())

    def create_product(self, product: Product):
        with shelve.open(self.db_name) as db:
            db[product.id] = product

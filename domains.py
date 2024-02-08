from dataclasses import dataclass


@dataclass
class Client:
    """Клиент"""
    id: str


@dataclass
class Manager(Client):
    """Пользователь с правом смены цены и описания товара"""
    username: str
    password: str


@dataclass
class Admin(Manager):
    """Имеет права менеджера, а также может добавлять товары на платформу"""
    username: str
    password: str


@dataclass
class Product:
    """Сущность товара"""
    id: str
    title: str
    content: str
    price: int

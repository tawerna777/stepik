from uuid import uuid4

from store.domains import Product, Client
from store.repositories import ProductsRepository, ClientsRepository


def get_articles(products_repository: ProductsRepository) -> list[Product]:
    return products_repository.get_products()


def create_product(
        title: str, content: str, products_repository: ProductsRepository, price: int) -> Product:
    """

    :rtype: object
    """
    product = Product(id=str(uuid4()), title=title, content=content, price=price)
    products_repository.add_product()
    return product


def login(
        username: str, password: str, clients_repository: ClientsRepository
) -> Client | None:
    clients = clients_repository.get_clients(username=username, password=password)
    if clients:
        return clients[0]

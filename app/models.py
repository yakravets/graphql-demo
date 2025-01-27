from typing import List
from uuid import UUID


class Category:
    def __init__(self, id: UUID, parent_id: UUID, name: str):
        self.id = id
        self.parent_id = id
        self.name = name


class Product:
    def __init__(self, id: UUID, name: str, code: str, description: str, price: float, images: List[str], category: Category):
        self.id = id
        self.name = name
        self.code = code
        self.description = description
        self.price = price
        self.images = images
        self.category = category

categories = [
    Category(
        id=UUID("6b9f2b66-1989-447f-88fd-5fffc63817b6"),
        name="Electronics",
        parent_id=UUID("00000000-0000-0000-0000-000000000000")
    ),
    Category(
        id=UUID("15cb8d80-cfc6-4a61-ba95-bf73dfc91c7e"),
        name="Iphone",
        parent_id=UUID('6b9f2b66-1989-447f-88fd-5fffc63817b6')
    ),
    Category(
        id=UUID("c7a4a669-5369-4ada-9d7d-d92de814e77c"),
        name="Ipad",
        parent_id=UUID("6b9f2b66-1989-447f-88fd-5fffc63817b6")
    )
]

products = [
    Product(
        id=UUID("7a96f3ba-eaa2-44c6-ae25-53efb720332e"),
        name="Iphone 16",
        description="Iphone 16",
        price=1999.00,
        images=["image1.jpg", "image2.jpg"],
        category=categories[1],
        code='001'
    ),
    Product(
        id=UUID("644c0175-d6d1-475b-9a83-7fcc6918510a"),
        name="Ipad 2024",
        description="Powerfull tablet",
        price=1500.00,
        images=["image3.jpg", "image4.jpg"],
        category=categories[2],
        code='002'),
    Product(
        id=UUID("00c1252b-770b-453f-8024-abfcf94b3675"),
        name="Iphone 15",
        description="Iphone 16",
        price=1799.00,
        images=["image5.jpg"],
        category=categories[1],
        code='003')
]
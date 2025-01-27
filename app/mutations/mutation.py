from ariadne import MutationType
from app.models import categories, products, Category, Product
import uuid

mutation = MutationType()

@mutation.field("createProduct")
def resolve_create_product(_, info, name: str, code: str, description: str, price: float, images: list, category_id: str):

    category = next((category for category in categories if category.id == category_id), None)

    if not category:
        raise ValueError(f"Category not found")

    product = Product(
        id=uuid.uuid4(),
        name=name,
        code=code,
        description=description,
        price=price,
        images=images,
        category=category
    )
    products.append(product)
    return product


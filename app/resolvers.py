from ariadne import QueryType
from .models import categories, products, Category, Product

query = QueryType()

# Резолвер для отримання всіх товарів
@query.field("products")
def resolve_products(_, info):
    return products

# Резолвер для отримання товару за ID
@query.field("productById")
def resolve_product_by_id(_, info, id):
    return next((product for product in products if product.id == id), None)

# Резолвер для отримання всіх категорій
@query.field("categories")
def resolve_categories(_, info):
    return categories

# Резолвер для отримання категорії за ID
@query.field("categoryById")
def resolve_category_by_id(_, info, id):
    return next((category for category in categories if category.id == id), None)

from ariadne import QueryType, MutationType
from app.models import categories, products, Category, Product

query = QueryType()

@query.field("products")
def resolve_products(_, info):
    return products

@query.field("productById")
def resolve_product_by_id(_, info, id):
    return next((product for product in products if product.id == id), None)

@query.field("categories")
def resolve_categories(_, info):
    return categories

@query.field("categoryById")
def resolve_category_by_id(_, info, id):
    return next((category for category in categories if category.id == id), None)

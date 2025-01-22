from ariadne import make_executable_schema
from .resolvers import query

# Опис схеми GraphQL
type_defs = """
    type Product {
        id: ID!
        name: String!
        code: String!
        description: String!
        price: Float!
        images: [String]!
        category: Category!
    }

    type Category {
        id: ID!
        name: String!
        parent_id: String!
    }

    type Query {
        products: [Product]!
        productById(id: ID!): Product
        categories: [Category]!
        categoryById(id: ID!): Category
    }
"""

# Створення схеми
schema = make_executable_schema(type_defs, query)

from ariadne import make_executable_schema
from app.queries.query import query
from app.mutations.mutation import mutation

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
    
    type Mutation {
        createProduct(
            name: String!, 
            code: String!, 
            description: String!, 
            price: Float!, 
            images: [String]!, 
            category_id: ID!
        ): Product
    }
"""

# Створення схеми
schema = make_executable_schema(type_defs, [query, mutation])

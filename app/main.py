from fastapi import FastAPI
from ariadne.asgi import GraphQL
from app.schema import schema

# Створення FastAPI додатку
app = FastAPI()

# Додавання маршруту для GraphQL
app.add_route("/graphql", GraphQL(schema, debug=True))

# Стандартний маршрут для перевірки
@app.get("/")
async def root():
    return {"message": "Hello World"}

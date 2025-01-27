from fastapi import FastAPI
from ariadne.asgi import GraphQL
from app.schema import schema
from fastapi.responses import RedirectResponse

app = FastAPI()
app.add_route("/graphql", GraphQL(schema, debug=True))

@app.get("/")
async def root():
    return RedirectResponse(url="/graphql")

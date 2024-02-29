from fastapi import FastAPI
from routes import articles
from routes import asyncio_test

app = FastAPI()


app.include_router(articles.router)
app.include_router(asyncio_test.router)

@app.get("/")
async def root():
    return {"message": "Hello I'm FastAPI"}
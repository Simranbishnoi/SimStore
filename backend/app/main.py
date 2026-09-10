from fastapi import FastAPI
from app.routers import books

app = FastAPI(title="The Reading Room API")

app.include_router(books.router)


@app.get("/")
def root():
    return {"message": "The Reading Room API is running"}
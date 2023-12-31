from fastapi import FastAPI
from dotenv import dotenv_values
from pymongo import MongoClient
from routes import router as book_router

config = dotenv_values(".env") # 환경 변수 가져오기

app = FastAPI()


@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(config["ATLAS_URI"])
    app.database = app.mongodb_client[config["DB_NAME"]]
    print("Connected to the MongoDB database!")

@app.get("/")
async def root():
    return {"message":"Welcome to the PyMongo tutorial!"}


app.include_router(book_router, tags=['books'], prefix="/book")

from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def home():
    return {"message": "My name is ANABIA"}

@app.get("/student")
def student():
    return {
         "name": "Ali",
         "age": 20,
         "course": "Python"
         }

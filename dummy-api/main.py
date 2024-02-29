from fastapi import FastAPI
from time import sleep
from random import choice

app = FastAPI()

NAMES = ["Frank", "Christian", "Sebastian", "Thomas", "Name"]

@app.get("/")
def root() -> str:
    sleep(0.5)
    return choice(NAMES)
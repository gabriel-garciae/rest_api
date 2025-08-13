from fastapi import FastAPI
import random

servidor = FastAPI()

@servidor.get("/recursos")
def numero_aleatorio():
    num = random.randint(1, 100)
    print(num)
    return num
import time
import os
import random

def numero_aleatorio():
    num = random.randint(1, 100)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    arquivo_path = os.path.join(script_dir, "recursos", "arquivo.txt")
    with open(arquivo_path, "a") as file:
        file.write(f"{num}\n")

if __name__ == "__main__":
    while True:
        numero_aleatorio()
        time.sleep(1)
import random
import time

def le_ultimo_numero():
    with open("recursos/arquivo.txt", "r") as file:
        return int(file.readlines()[-1])

def main():
    print(le_ultimo_numero())

if __name__ == "__main__":
    while True:
        print(le_ultimo_numero())
        time.sleep(1)
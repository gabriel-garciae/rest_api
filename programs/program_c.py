import random

def numero_aleatorio():
    return random.randint(1, 100)

def dobro_numero(numero: int):
    return numero * 2

def main():
    print(numero_aleatorio())
    print(dobro_numero(numero_aleatorio()))

if __name__ == "__main__":
    main()
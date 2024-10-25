if __name__ == '__main__':
    a = int(input("Teclea un numero: "))
    b = int(input("Teclea otro numero: "))
    c = int(input("Teclea uno mas: "))

    if a>b:
        if a>c:
            print(f"El mayor es {a}")
        else:
            print(f"El mayor es {c}")
    elif b>c:
        print(f"El mayor es {b}")
    else:
        print(f"El mayor es {c}")
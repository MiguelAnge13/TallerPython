import math

if __name__ == "__main__":
    Suma = lambda x,y:x+y
    print(f"La suma es {Suma(2,6)}")

    Resta = lambda x, y: x - y
    print(f"La resta es {Resta(2, 6)}")

    Potencia = lambda x:x**2
    print(f"La potencia de 2 es {Potencia(2)}")

    X1 = lambda a,b,c:(-b + math.sqrt(b**2 - 4*a*c)/2*a)
    X2 = lambda a,b,c:(-b - math.sqrt(b**2 - 4*a*c)/2*a)
    print(f"El resultado de la formula general es: {X1(2,5,1)} y {X2(2, 5, 1)}")
import math

class FormulaGral:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def pot(self) -> float:
        return self.b * self.b
    def multi(self) -> float:
        return self.a * self.c * 4
    def r(self) -> float:
        return math.sqrt(self.pot() - self.multi())
    def x1(self) -> float:
        x1 = (-self.b + self.r())/(2 * self.a)
        return x1
    def x2(self) -> float:
        x2 = (-self.b - self.r()) / (2 * self.a)
        return x2

if __name__ == "__main__":
    resultado = FormulaGral(2, 5, 3)
    print(f"x1 = {resultado.x1()}, x2 = {resultado.x2()}")
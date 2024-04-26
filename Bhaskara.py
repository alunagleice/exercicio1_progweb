import math

def calcular_bhaskara(a, b, c):
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        return "A equação não possui raízes reais."
    elif delta == 0:
        raiz = -b / (2 * a)
        return f"A equação possui uma raiz real: {raiz}"
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-b - math.sqrt(delta)) / (2 * a)
        return f"A equação possui duas raízes reais: {raiz1} e {raiz2}"

# Exemplo de uso
a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))

resultado_bhaskara = calcular_bhaskara(a, b, c)
print(resultado_bhaskara)

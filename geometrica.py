import math

def calcular_area_retangulo(base, altura):
    area = base * altura
    return area

def calcular_area_triangulo(base, altura):
    area = (base * altura) / 2
    return area

def calcular_area_circulo(raio):
    area = math.pi * (raio ** 2)
    return area

# Exemplo de uso
opcao = input("Escolha a forma geométrica (R para retângulo, T para triângulo, C para círculo): ")

if opcao.upper() == 'R':
    base = float(input("Digite a base do retângulo: "))
    altura = float(input("Digite a altura do retângulo: "))
    area_retangulo = calcular_area_retangulo(base, altura)
    print("A área do retângulo é:", area_retangulo)
elif opcao.upper() == 'T':
    base = float(input("Digite a base do triângulo: "))
    altura = float(input("Digite a altura do triângulo: "))
    area_triangulo = calcular_area_triangulo(base, altura)
    print("A área do triângulo é:", area_triangulo)
elif opcao.upper() == 'C':
    raio = float(input("Digite o raio do círculo: "))
    area_circulo = calcular_area_circulo(raio)
    print("A área do círculo é:", area_circulo)
else:
    print("Opção inválida. Escolha R para retângulo, T para triângulo ou C para círculo.")
    
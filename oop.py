# class Pessoa:
#     def __init__(self, nome):
#         self.nome = nome
#     def __str__(self):
#         return self.nome

# igor = Pessoa('Igor Camões de Oliveira')

# print(igor)

# #arquivo animal_estimacao.py
# class AnimalEstimacao():
#     def __init__(self, nome, especie, dono):
#         self.nome = nome
#         self.especie = especie
#         self.dono = dono
#     def __str__(self):
#         return self.nome

#             # dono = AnimalEstimacao('Thaina')
#             # capivara = AnimalEstimacao('Capivara de Santa Isabel')
#             # isabellita = AnimalEstimacao('Isabellita')

# #novo arquivo
# import animal_estimacao as animal 

# isabellita = animal.AnimalEstimacao('Isabellita', 'capivara', 'Thaina')
# bob = animal.AnimalEstimacao('Bob', 'quati', 'Thaina')

class Calculadora:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def soma(self):
        return self.a + self.b
    
    def sbtr(self):
        return self.a - self.b
    
    def divs(self):
        return self.a / self.b

    def mult(self):
        return self.a * self.b

a = float(input("Qual o primeiro valor que deseja calcular? "))
b = float(input("Qual o segundo valor que deseja calcular? "))

teste = Calculadora(a,b)

print(f'Soma: {teste.soma():.1f}')
print(f'Subtração: {teste.sbtr():.1f}')
print(f'Divisão: {teste.divs():.1f}')
print(f'Multiplicação: {teste.mult():.1f}')


# meios de importar

# import math > IMPORTA TODO MODULO MATH 
# from math import sqrt > IMPORTA A FUNÇÃO SQRT DO MODULO MATH 
"""Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira"""


import math
num = float(input("Digite um numero qualquer:"))
print(f"o numero {num} tem como sua porção inteira {math.trunc(num)}")

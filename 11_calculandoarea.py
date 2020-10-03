"""Ler altura e largura de uma parede, calcular area e informar quantas litros de tinta serão necessarios, lembrando que cada litro equivale pra 2m²"""
altura = int(input("Quantos metros de altura tem sua parede"))
largura = int(input("Quantos metros de largura tem sua parede"))
area = altura * largura
litro = 2

print(f"Sua parede tem {altura}mts e {largura}mts, totalizando uma area de {area}metros. Com {area / litro} de tinta você consegue pintar sua parede")

"""Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado."""

percorridos = float(input("Quantos Kms você rodou com o carro?"))
dias = int(input("Quantos dias o carro está alugado?"))

dias_usados = 60
km_percorridos = 0.15

print(f"Você rodou {percorridos}kms com o carro, e ficou {dias} dia (s)")
print(f"O valor por km percorrido ficou em {km_percorridos * percorridos}R$")
print(f"O valor por diaria ficou em {dias * dias_usados}R$")
print(f"Totalizando {km_percorridos * percorridos + dias * dias_usados}R$")

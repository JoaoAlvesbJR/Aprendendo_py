"""022: Crie um programa que leia o nome completo de uma pessoa e mostre: 
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome."""


frase =str(input("digite uma frase"))


maiusc = frase.upper()
minusc = frase.lower()
print(f"A frase digitada em maiuscula fica assim: {maiusc}")
print(f"A frase digitada em minuscula fica assim: {minusc}")
print("Ao todo a frase tem {} caracteres.".format(len(frase) - frase.count(' ')))

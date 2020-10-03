"""O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada."""
import random
alunos = ["Diego","Léo","Rodrigo","João"]
print(f"{random.sample(alunos, k=4)}")  #O "k" representa a quantidade de elementos da lista

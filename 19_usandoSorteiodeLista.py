"""Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido."""

import random
alunos = ["Diego", "Léo", "João", "Rodrigo"]
print(f"o aluno sorteado foi {random.choice(alunos)}")#random.choice(lista) realiza o sorteio dentro da lista

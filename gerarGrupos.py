#Crie um sistema de cadastro de produtos,
#onde serão passadas todas as informações
#dos produtos, e no final mostre um relatorio
# pelo menos três produtos
#Informações dos produtos serão:
#Nome, fabricante, quantidade em estoque, preço, valor da total.

from random import *

alunos = ["Thaylon", "Nayra", "Kauan", "Jaquesson", "Maria Eduarda", "Maria Isaura", "Clardson", "Eliezio"]
grupos = 2
integrantes = 4
adicionados = []


for x in range(1, (grupos+1)):
    print("Grupo ", x)
    for y in range(1, (integrantes+1)):
        r = randint(1, 8)
        while r in adicionados:
            r = randint(1, 8)
        adicionados.append(r)
        print( alunos[r-1])
    print("\n")

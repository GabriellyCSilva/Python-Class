#Bubble sort
#Ordena o sistema por metodos de bolhas, a bolha de maior tamanho sobe mais rapido para o topo da piscina
#Ele vai comprando e "borbulhando" até terminar de ajustar a lista

#Ex1
#A) Troque dois elemntos (i e j) de uma lista

"""i = 1
j = 2

a = i
a = j
j = i
i = a

print(i , j)"""

#B) Faça a troca de uma iteração do algoritimo (até a posição i)

"""l=[12,68,95,25,71]
for interacao in range(len(l)-1,0,-1): #só o l tabem funciona mas ele percorre varias vezes
    for i in range(interacao):
        if l[i]> l[i+1]:
            aux = l[i]
            l[i] = l[i+1]
            l[i+1]=aux
        print(l)"""



#Selection sort
#Faz o processo ao contrario
#Esse não compara, ele só acha o menor e ja coloca no começo

#Crie uma função que vai retornar o indice do menor elemento de uma lista

"""l=[12,68,95,10,71]
aux = l[0] #auxiliar para começar a comparação
a = 0
for i in range(1,len(l)): #len começando a contar do 1
    if l[i] < aux:
        aux = l[i]
        a = i
print(a)
print(aux)"""

#Agora pegue o menor a partir de uma posição inicial dada i
"""l=[12,68,95,10,71,30]
aux = l[0]
a = 0

for j in range(4,len(l)):
    aux1 = l[j]
    if l[j] < aux1:
        aux1 = l[j]
print(aux1)"""

"""#para criar o programa  
j = index(l,0)
aux = l[0]
l[0] = l[j]
l[j] = aux
print(l)"""


#insertion sort
#inserir a posição correta
#assume que a lista esta entre as posiçoes zero e zero

#Assuma que temos uma lista ordenada com exceção do ultimo elemento. Insira esse elemento de forma ordenada na lista
"""l1 = [12,41,68,71,95,52]

aux= 1

while l1[aux]<l1[-1]:
    aux += 1
    troca = l1[aux]
    l1[aux] = l1[-1]
    l1[-1] = troca
print(l1)"""

#ou
"""l = [12,41,68,71,95,52]

i = 5
aux = l[i]
j = i -1
while j >= 0 and l[j] > aux:
    l[j+1] = l[j]
    j = j - 1
    print(l)
l[j+1] = aux
print(l)"""

#Quando não assumimos qual está errado
"""l = [12,45,68,100,93,52]

for i in range(len(l)):
    aux = l[i]
    j = i -1
    while j >= 0 and l[j] > aux:
        l[j+1] = l[j]
        j = j - 1
        print(l)
    l[j+1] = aux
    print(l)
print(l)"""













#list comprehensions
import random

a = [1,2,3,4,5,6,7,8,9,10]
b = [i for i in a if i%2==0]  #para pegar os pares da lista
print(b)

#ou podemos passaar as condições com range
b = [i for i in range(1,101) if i%2==0]  #para pegar os pares da lista
print(b)

#para printar numeros aleatorios
a= [random.uniform(-1,1) for i in range(1,11)]
print(a)

#crie uma lista com os quadrados dos números 1 a 10

a = [i*i for i in range(1,11)]
print(a)

#gere uma lista contendo apenas os numeros pares de 1 a 20

a=[i for i in range(1,21) if i%2==0]
print(a)

#crie uma lista contendo o comprimento de cada palavra na lista

a = ["Python", "List", "Comprehension", "Exercícios"]

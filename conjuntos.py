#estrutura de dados que implementa operações de: união, intersecção, diferença
#A principal carct é não admitir repetição de elementos
#não mantem as ordens dos elementos

#declaro da seguinte maneira
a = set()
print(a) #printa apenas o set // o type coloca a classificação

#para adicionar
a.add(45)  #quando printamos depois de adicionar, printa apenas o valor dentro de {}
a.add('a') #podemos adicionar string
#não aceita lista
#caso adicione o mesmo elemento duas vezes, ele não adiciona

#para testar se faz parte do conjunto
print(1 in a) #retorna true or false

#colocando uma lista dentro
b = [1,2,3,4,5,6,7]
a = set(b) #adiciona os itens da lista dentro

#transformando o conjunto em lista
c = list(a)
#caso queira tirar a duplicidade dos itens da lista, podemos fazer esses passos, pois volta a lista e retira a duplicidade

#AUB = unir os dois sem as repetições  /// união = |
#AU(invertido)B = apenas as repetições  /// repetição = &
#A - B = Tudo que esta no A mas não esta no B

#exemplos
a = set([1,2,3])
b = set([2,3,5])
print(a)
print(b)
print(a-b)
print(a | b) #união
print(a & b) #repetição

#Exercícios

list1 = [1,2,34,5,6]
list2 = [1,23,56,78,9]
c = set(list1)
d = set(list2)

#ex1 - valores comuns as duas listas
print(c | d)

#ex2 - valores só da primeira lista
print(c-d)

#ex3 - os valores que existem apenas na segunda
print(d-c)

#ex4 - Uma lista com os elementos não repetidos das duas listas
print(c^d)
#ou
f = (c-d) | (d-c)  #ou  (c-d) - (c&d)
print(f)

#as chaves nos dicionarios são unicas






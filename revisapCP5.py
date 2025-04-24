#Dicionario
#São estruturas para armazenar daods, mapeamentos formados por chave-valor
#Representa uma coleção não ordenada de valores onde cada valor é referenciado através de sua chave
#Podemos também declarar um dicionário de maneira explícita utilizando a função dict

#Acessando valores do dicionário
#Acessamos um valor do dicionário da seguinte forma:
"""nome_do_dicionario[chave]"""
from unicodedata import numeric

#Essa operação retorna o valor associado à chave informada
#Se informarmos uma chave que não esta dentro do dicionário, ele retorna uma erro

#Podemos utilizar o get para localizar  uma chave dentro do dicionario tambem
"""nome_do_dicionario.get("chave")""" #Se estivver retorna o valor, se não estiver retorna none


#Assim como em listas, podemos verificar se uma chave está dentro do dicionário atravès do "in"
"""chave in nome_do_dicionario"""


#Podemos verificar o tamanho de um dicionário através do comando len
"""len(nome_do_dicionario)"""


#Para adicionar chaves dentro do dicionario
"""nome_do_dicionario["chave"] = "Valor"""


#Para atualizar um valor ja existente
"""nome_do_dicionario["chave"]=valor"""


#Removendo valores // POP // DEL // popitem
#Para remover, podemos utilizar o metodo pop, ele recebe como parametro a chave que está associada ao valor que deve ser removido, caso a chave informada não esteja no dicionario, retorna um erro
"""nome_do_dicionario.pop("chave")"""

#Outra forma de remover é utilizando o comando del, caso o parametro informado não esteja no dicionario, um erro é gerado
"""del nome_do_dicionario["chave"]"""

#O metodo popitem remove sempre o ultimo par (chave-valor), e como reposta ele retorna o removido, se o dicionario estiver vazio, ele retorna um erro
"""nome_do_dicionario.popitem()"""


#Para atualizar um dicionário
#update pode ser utilizado para atualizar um dicionário , esse metodo recebe como parâmetro outro dicionário
"""dicionrio_atualizar.update(dicionario_parametro)"""
#Nesse caso, ele só adiciona as informações que não tem no dicionario_atualizar, mas tem no dicionario_parametro


#Chaves e Valores de um Dicionário
#O metodo keys retorna as chaves do dicionario, podemos tranformar em uma lista
"""lugar = {"Lat": -22.817087, "Long": -47.069750} #dicionario
print(lugar.keys()) #printando só as chaves 
# dict_keys(['Lat', 'Long '])
print(list(lugar.keys())) #tranformando em uma lista 
# ['Lat', 'Long']"""

#O metodo values retorna os valores de um dicionario, podemos transformar em uma lista
"""lugar = {"Lat": -22.817087, "Long": -47.069750} #dicionario
print(lugar.values()) #printando valores
# dict_values([-22.817087, -47.06975])
print(list(lugar.values())) #tranformando em lista 
# [-22.817087, -47.06975]"""

#O metodo items retorna uma estrutura que pode ser convertida para uma lista de tuplas, onde cada tupla é composta pelo par(chave-valor)
"""lugar = {"Lat": -22.817087, "Long": -47.069750} #dicionario
print(lugar.items())  #printando todos os pares 
# dict_items([('Lat', -22.817087), ('Long', -47.06975)])
print(list(lugar.items()))  #tranformando em tuplas 
# [('Lat', -22.817087), ('Long', -47.06975)]"""


#Iterando sobre Dicionários
#Podemos iterar sobre uma lisa de chaves utilizando o metodo keys // Iterar=percorrer
"""dic = {
"A": "Abacate",
"B": "Banana",
"C": "Caqui"
}
for letra in dic.keys(): #percorre apenas as chaves
    print("Letra:", letra)"""

#Podemos fazer a mesma coisa com os valores
"""dic = {
"A": "Abacate",
"B": "Banana",
"C": "Caqui"
}
for fruta in dic.values():  #percorre os valores
    print("Fruta:", fruta)"""

#Podemos também iterar sobre uma lista de tuplas contendo as chaves e os valores utilizando o metodo items.
"""dic = {
"A": "Abacate",
"B": "Banana",
"C": "Caqui"
}
for letra, fruta in dic.items():  #|aqui temos duas variáveis temporárias pois estamos falando de dois elementos
    print("Fruta com Letra ", letra, ": ", fruta, sep = "")"""

#Isso só funciona porque .items() retorna tuplas com dois elementos, e o Python sabe desempacotar isso nessas duas variáveis. Então, sim, isso funciona especificamente com estruturas que retornam pares ou outro tipo de sequência com múltiplos elementos
#ou seja, só funcionaria casa haja DOIS elementos

#Exercício 1 - Escreva um programa que dada a lista a seguir:
"""dados = [
{"dia": 12, "mes": 2, "ano": 2019, "temp": 30.5},
{"dia": 18, "mes": 3, "ano": 2019, "temp": 29.1},
{"dia": 22, "mes": 4, "ano": 2019, "temp": 28.5},
{"dia": 17, "mes": 5, "ano": 2019, "temp": 26.4}
]

for registro in dados: #aqui ele printa cada dicionario dentro da lista
    dia = registro["dia"] #aqui estamos criando variaveis e adicionando os valores de foma temporaria, passando qual informação acessar
    mes = registro["mes"]
    ano = registro["ano"]
    temp = registro["temp"]
    print(f"{dia:02}/{mes:02}/{ano}: Temperatura: {temp:.1f}C")"""
#f"{dia:02}" Isso quer dizer: “Formate o número com no mínimo 2 dígitos. Se tiver menos, preencha com zero na frente.
#f"{temp:.1f}" Isso quer dizer: “Formate esse número como ponto flutuante (decimal), com 1 casa após o ponto.


#Excercícios Dicionário
#1. Criação de um dicionário - Crie um dicionário com três pares chave-valor. As chaves devem ser os nomes de três frutas e os valores, suas respectivas cores.
dic_fruta= {
    "Uva":"Roxo",
    "Laranja":"Laranja",
    "Limão":"Verde"
}

#2. Acesso a um valor - Usando o dicionário criado no exercício anterior, acesse e imprima a cor de uma das frutas.
"""print(dic_fruta["Uva"])"""

#3. Adicionar um novo par chave-valor - Adicione um novo par chave-valor ao dicionário, representando outra fruta e sua cor.
"""dic_fruta["Mamão"]="Laranja"""

#4. Atualizar um valor - Modifique a cor de uma das frutas no dicionário. Substitua o valor atual por uma nova cor.
"""dic_fruta["Mamão"]="Rosa"""

#5. Remover um item - Remova uma fruta do dicionário utilizando o metodo pop().
"""dic_fruta.pop("Mamão")"""

#6. Iterar sobre as chaves - Itere sobre o dicionário e imprima apenas as chaves (nomes das frutas).
"""for i in dic_fruta.keys():
    print(i)"""

#7. Iterar sobre os valores - Itere sobre o dicionário e imprima apenas os valores (cores das frutas).
"""for i in dic_fruta.values():
    print(i)"""

#8. Verificar a existência de uma chave - Verifique se a fruta "banana" está presente no dicionário e imprima uma mensagem com base no resultado.
"""if "banana" in dic_fruta:
    print("Está no dicionário")
else:
    print("Não esta no dicionario")
"""
#9. Combinar dois dicionários - Crie um segundo dicionário com outras frutas e cores. Combine os dois dicionários em um só.
dic_fruta2={
    "Morango":"Vermelho",
    "Maça":"Vermelho",
    "Maracujá":"Amarelo"
}

"""dic_fruta.update(dic_fruta2)
print(dic_fruta)"""

#10. Contar a quantidade de itens - Usando o metodo adequado, imprima o número total de itens no dicionário (pares chave-valor)
"""contador = 0
for i in dic_fruta.items():
    contador+=1
print(f'Neste dicionário temos {contador} itens')
#uma maneira mais facíl é usar o len
print(f'Neste dicionário temos {len(dic_fruta)} itens')"""


#Copiando dicionários
#Similar ao que vimos em listas, podemos atribuir um dicionário para diferentes variáveis, mas as variáveis estarão relacionadas ao mesmo dicionário (objeto)
"""dic_a = {"Nome": "João", "Idade": 18}
print(dic_a)
# {'Nome': 'João', 'Idade': 18}
dic_b = dic_a
dic_b["Nome"] = "Maria"
print(dic_b)
# {'Nome': 'Maria', 'Idade': 18}
print(dic_a)
# {'Nome': 'Maria', 'Idade': 18}
"""
#Isso ocorre porque, você não está criando uma cópia do dicionário. Você está dizendo:
# "dic_b agora aponta para o mesmo dicionário que dic_a."
#Ou seja, os dois nomes estão se referindo ao mesmo lugar na memória. Se mudar um, o outro vê a mudança também — porque são o mesmo objeto

#se quisermos criar uma cópia independente de um dicionário devemos utilizar o metodo copy
"""dic_a = {"Nome": "João", "Idade": 18}
print(dic_a)
# {'Nome': 'João', 'Idade': 18}
dic_b = dic_a.copy()
dic_b["Nome"] = "Maria"
print(dic_b)
# {'Nome': 'Maria', 'Idade': 18}
print(dic_a)
# {'Nome': 'João', 'Idade': 18}"""

#ZIP
#É possível criar um dicionário a partir de duas listas com o auxílio da função zip.
#A função zip recebe dois parâmetros, o primeiro é uma lista contendo as chaves desejadas para o dicionário, enquanto o segundo é uma lista contendo os respectivos valores.
"""pessoas = ["Alice", "Beatriz", "Carlos"]
telefones = ["99999-0000", "99999-1111", "99999-2222"]
contatos = dict(zip(pessoas , telefones))
print(contatos)
# {'Alice': '99999-0000',
# 'Beatriz': '99999-1111',
# 'Carlos': '99999-2222'}"""

#É possível criar um dicionário cujos valores são listas
"""pessoas = {}
n = int(input("Quantas pessoas? "))  #qtd de vazes que o codigo vai rodar
for i in range(n):
    nome = input("Digite o nome: ") #adiconando nome/idadxe/sexo
    idade = int(input("Digite a idade: "))
    sexo = input("Digite o sexo: ")
    pessoas[nome] = [idade, sexo] #adicionando dentro do dicionario o nome, a idade e o sexo, repetindo isso n vezes
print(pessoas)"""

#É possível criar um dicionário cujos valores são dicionários
pessoas = {}
"""n = int(input("Quantas pessoas? "))
for i in range(n):
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    sexo = input("Digite o sexo: ")
    pessoas[nome] = {"idade": idade, "sexo": sexo}
print(pessoas)"""

#Exercícios
#Exercício1: Escreva uma função que receba uma frase como parâmetro e retorne um dicionário, onde cada chave seja um caractere e seu valor seja o número de vezes que o caractere aparece na frase lida.

"""frase = input("Digite a frase: ")
def contar(frase):
    resultado = {} #criando o dicionário vazio para armazenas os pares

    for i in frase: #percorrendo a frase e o i se torna cada letra percorrida
        if i in resultado:
            resultado[i]+=1 #aqui ele já adiciona o dicionário e conta
        else:
            resultado[i] = 1
    return resultado"""
#O dicionario não adiciona duas chaves iguais, por isso as letras não se repetem

#Exercício2: Escreva uma função que recebe uma lista e retorna uma nova lista sem elementos duplicados. Lembre-se que os elementos duplicados não precisam aparecer em posições consecutivas.

"""lista1 = ["cachorro","gato","cachorro","gato"]
def remov_duplicatas(lista1):
    dict1={}
    for i in lista1:
        dict1[i]=''
    result = list(dict1.keys())
    return result"""

#Exercício3: Escreva uma função que recebe uma lista de compras e um dicionário contendo o preço de cada produto disponível em uma determinada loja, e retorna o valor total dos itens da lista que estejam disponíveis nesta loja. Por exemplo, para os dados:
"""lista_de_compras = ['biscoito', 'chocolate', 'farinha']
supermercado = {
'amaciante':4.99,
'arroz':10.90,
'biscoito':1.69,
'cafe':6.98,
'chocolate':3.79,
'farinha':2.99
}
def valor_compras(lista_de_compras,supermercado):
    valor_total = 0
    
    for i in lista_de_compras:
        if i in supermercado:
            valor_total += supermercado[i]  #quando passamos o dicionario e sua chave, ele retorna o valor dessa chave
        else:
            print(f"Produto '{i}' não está disponível no supermercado.")
    return valor_total
"""

# Exercício4 - Sabe-se que uma molécula de RNA mensageiro é utilizada como base para sintetizar proteínas, no processo denominado de tradução. Cada trinca de bases de RNA mensageiro está relacionado com um aminoácido. Combinando vários aminoácidos, temos uma proteína. Com base na tabela (simplificada) de trincas de RNA abaixo, crie uma função que receba uma string representando uma molécula de RNA mensageiro válida, segundo essa tabela, e retorne a cadeia de aminoácidos que representam a proteína correspondente.
"""rna_mensageiro = input("Digite o RNA: ")
def traduzir_rna(rna_mensageiro):
    traducao = {
        "UUU": "Phe",
        "CUU": "Leu",
        "UUA": "Leu",
        "AAG": "Lisina",
        "UCU": "Ser",
        "UAU": "Tyr",
        "CAC": "Gln"
    }

    cadeia_aminoacidos = ""

    for i in range(0, len(rna_mensageiro), 3): #começa do indice 0 e vai pulando de 3 em 3
        trinca = rna_mensageiro[i:i+3]  #usamos para fatear a string

        if trinca in traducao:
            cadeia_aminoacidos += traducao[trinca] + "-"
        else:
            cadeia_aminoacidos += "???-"

    return cadeia_aminoacidos"""


#Exercício: Escreva uma função que converte números inteiros entre 1 e 999 para algarismos romanos. Não converta o número para uma string.
#Use os três dicionários abaixo:
"""numero = int(input("Digite um número de 1 a 999: "))
#criação de 3 dicionarios para converter os números
UNIDADES = { 0: '', 1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX' }
DEZENAS = { 0: '', 1: 'X', 2: 'XX', 3: 'XXX', 4: 'XL', 5: 'L', 6: 'LX', 7: 'LXX', 8: 'LXXX', 9: 'XC' }
CENTENAS = { 0: '', 1: 'C', 2: 'CC', 3: 'CCC', 4: 'CD', 5: 'D', 6: 'DC', 7: 'DCC', 8: 'DCCC', 9: 'CM' }

centena = numero // 100
#Calculamos a parte das dezenas. Ex: 345 % 100 = 45 → 45 // 10 = 4
dezena = (numero % 100) // 10  #retorna o resto da devisao e depois divide por mais 10 para pegar apenas a dezena
unidade = numero % 10

romano = CENTENAS[centena] + DEZENAS[dezena] + UNIDADES[unidade]

print(romano)
"""

#Tuplas
#Tuplas são uma sequência de elementos separados por vírgulas, representados ou não entre parênteses, isto é, os parênteses não são obrigatórios.
#Pode-se ainda misturar elementos de tipos diferentes.
#Porém, ao contrário de listas, as tuplas são imutáveis
#Podemos declarar uma tupla utilizando ().
"""variavel = (elemento_1 , elemento_2 , ..., elemento_n)"""
#Também podemos declarar uma tupla de maneira explícita utilizando a função tuple.
"""variavel = tuple([elemento_1 , elemento_2 , ..., elemento_n])"""

#Declaração implícita: É quando você cria a tupla direto com parênteses :
got = ("Game of Thrones", 2011, 2019, 9.4)
#Você está dizendo: “Ei, Python, aqui está uma tupla com 4 elementos”.

#Declaração explícita: É quando você usa a função tuple()para converter outra estrutura (como uma lista) em uma tupla:
got = tuple(["Game of Thrones", 2011, 2019, 9.4])
#Aqui, você criou uma lista dentro, eem tupladentro dos colchetes [], e depois a transformou em tupla.usando tuple()

#Caso tente alterar um tupla, gera um erro informando que o tipo tupla não permite modificações
#Tudo o que vimos para listas também podemos aplicar para tuplas, exceto operações, métodos ou funções que adicionem, removam ou modifiquem elementos

#Verificando se um elemento está na tupla:
"""print("House MD" in top5)""" #Se estiver, retorna True, se não estiver, retorna False

#Concatenando tuplas:
"""a = (1, 2)
b = (3, 4)
c = (5, 6)
print(a + b + c)
# (1, 2, 3, 4, 5, 6)
print(c + b + a)
# (5, 6, 3, 4, 1, 2)
print(b + c + a)
# (3, 4, 5, 6, 1, 2)"""

#Obtendo a posição de um elemento em uma tupla:
"""cinema = ("Sony Pictures", "Walt Disney", "Universal Pictures", "Warner")
print(cinema.index("Warner"))  //para verificar se está na tupla, utilizando o comando .index
# 3
print(cinema.index("Disney"))
# ValueError: tuple.index(x): x not in tuple"""

#Imprimindo todos os elementos de uma tupla (um elemento por linha).
"""cinema = ("Sony Pictures", "Walt Disney",
"Universal Pictures", "Warner")
for estudio in cinema:
    print(estudio)"""

#Tuplas: Empacotamento e Desempacotamento
#Os elementos de uma tupla podem ser acessados de uma forma implícita na atribuição (conhecido como desempacotamento).

#Exemplo:
"""tupla = ("Gabrielly", 19, "FIAP")

nome, idade, faculdade = tupla  #O número de variáveis ​​tem que ser igual ao número de elementos da tupla, caso não seja, um erro é gerado

print(nome)       # Gabrielly
print(idade)      # 19
print(faculdade)  # FIAP"""


#Se tiver um valor que você não quer usar , pode usar _:
"""tupla = ("Gabrielly", 19, "FIAP")
nome, _, faculdade = tupla

print(nome)       # Gabrielly
print(faculdade)  # FIAP"""

#A tupla também pode ser implicitamente criada apenas separando os elementos por vírgula (conhecido como empacotamento).

#Split
#O .split() é um metodo muito útil em Python para dividir strings em partes menores baseadas em um separador.
#Exemplo básico:
"""frase = "Olá mundo Python"
palavras = frase.split()
print(palavras)  # Saída: ['Olá', 'mundo', 'Python']"""

#Tuplas: enumerate
#A função enumerate() é usada para adicionar um contador a um iterável (como listas, tuplas ou strings), retornando um objeto enumerado que produz tuplas contendo:
frutas = ('maçã', 'banana', 'laranja')

"""for tupla_enumerada in enumerate(frutas):
    print(tupla_enumerada)

# Saída:
# (0, 'maçã')
# (1, 'banana')
# (2, 'laranja')"""
#para printar em sequencia sem usar o for, precisamos converter em lista
"""print(list(enumerate(frutas)))
# Saída: [(0, 'maçã'), (1, 'banana'), (2, 'laranja')]"""

#Acesso direto aos pares
"""enum = enumerate(['primeiro', 'segundo', 'terceiro'], start=1)

# Pegando o próximo item com next()
print(next(enum))  # (1, 'primeiro')
print(next(enum))  # (2, 'segundo')
"""

#Tuplas: List Comprehension
"""tuple(x for x in range(n))
tuple([x for x in range(n)])"""

#Exercicio1 - Crie um maneira para adicionar elementos em uma tupla

"""tupla = 1,2,3,4
add = list(tupla)
add.append(5)
tupla = tuple(add)  # Atribui a nova tupla à variável
print(tupla)            # Agora sim imprime a tupla (1, 2, 3, 4, 5)"""

#Exercicio2 - Crie um maneira para remover elementos em uma tupla
"""tupla = 1,2,3,4
remover = list(tupla)
remover.pop(3)
tupla = tuple(remover)
print(tupla)
"""

#Exercicio 3 - Crie um maneira para adicionar elementos em uma tupla

"""tupla = 1,2,3,4
qtd = int(input("Digite a quantidade de elementos que gostaria de adicionar"))
for i in range(qtd):
    list1 = list(tupla)
    list1.append(input("Digite o elemento que gostria de add: "))
    tupla = tuple(list1)
print(tupla)"""

#Crie um maneira para remover elementos em uma tupla
"""tupla = 1,2,3,4
qtd = int(input("Digite a quantidade de elementos que gostaria de remover"))
list2 = list(tupla)
for i in range(qtd):
    elemento = int(input("Digite o elemento que gostria de remover: "))
    if elemento in tupla:
        list2.remove(elemento)
    else:
        print("Esse elemento não está na tupla")
tupla = tuple(list2)
print(tupla)"""

#Criando uma tupla de forma iterativa
"""qtd = int(input("Digite a qtd de elementos que gostaria de adicionar: "))
tupla = ()
list1 = []
for i in range(qtd):
    elemento = input("Digite o elemento que gostaria de add: ")
    list1.append(elemento)
tupla = tuple(list1)
print(tupla)"""

#Conjuntos (set)
#Estrutura de dados que implementa operações de: união, intersecção, diferença
#Principal característica é não admitir repetição de elementos (como os conjuntos em matemática)
#Conjuntos não mantêm a ordem de seus elementos
"""a = set() #conjunto vazio.
print(type(a))
# <class ‘set'>"""

#Testar se um elemento faz parte do conjunto utilizamos o IN

#Existem operações de:

#Diferença:
"""a = {0, 1, 2, 3, -1}
b = {2, 3}
print(a - b)
# {0, 1, -1} elementos de a que não estão presentes em b"""

#União:
"""print(a | b)
# {0, 1, 2, 3, -1}
c = set([4, 5, 6])
print(a | c)"""

#Intersecção:
"""a = {0, 1, 2, 3, -1}
b = {2, 3}
print(a & b)
# {2, 3} elementos de a que também estão presentes em b"""

#Exercício1: Escreva uma programa que compare duas listas. Utilizando operações de conjuntos, imprima:
"""lista1 = [1,2,3,4,5,6,8,9]
lista2 = [4,6,2,7,8,9,10,11]
conjunto1 = set(lista1)
conjunto2 = set(lista2)
#1) Os valores comum às duas listas
print("Valores comuns:", conjunto1 & conjunto2)

#2) Os valores que só existem na primeira
print(conjunto1-conjunto2)

#3) Os valores que existem apenas na segunda
print(conjunto2-conjunto1)

#4) Uma lista com os elementos não repetidos das duas listas (^)
print(conjunto1^conjunto2)

#5) A primeira lista sem os elementos repetidos na segunda
print(conjunto1 - conjunto2)"""


#Biblioteca requests

"""import requests
url = f”pegar_url/{complemento}”
r = requests.get(url)
print(r)
print(r.text)
print(r.json())"""


#Exercício: Escreva uma programa que compare duas listas. Utilizando operações de conjuntos, imprima:
#1) Faça uma função para extrair as informações de um dado CEP. (Teste com o seu CEP).
"""import requests
url = f"https://viacep.com.br/ws/{input("Digite seu cep:")}/json/"
r = requests.get(url)
print(r)
print(r.text)
print(r.json())"""

#3) Faça uma função para extrair a quantidade de medalhas totais, ouro, para e bronze do país escolhido.
"""import dicmedalha_revisaocp5 #importa

pais = input("Digite o pais que gostaria de acessar: ")
md_total = 0
text5 = dicmedalha_revisaocp5.dado() #puxa a informação e armazena na variavel
tamanho = len(text5['data']) #quantidade de vezes que precisamos percorrer
for i in range(tamanho):
    cond = text5['data'][i]['name'] #condição passando o parâmetro de onde está o nome do pais 
    if cond == pais:
        md_total = text5['data'][i]["total_medals"]
    else:
        continue
    md_total = text5['data'][i]["total_medals"]

print(md_total)"""

#Bubble sort

#1) Troque dois elementos (i e j) de uma lista
# Lista original
"""lista = [10, 20, 30, 40, 50]
print("Lista original:", lista)
# Índices a serem trocados
i = 1  # Segundo elemento (20)
j = 3  # Quarto elemento (40)
# Fazendo a troca
lista[i], lista[j] = lista[j], lista[i]

print("Lista após troca:", lista)"""

#2) Faça a trocas de uma iteração do algoritmo (até a posição i)

"""lista = [5, 3, 8, 6, 2]  # Lista inicial: [0]=5, [1]=3, [2]=8, [3]=6, [4]=2
print("Lista original:", lista)  # Saída: [5, 3, 8, 6, 2]

i = 3  # Isso limita as comparações até lista[2] vs lista[3]

for j in range(i):  # j vai ser: 0, 1, 2
    if lista[j] > lista[j + 1]:  # Se o atual > próximo
        lista[j], lista[j + 1] = lista[j + 1], lista[j]  # Troca os valores

print("Lista após uma iteração:", lista)  # Saída: [3, 5, 6, 8, 2]"""

#3) Crie o algoritmo

lista = [5, 3, 8, 6, 2]
print("Lista original:", lista)  # [5, 3, 8, 6, 2]
n = len(lista)  # n = 5

for i in range(n):
    for j in range(0, n-i-1):  # A cada passagem, diminui o limite
        if lista[j] > lista[j+1]:
            lista[j], lista[j+1] = lista[j+1], lista[j]
            print(f"Trocou {lista[j+1]} ↔ {lista[j]} | Lista atual: {lista}")

print("Lista ordenada:", lista)  # [2, 3, 5, 6, 8]


#Selection sort









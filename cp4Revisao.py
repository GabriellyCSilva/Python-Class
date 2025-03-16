#Ex 1
#Escreva um programa que leia 2
#números do usuário e exiba o resultado de
#2a x 3b, em que a é o primeiro número e b
#o segundo

"""a = int(input("Digite o valor a: "))
b = int(input("Digite o valor b: "))

result = (2*a) * (3*b)
print(f'O resultado de (2x{a})x(2x{b}) é {result}')"""


#While
#O bloco é repetido enquanto a condição for verdadeira
#A condição é um expressão ou dado do tipo booleano
#O continue pula para a proxima execução do while

#Listas
#Para verificar se o elemento esta ou não em uma lista, usamos o in, ou seja:
#elento in lista
#Esse operador retorna True ou False caso o elemento esteja ou não
#na lista, respectivamente.
#Para adicionar elementos em uma lista, usamos o append:
#nomedalista.append(valorquequeratribuir)
#A operação de soma em listas gera uma nova lista que é o
#resultado de “grudar” lista2 ao final da lista1. Isto é conhecido
#como concatenação de listas
#lista1.extend(lista2): Concatena duas listas
#O operador “*” faz repetições da concatenação
#EXEMPLO:
lista1 = ["oi", "tudo","bem"]
lista2 = ["sim", "e","voce"]
lista1.extend(lista2)

#lista.insert(índice, dado) insere na lista o dado antes da posição
#índice
#del lista[posição] remove da lista o item da posição especificada;
#Também podemos remover um item da lista pelo valor utilizando o
#método remove;
#Podemos contar o número de elementos na lista com um certo
#valor usando o método count
#O método index é utilizado para obter a posição de um elemento
#em uma lista
#Outra opção para remover um elemento de uma lista é utilizando o
#método pop.
#O método pop recebe como parâmetro a posição do elemento a ser
#removido da lista. Caso o parâmetro seja omitido, o último
#elemento da lista será removido.
#Como resposta, o método retorna o elemento removido.
#Cada elemento da posição especificada até o fim da lista é
#realocado para a posição anterior
#O método reverse inverte a ordem dos elementos de uma lista.
#O método reverse não recebe nenhum parâmetro e modifica
#automaticamente a lista
#Uma lista pode ser ordenada utilizando o método sort.
#O método sort possui o parâmetro opcional reverse, que indica se
#a lista deve ser ordenada de forma crescente (False) ou
#decrescente (True). Por padrão, o valor desse parâmetro é False
#(ordenação crescente)
#Podemos usar a função sorted para obter uma cópia ordenada de
#uma lista, sem alterar a lista original
#Se quisermos uma cópia independente de uma lista podemos
#utilizar o método copy.
#O método copy retorna uma cópia da lista
#A função min retorna o menor valor em uma lista:
#A função max retorna o maior valor em uma lista:
#A função sum retorna a soma de todos os elementos de uma lista

#EX2
produtos = ["Caixa", "Lapís", "Caneta","Caneca", "Sapato"]

contador = 0
"""while True:
    escolha = input("Digite Adicionar se quiser adicionar um protudo e retirar se quiser retirar um prodtudo: ")
    if escolha == "adicionar":
        qtd = int(input("Digite a qtd de itens que gostaria de add: "))
        for i in range(qtd):
            add = input("Digite o produto que gostaria de adicionar: ")
            produtos.append(add)
        print(f"Produtos após adição: {produtos}")
    elif escolha == "retirar":
        ret = input("Digite o produto que gostaria de retirar")
        if ret in produtos:
            produtos.remove(ret)  #nesse caso não podemos usar o pop pois ele esperar o indice e não o valor
            print(f"Produto retirado. Produtos restantes: {produtos}")
        else:
            print("Esse produto não está em nossa lista")
    elif escolha == "sair":
        print("Saindo...")
        break
    else:
        print("Opção inválçida")
        continue
print("Inventário final de produtos:", produtos)
"""

#Funções
#def nome(parametros):
#    comandos
#    return valor do retorno

#Os parametros são variáveis que são inicializadas com valores indicados durante a chamada da função
#O comando return devolve para o invocador da função o resultado da execução desta









"""a = open('aula12.txt', 'w')""" #precisa trocar as letras do parâmetro quando for executar leitura
"""txt = a.read()
print(txt)"""

#podemos passar um aparametro no read para o que ele vai ler read(5), que é a qtd de caracter
#txt1 = a.readline() #armazena cada linha em uma lista

"""i = 0
while True:
    txt1 = a.readline() #paa printar todas as linhas precisa estar dentro da repetição, caso contrário,. printa várias vezes a primeira linha
    print(txt1) #para printar um do lado do outro, print(txt1, end='')
    if txt1 == '':
        break"""

#para ler o todos os caracteres, printa o i dentro do while

#todas vez que lemos o arquivo precisamos fechar, utilizando o .close
"""a.close()"""

"""a = open('aula12.txt', 'r+')
a.write('teste.....')"""

#podemos escreve rum arquivo usando o w também, se colocarmos um arquivo que não existe, ele cria e escreve
"""c = open('aula13.txt', 'w')
c.write('teste.....')"""


#Exercicio- Alterando um texto: Faça um programa que altere um texto de um arquivo substituindo a letra 'a' por 'A'
"""d = open('aula12.txt', 'r+')

final = ''
while True:
    txt3 = d.read(1)
    if txt3 == 'a':
        txt3 = 'A'
    final += txt3
    if txt3 =='':
        break
print(final)
d.close()
d = open('aula12.txt', 'w')
d.write(final)
d.close()"""

#Passando os parâmetros
import sys

#para achar o parametro do arquivo
"""argumentos = sys.argv
print(argumentos)

L = open(sys.argv[1],'w')"""

#pickle

import pickle
lista = [65,66,67,68,69]
arqbin = open('arq2.bin', 'wb')

pickle.dump(lista, arqbin)
arqbin.close()

arqbin = open('arq2.bin', 'rb')
a = pickle.load(arqbin)
print(a)
arqbin.close()







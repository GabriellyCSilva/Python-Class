#no site quando colocamos o cep, ele traz um dicionario com as informações
#podemos puxar isso e transformar em python importando bibliotecas
#precisamos instalar a biblioteca requests

"""import requests
url = 'https://viacep.com.br/ws/03622000/json/'

txt = requests.get(url)  #podemos puxar direto do link ou colocando dentro de uma variável
a = txt.json() #ele vem como string mas se colocar o .json ele transforma em dicionario
print(a)"""
#podemos printar as chaves igualmente fazemos nos dicionarios, até porque o json tranforma em dicionario

#EX1 - Faça uma função que extrai as informações dado um cep
"""seu_cep = input("Digite seu cep: ")

def puxar_cep(seu_cep):
    url1 = f'https://viacep.com.br/ws/{seu_cep}/json/'
    txt1 = requests.get(url1)
    b = txt1.json()
    return b"""



#EX2 - Faça uma função que extrai as infos do pokemom

"""pokemon = input("Digite o nome do pokemon que gostaria de puxar: ")
def pokemon_achar(pokemon):
    url2 = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
    txt2 = requests.get(url2)
    c = txt2.json()
    return c['id'], c['types'][0]['type']['name']
print(pokemon_achar(pokemon))"""

#EX3 - Faça uma função para extrair a qtde de medalhas totais de ouro, prata e bronze
"""import medalhas

pais = input("Digite o pais que gostaria de acessar: ")
def puxar_medalhas(medalhas):
    global pais
    text5 = medalhas.dado()
    tamanho = len(text5['data'])
    for i in range(tamanho):
        cond = text5['data'][i]['name']
        if cond == pais:
            md_total = text5['data'][i]["total_medals"]
        else:
            continue
        md_total = text5['data'][i]["total_medals"]
    return md_total
    """








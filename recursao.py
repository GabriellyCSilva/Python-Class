#Revisao recursao
#Calculando o fatorial
def fatorial(n):
    if n == 0:
        return 1
    return n*fat(n-1)

print(fat(5))

def potencia(a, n):
    if n == 0:
        return 1
    else:
        pot = a * potencia(a, n - 1)
        return pot

def sen(x, n):
    if n == 0:
        return x
    else:
        funcao = potencia(-1, n) * (potencia(x, (2*n)+1) / fatorial((2*n) + 1)) + sen(x, n-1) #
        return funcao

def cos(x, n):
    if n == 0:
        return 1
    else:
        funcao = potencia(-1, n) * (potencia(x, (2*n)) / fatorial(2*n)) + cos(x, n-1)
        return funcao
print(cos(0, 50))



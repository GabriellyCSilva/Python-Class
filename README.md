# Python-Class

#calcular média anual

def check(n1,n2,n3):  #pegando as duas maiores notas do check point
    if n1 < n2 and n1 < n3:
        return n2 + n3
    elif n2 < n1 and n2 < n3:
        return n1+ n3
    else:
        return n1 + n2

def nota_sem(n1, n2, n3, sp1,sp2, gs):
    return check(n1, n2, n3) + sp1 + sp2 + gs*0.6   #calculando nota do semestre

def nf(sem1, sem2):     #calculando média final do semestre
    return 0.4*sem1 + 0.6*sem2

nota_final= nf(nota_sem(10, 10, 10, 10, 10, 100) , nota_sem(10, 10, 10, 10, 10, 100))  #calculando a média anual sem a divisão por 10
#nf(nota_sem(n1_1, n2_1, n3_1, sp1_1, sp2_1.gs_1) , nota_sem(n1_2, n2_2, n3_2, sp1_2, sp2_2, gs_2))


print(nota_final/10)

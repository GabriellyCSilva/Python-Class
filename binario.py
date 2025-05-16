import pickle

arqbin = open('arq.2bin', 'rb')
a = pickle.load(arqbin)
print(a)
arqbin.close()
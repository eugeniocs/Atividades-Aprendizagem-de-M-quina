from numpy import *

def run():
    dados = genfromtxt("income.csv", delimiter=",")
    tmpx = 0
    tmpy = 0

    for i in range (1, len(dados)):
        x = dados[i, 0]
        y = dados[i, 1]
        tmpx = tmpx + x
        tmpy = tmpy + y
    
    mediax = tmpx/len(dados)
    mediay = tmpy/len(dados)
    a = 0
    b = 0

    for i in range(1,len(dados)):
        x = dados[i, 0]
        y = dados[i, 1]
        a = a + (x-mediax)*(y-mediay)
        b =  b+ (x-mediax)**2
    w1 = a/b
    w0 = mediay-w1*mediax

    print("w0 = {0}, w1 = {1}".format(w0,w1))
    print("De fato, muito mais rápido!")

if __name__ == '__main__':
    run()

#!/usr/bin/envetor python
# -*- coding: UTF-8 -*-


def media(vetor):
    return sum(vetor) / len(vetor)


def moda(vetor):
    b, modas = 2, []
    for i in vetor:
        a = vetor.count(i)
        if a > b:
            b, modas = a, [i]
        elif a == b and i not in modas:
            modas.append(i)
    modas.sort()
    return modas


def mediana(vetor):
    vetor.sort()
    if len(vetor) % 2 == 0:
        return media([vetor[int(len(vetor) / 2) - 1], vetor[int(len(vetor) / 2)]])
    else:
        return vetor[int(len(vetor) / 2)]


def desvio_medio(vetor):
    return media([abs(i - media(vetor)) for i in vetor])


def variancia(vetor):
    return media([pow(i - media(vetor), 2) for i in vetor])


def desvio_padrao(vetor):
    return pow(variancia(vetor), .5)


if __name__ == "__main__":

    executa = True
    
    while (executa):
        entrada = int(input("Insira a quantidade de valores da amostra: "))
        vetor = list(map(int,input("Insira os valores: ").strip().split()))[:entrada]


        if(len(vetor) >= entrada):
            executa = False


    print("MEDIA: ")
    print(media(vetor))
    print(" ")

    print("MODA: ")
    print(moda(vetor))
    print(" ")

    print("MEDIANA: ")
    print(mediana(vetor))
    print(" ")

    print("Medidas de Dispersão\n")
	
    print("DESVIO MEDIO: ")
    print(desvio_medio(vetor))
    print(" ")

    print("VARIANCIA: ")
    print(variancia(vetor))
    print(" ")

    print("DESVIO PADRAO: ")
    print(desvio_padrao(vetor))
    print(" ")

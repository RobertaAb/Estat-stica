# Estat-stica

import pandas as pd
import math

print ( " Bem vindo ao app de cálculos estatísticos! \ n Por favor, coloque sua base de dados (.csv) na massa dessa aplicação " )
x =  input ( " Insista do nome do arquivo: " )
lista = pd.read_csv ( str (x) +  ' .csv ' ) # Realiza uma leitura do arquivo com os dados do usuário.

# Realiza o cálculo da média aritimética dos dados inseridos pelo usuário
def  media_arit ( lista ):
    para x na lista:
        soma + = x
    resposta = soma /  len (lista)
     rodada de retorno (resposta, 2 )

# Realiza o cálculo da média ponderada dos dados inseridos pelo usuário
def  media_pond ( lista , pesos ):
    medias =  zip (lista, pesos)
    medias_pond = []
    para x, y em mídias:
        medias_pond.append (x * y)
    para x em medias_pond:
        soma + = x
        resposta = soma /  len (lista)
     rodada de retorno (resposta, 2 )

# Realiza o cálculo da média geométrica dos dados inseridos pelo usuário
def  media_geo ( lista ):
    para x na lista:
        mult * = x
    resposta = mult ** ( 1  /  len (lista))
     rodada de retorno (resposta, 2 )

# Realiza o cálculo da amplitude de classe dos dados inseridos pelo usuário
def  amplitude_class ( lista ):
    lista.sort ()
    n =  len (lista)
    k = sqrt (n)
    ac = (lista [ - 1 ] - lista [ 0 ]) / k
    volta de  volta (ac, 2 )

# Realiza o cálculo da variância da amostra dos dados inseridos pelo usuário
def  variancia_amos ( lista ):
    para eu na lista:
        soma + = (i - media_arit (lista)) **  2
    resposta = (soma / ( len (lista) -  1 )) **  2
     rodada de retorno (resposta, 2 )

# Realiza o cálculo da variância populacional dos dados inseridos pelo usuário
def  variancia_pop ( lista ):
    para eu na lista:
        soma + = (i - media_arit (lista)) **  2
    resposta = (soma /  len (lista)) **  2
     rodada de retorno (resposta, 2 )

# Realiza o cálculo do desvio padrao dos dados inseridos pelo usuário
def  desv_padrao_amos ( lista ):
    retornar sqrt (variancia_amos)

# Realiza o cálculo do desvio padrao populacional dos dados inseridos pelo usuário
def  desv_padrao_pop ( lista ):
    retornar sqrt (variancia_pop)

# Realiza o cálculo do grau de confiança de uma determinada amostra dos dados inseridos pelo usuário
def  grau_confianca ( lista ):
    z =  input ( " Inserir o nivel de confianca desejado: " )
    e =  input ( " Inserir uma margem e erro intiabável: " )
    n = ((z * desv_padrao_pop (lista)) / e) **  2
    volta de  volta (n, 2 )

# Realiza o cálculo do coeficiente de seleção dos dados inseridos pelo usuário
def  coef_variacao ( lista ):
    return des_padrao_amos / media_arit

# Realiza o cálculo da mediana dos dados inseridos pelo usuário
def  mediana ( lista ):
    lista.sort ()
    k = ( len (lista) //  2 )
    if ( len (lista) %  2  ! =  0 ):
        return lista [k]
    else :
        a = lista [ - k]
        b = lista [k]
        resultado = (a + b) /  2
        volta em  volta (resultado, 2 )

# Realiza o cálculo do tamanho de uma amostra confiável dos dados inseridos pelo usuário
def  tamanho_amostra ( lista ):
    n =  len (lista)
    return  = (n * grau_confianca (lista)) / (n + grau_confianca (lista))

# Realização do cálculo da distribuição de frequência (regra da raiz quadrada) dos dados inseridos pelo usuário
def  distri_freq ( lista ):
    retornar sqrt ( len (lista))

# Monta uma tabela de frequencia absoluta dos dados inseridos pelo usuário
def  freq_absoluta ( lista ):
    lista.sort ()
    tabela = [] []
    para eu na lista:
        para y na lista:
            if (i == y):
                soma + =  1
        tabela.append (i, soma)
        soma =  0
    imprimir (tabela)

# Monta uma tabela de frequencia acumulada dos dados inseridos pelo usuário
def  freq_acumulada ( lista ):
    lista.sort ()
    tabela = [] []
    para eu na lista:
        para y na lista:
            if (i == y):
                soma + =  1
        tabela.append (i, soma)
    imprimir (tabela)

# Monta uma tabela de frequencia relativa dos dados inseridos pelo usuário
def  freq_relativa ( lista ):
    lista.sort ()
    tabela = [] []
    para eu na lista:
        para y na lista:
            if (i == y):
                soma + =  1
        porcentagem = (soma *  100 ) /  len (lista)
        tabela.append (i, porcentagem)
        soma =  0
    imprimir (tabela)

# Monta uma tabela de frequencia relativa acumulada dos dados inseridos pelo usuário
def  freq_rel_acumulada ( lista ):
    lista.sort ()
    tabela = [] []
    para eu na lista:
        para y na lista:
            if (i == y):
                soma + =  1
                porcentagem = (soma *  100 ) /  len (lista)
        tabela.append (i, porcentagem)
    imprimir (tabela)

# -*- coding: utf-8 -*-
import random
import numpy as np
def Irodov():#Indice 0
    #matriz com o maior exercício de cada parte
    maximo=np.array([388,257,407,224,292,310])
    #escolha a parte
    parte=random.randrange(1,7)
    exercicio=random.randrange(1,maximo[parte-1]+1)
    return ("irodov parte "+str(parte)+" exercício "+str(parte)+"."+str(exercicio)+".")
def Goldman():#indice 1
    #Matriz com o maior exercício de cada parte(que me considero capaz hj)
    maximo=[42,17,64,60,21]
    #ecolha a parte e o exercício
    parte=random.randrange(1,6)
    exercicio=random.randrange(1,maximo[parte-1]+1)
    return "Goldman capítulo "+str(parte)+" exercício "+str(exercicio)
def NilsonRiedell():#indice 2
    #Matriz com o maior exercício de cada parte(que me considero capaz hj)
    maximo=[35,44,75,108]
    #escolha a parte e o exercício
    parte=random.randrange(1,5)
    exercicio=random.randrange(1,maximo[parte-1]+1)
    return "NilsonRiedell "+str(parte)+" exercício "+str(parte)+"."+str(exercicio)

    
def probabilidade(DistribuiçãoDequestões):
    #Quero que o que tem mais questões tenha peso 2 e o que tem menos questões peso 1 os outros livros com  peso intermediário baseado no número de questões
    #Encontrando os limites
    minimo=np.min(DistribuiçãoDequestões)
    maximo=np.max(DistribuiçãoDequestões)
    #Encontre os pesos
    pesos=(DistribuiçãoDequestões-minimo)/(maximo-minimo)+1
    #Encontre a probabilidade
    return pesos/np.sum(pesos)

def livroResultante():
    #Consegue a probabilidade de cada livro
    prob=probabilidade(np.array([388+257+407+224+292+310,42+17+64+60+21,35+44+75+108]))
    #Escolhe o livro:
    dado=random.random()
    if dado<prob[0]:
        return Irodov()
    dado-=prob[0]
    if dado<prob[1]:
        return Goldman()
    dado-=prob[1]
    if dado<prob[2]:
        return NilsonRiedell()
    dado-=prob[2]
    return "error"






# coding: utf-8
import numpy as np
def iniciarFiles():
    nameFile = open(".spacedRepetition/data/challenges/names.txt","a",encoding="utf-8")
    nameFile.close()
    subdivisionsFile= open(".spacedRepetition/data/challenges/subdivisions.txt","a",encoding="utf-8")
    subdivisionsFile.close()
    problemFile = open(".spacedRepetition/data/challenges/problems.txt","a",encoding="utf-8")
    problemFile.close()
def checkChallenges(materials):
    for material in materials:
    #verifies if there are as many sections as exercises per section
        if len(material["subdivisions"])!=len(material["exercises"]):
            return False
    return True
def integerStringCheck(checkedString:str):
    try:
        int(checkedString)
    except:
        return False
    return True
def saveChallenges(materials):
    if not checkChallenges(mateials):
        return False
    #write the names
    nameFile = open(".spacedRepetition/data/challenges/names.txt","w",encoding="utf-8")
    for index in range(len(materials)):
        nameFile.write(materials[index]["name"])
        if index+1<len(materials):
            nameFile.write("\n")
    nameFile.close()
    #write the subdivisions
    subdivisionsFile= open(".spacedRepetition/data/challenges/subdivisions.txt","a",encoding="utf-8")
    for index in range(len(materials)):
        subdivisionsPH=""
        for indexPrime in range(len(materials[index]["subdivisions"])):
            subdivisionsPH+=materials[index]["subdivision"][indexPrime]
            if indexPrime+1<len(materials[index]["subdivisios"]):
                subdivisionsPH+="@"
        subdivisionFile.write(subdivisionsPH)
        if index+1<len(materials):
            subdivisionFile.write("\n")
    subdivisionFile.close()
    #Write the number of problem
    problemFile = open(".spacedRepetition/data/challenges/problems.txt","a",encoding="utf-8")
    for index in range(len(materials)):
        problem=""
        for indexPrime in range(len(materials[index]["exercise"])):
            probllemPH+=str(materials[index]["exercise"][indexPrime])
            if indexPrime+1<len(materials[index]["exercise"]):
                problemPH+=" "
        problemFile.write(problemPH)
        if index+1<len(materials):
            problemFile.write("\n")
    problemFile.close()
    return False

def ConseguirDesafios():
    try:
        #Consegue os Nomes
        fileNomesDosDesafios = open(".NomesDosDesafios.txt","r",encoding="utf-8")
        nomesPH=fileNomesDosDesafios.read().split("\n")
        fileNomesDosDesafios.close()
        #Consegue as subdivisões
        fileSubdivisoes = open(".DesafiosSubdivisoes.txt","r",encoding="utf-8")
        subdivisoesPH=fileSubdivisoes.read().split("\n")
        for index in range(len(subdivisoesPH)):
            subdivisoesPH[index]=subdivisoesPH[index].split("@")
        fileSubdivisoes.close()
        #Consegue o número de exercícios
        fileExercicios = open(".DesafiosExercicios.txt","r",encoding="utf-8")
        exerciciosPH=fileExercicios.read().split("\n")
        for index in range(len(exerciciosPH)):
            exerciciosPH[index]=exerciciosPH[index].split(" ")
            for indexPrime in range(len(exerciciosPH[index])):
                exerciciosPH[index][indexPrime]=int(exerciciosPH[index][indexPrime])
        fileExercicios.close()
        #Concatena o dicionário
        materiais=[]
        for index in range(len(nomesPH)):
            materiais.append({
            "nome":nomesPH[index],
            "subdivisoes":subdivisoesPH[index],
            "exercicios":exerciciosPH[index]
        })
        return materiais
    except:
        #Caso a file estiver vazia retorne uma array vazia
        return[]


def probabilidade(materiais):
    #Encontrando a distribuição de questoes
    distribuicaoQuestoes=[]
    for index in range(len(materiais)):
        distribuicaoQuestoes.append(np.sum(np.array(materiais[index]["exercicios"])))
    distribuicaoQuestoes=np.array(distribuicaoQuestoes)
    print(distribuicaoQuestoes)
    #Retorne caso só houver menos de 1 exercício
    if len (distribuicaoQuestoes)==1:
        return np.array([1])
    elif len(distribuicaoQuestoes)==0:
        return np.array([0])
    #Quero que o que tem mais questões tenha peso 2 e o que tem menos questões peso 1 os outros livros com  peso intermediário baseado no número de questões
    #Encontrando os limites
    minimo=np.min(distribuicaoQuestoes)
    maximo=np.max(distribuicaoQuestoes)
    #Encontre os pesos
    pesos=(distribuicaoQuestoes-minimo)/(maximo-minimo)+1
    #Encontre a probabilidade
    return pesos/np.sum(pesos)
def verificarPresencaArrouba(texto:str):
    for character in texto:
        if character =="@":
            return True
    return False
def materiaisString(materiais):
    textoFinal=["materiais randomizados :"]
    for index in range(len(materiais)):
        textoPH=str(index)+"-"+materiais[index]["nome"]
        for indexPrime in range(len(materiais[index]["exercicios"])):
            textoPH+="\n  +"+materiais[index]["subdivisoes"][indexPrime]+"|"+str(materiais[index]["exercicios"][indexPrime])+" exercícios."
        textoFinal.append(textoPH)
    textoFinal.append("pronto")
    return textoFinal







iniciarFiles()
# coding: utf-8
import numpy as np
def iniciarFiles():
    nameFile = open("","a",encoding="utf-8")
    nameFile.close()
    fileSubdivisoes = open(".DesafiosSubdivisoes.txt","a",encoding="utf-8")
    fileSubdivisoes.close()
    fileExercicios = open(".DesafiosExercicios.txt","a",encoding="utf-8")
    fileExercicios.close()
def verificarSeValido(materiais):
    for material in materiais:
    #Verifica se há os mesmo número de seções e números de exercícios por seção
        if len(material["subdivisoes"])!=len(material["exercicios"]):
            return False
    return True
def checagemInteiraDeStrings(stringChecada:str):
    try:
        int(stringChecada)
    except:
        return False
    return True
    
            

def salvarDesafios(materiais):
    if not verificarSeValido(materiais):
        return False
    #Escreva os nomes
    fileNomesDosDesafios = open(".NomesDosDesafios.txt","w",encoding="utf-8")
    for index in range(len(materiais)):
        fileNomesDosDesafios.write(materiais[index]["nome"])
        if index+1<len(materiais):
            fileNomesDosDesafios.write("\n")
    fileNomesDosDesafios.close()
    #Escreva as subdivisões
    fileSubdivisoes = open(".DesafiosSubdivisoes.txt","w",encoding="utf-8")
    for index in range(len(materiais)):
        subdivisoesPH=""
        for indexPrime in range(len(materiais[index]["subdivisoes"])):
            subdivisoesPH+=materiais[index]["subdivisoes"][indexPrime]
            if indexPrime+1<len(materiais[index]["subdivisoes"]):
                subdivisoesPH+="@"
        fileSubdivisoes.write(subdivisoesPH)
        if index+1<len(materiais):
            fileSubdivisoes.write("\n")
    fileSubdivisoes.close()
    #Escreva o número de exercícios de cada subdivisão
    fileExercicios = open(".DesafiosExercicios.txt","w",encoding="utf-8")
    for index in range(len(materiais)):
        exerciciosPH=""
        for indexPrime in range(len(materiais[index]["exercicios"])):
            exerciciosPH+=str(materiais[index]["exercicios"][indexPrime])
            if indexPrime+1<len(materiais[index]["exercicios"]):
                exerciciosPH+=" "
        fileExercicios.write(exerciciosPH)
        if index+1<len(materiais):
            fileExercicios.write("\n")
    fileExercicios.close()
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
# coding: utf-8
import time
import os

def initialiseFiles():
    #makes (or not) the data files
    fileEnunciadosNumericos = open(".spacedRepetition/data/NumericExercise","a",encoding="utf-8")
    fileDadosNumericos = open(".dadosNumericos.txt","a",encoding="utf-8")
    fileEnunciadosNumericos.close()
    fileDadosNumericos.close()
    fileEnunciadosTeoricos = open(".enunciadosTeoricos.txt","a",encoding="utf-8")
    fileDadosTeoricos= open(".dadosTeoricos.txt","a",encoding="utf-8")
    fileGabaritosTeoricos = open(".gabaritosTeoricos.txt","a",encoding="utf-8")
    fileEnunciadosTeoricos.close()
    fileDadosTeoricos.close()
    fileGabaritosTeoricos.close()
    fileAjuda = open("help.txt","a",encoding="utf-8")
    fileAjuda.close
def obterExerciciosNumericos():
    fileEnunciadosNumericos = open(".enunciadosNumericos.txt","r",encoding="utf-8")
    enunciados = fileEnunciadosNumericos.read()
    enunciados=enunciados.split("\n")
    fileEnunciadosNumericos.close()
    fileDadosNumericos =open(".dadosNumericos.txt","r",encoding="utf-8")
    dados=fileDadosNumericos.read()
    dados=dados.split("\n")
    for index in range(len(dados)):
        dados[index]=dados[index].split(" ")
    fileDadosNumericos.close()
    exerciciosNumericos=[]
    try:
        for index in range(len(enunciados)):
            exerciciosNumericos.append({
        "enunciado":enunciados[index],
        "caixa":int(dados[index][0]),
        "gabarito":float(dados[index][1]),
        "certeza":int(dados[index][2]),
        "ultimaAbertura":float(dados[index][3]),
        "erros":int(dados[index][4])
        })
        return exerciciosNumericos
    except:
        print("Arquivos:Erro ao obter exercícios numéricos.")
        return[]
def obterExerciciosTeoricos():
    fileEnunciadosTeoricos = open(".enunciadosTeoricos.txt","r",encoding="utf-8")
    enunciados = fileEnunciadosTeoricos.read()
    enunciados=enunciados.split("\n")
    fileEnunciadosTeoricos.close()
    fileGabaritosTeoricos =open(".gabaritosTeoricos.txt","r",encoding="utf-8")
    gabaritos=fileGabaritosTeoricos.read()
    gabaritos=gabaritos.split("\n")
    fileGabaritosTeoricos.close()
    fileDadosTeoricos =open(".dadosTeoricos.txt","r",encoding="utf-8")
    dados=fileDadosTeoricos.read()
    dados=dados.split("\n")
    for index in range(len(dados)):
        dados[index]= dados[index].split(" ")
    fileDadosTeoricos.close()
    exerciciosTeoricos=[]
    try:
        for index in range(len(enunciados)):
            exerciciosTeoricos.append({
            "enunciado":enunciados[index],
            "caixa":int(dados[index][0]),
            "gabarito":gabaritos[index],
            "ultimaAbertura":float(dados[index][1]),
            "erros":int(dados[index][2])
        })
        return exerciciosTeoricos
    except:
        print("Arquivos:Erro ao obter exercícios teóricos.")
        return[]

def salvarExerciciosNumericos(exerciciosNumericos):
    fileEnunciadosNumericos = open(".enunciadosNumericos.txt","w",encoding="utf-8")
    fileDadosNumericos = open(".dadosNumericos.txt","w",encoding="utf-8")
    for index in range(len(exerciciosNumericos)):
        exercise= exerciciosNumericos[index]
        fileEnunciadosNumericos.write( exercise["enunciado"])
        fileDadosNumericos.write(str(exercise["caixa"])+" "+str(exercise["gabarito"])+" " + str(exercise["certeza"])+" "+str(exercise["ultimaAbertura"])+ " "+ str(exercise["erros"]))
        if(index+1<len(exerciciosNumericos)):
            fileEnunciadosNumericos.write("\n")
            fileDadosNumericos.write("\n")
    fileEnunciadosNumericos.close()
    fileDadosNumericos.close()
def salvarExerciciosTeoricos(exerciciosAAdicionar):
    fileEnunciadosTeoricos = open(".enunciadosTeoricos.txt","w",encoding="utf-8")
    fileDadosTeoricos = open(".dadosTeoricos.txt","w",encoding="utf-8")
    fileGabaritoTeoricos=open(".gabaritosTeoricos.txt","w",encoding="utf-8")
    for index in range(len(exerciciosAAdicionar)):
        fileEnunciadosTeoricos.write( exerciciosAAdicionar[index]["enunciado"])
        fileDadosTeoricos.write(str(exerciciosAAdicionar[index]["caixa"])+" "+str(exerciciosAAdicionar[index]["ultimaAbertura"])+ " "+ str(exerciciosAAdicionar[index]["erros"]))
        fileGabaritoTeoricos.write(exerciciosAAdicionar[index]["gabarito"])
        if(index+1<len(exerciciosAAdicionar)):
            fileEnunciadosTeoricos.write("\n")
            fileDadosTeoricos.write("\n")
            fileGabaritoTeoricos.write("\n")
    fileDadosTeoricos.close()
    fileDadosTeoricos.close()

def adicionarExercicioNumerico(enunciado,gabarito,certeza,exerciciosAtuais):
    exerciciosAtuais.append({
        "enunciado":enunciado,
        "caixa":0,
        "gabarito":float(gabarito),
        "certeza":int(certeza),
        "ultimaAbertura":int(time.time()),
        "erros":0
        })
    salvarExerciciosNumericos(exerciciosAtuais)
def deletarExercicioNumericos(index,exerciciosAtuais):
    exerciciosAtuais.pop(index)
    salvarExerciciosNumericos(exerciciosAtuais)
    return exerciciosAtuais
def adicionarExercicioTeorico(enunciado,gabarito,exerciciosAtuais):
    exerciciosAtuais.append({
        "enunciado":enunciado,
        "caixa":0,
        "gabarito":gabarito,
        "ultimaAbertura":int(time.time()),
        "erros":0
        })
    salvarExerciciosTeoricos(exerciciosAtuais)
def deletarExercicioTeorico(index,exerciciosAtuais):
    exerciciosAtuais.pop(index)
    salvarExerciciosTeoricos(exerciciosAtuais)
    return exerciciosAtuais
def listarExercicios():
    exerciciosNumericos=obterExerciciosNumericos()
    exerciciosTeoricos=obterExerciciosTeoricos()
    exerciciosListados=["Exercícios Numéricos:"]
    for index in range(len(exerciciosNumericos)):
        exercise=exerciciosNumericos[index]
        exerciciosListados.append(str(index)+"-"+exercise["enunciado"]+"-caixa:"+str(exercise["caixa"])+"-erros:"+str(exercise["erros"]))
    exerciciosListados.append("Exercícios teóricos:")
    for index in range(len(exerciciosTeoricos)):
        exercise=exerciciosTeoricos[index]
        exerciciosListados.append(str(index)+"-"+exercise["enunciado"]+"-caixa:"+str(exercise["caixa"])+"-erros:"+str(exercise["erros"]))
    exerciciosListados.append("finalizado")
    return exerciciosListados
def listarExerciciosIncompletos():
    exerciciosNumericos=obterExerciciosNumericos()
    exerciciosTeoricos=obterExerciciosTeoricos()
    exerciciosListados=["Exercícios Numéricos:"]
    contador=0
    for index in range(len(exerciciosNumericos)):
        exercise=exerciciosNumericos[index]
        if exercise["caixa"]<4:
            exerciciosListados.append(str(index)+"-"+exercise["enunciado"]+"-caixa:"+str(exercise["caixa"])+"-erros:"+str(exercise["erros"]))
            contador+=1
    exerciciosListados.append("Exercícios teóricos:")
    for index in range(len(exerciciosTeoricos)):
        exercise=exerciciosTeoricos[index]
        if exercise["caixa"]<4:
            exerciciosListados.append(str(index)+"-"+exercise["enunciado"]+"-caixa:"+str(exercise["caixa"])+"-erros:"+str(exercise["erros"]))
            contador+=1
    exerciciosListados.append("finalizado:"+str(contador)+"exercícios incompletos")
    return exerciciosListados
def conseguirAjuda():
    #Leia o que está escrito em ajuda.txt
    fileAjuda=open("help.txt","r",encoding="utf-8")
    textoDeAjuda=fileAjuda.read()
    fileAjuda.close()
    return textoDeAjuda
initialiseFiles()

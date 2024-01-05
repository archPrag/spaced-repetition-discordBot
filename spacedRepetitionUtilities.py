# coding: utf-8

def checagemInteiraDeStrings(stringNumerica:str):
    try:
        int(stringNumerica)
        return True
    except:
        return False
def checagemFlutuanteDeStrings(stringNumerica:str):
    try:
        float(stringNumerica)
        return True
    except:
        return False
def diferencaEmDias(tempoinicial,tempofinal):
    tempoinicial=int((tempoinicial-10800)/86400)
    tempofinal=int((tempofinal-10800)/86400)
    return abs(tempofinal-tempoinicial)
def compararValores(valorCerto,valorDuvidoso,algarismosSignoficativos):
    if valorCerto==0:
        return abs(valorDuvidoso)<=10*0.1**algarismosSignoficativos
    elif abs(valorCerto)>=10:
        return compararValores(valorCerto/10,valorDuvidoso/10,algarismosSignoficativos)
    elif abs(valorCerto)<1:
        return compararValores(valorCerto*10,valorDuvidoso*10,algarismosSignoficativos)
    else:
        return abs(valorCerto-valorDuvidoso)<=10*0.1**algarismosSignoficativos
def algarismosSignificativosEmString(stringNumerica:str):
    #verifique se é de fato numérica
    if not checagemFlutuanteDeStrings(stringNumerica):
        return 0
    #retorne o número de algarismos significativos
    stringNumerica.split(".")
    if len(stringNumerica)==1:
        return len(stringNumerica[0])
    else:
        return len(stringNumerica[0])+len(stringNumerica[1])

def erroPercentual(correto:float,errado:float):
    return str(100*(correto-errado))+"%"

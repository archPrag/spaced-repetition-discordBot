# coding: utf-8
import numpy as np

def integerStringCheck(numericString:str):
    try:
        int(numericString)
        return True
    except:
        return False
def floatStringCheck(numericString:str):
    try:
        float(numericString)
        return True
    except:
        return False
def dayDifference(initialTime,finalTime):
    #Using Brazil-Sao_Paulo Timezone
    initialTime=int((initialTime-10800)/86400)
    finalTime=int((finalTime-10800)/86400)
    return abs(finalTime-initialTime)
def compareValues(correct,dubious,significantFigures):
    if correct==0:
        return abs(dubious)<=10*0.1**significantFigures
    elif abs(correct)>=10:
        return compareValues(correct/10,dubious/10,significantFigures)
    elif abs(correct)<1:
        return compareValues(correct*10,dubious*10,significantFigures)
    else:
        return abs(correct-dubious)<=10*0.1**significantFigures
def stringSignificantFigures(numericString:str):
    #verify if the string is numeric
    if not floatStringCheck(numericString):
        return 0
    #return the significant figure numbers
    numericString.split(".")
    if len(numericString)==1:
        return len(numericString[0])
    else:
        return len(numericString[0])+len(numericString[1])

def percentualDeviation(right:float,wrong:float):
    return str(100*(right-wrong))+"%"

import numpy as np
timeZone=-3
def integerStringCheck(numStr):
    try:
        int(numStr)
        return True
    except:
        return False
def dayDifference(begining,ending):
    global timeZone
    beginingTZ=begining-timeZone*3600
    endingTZ=ending-timeZone*3600
    return int((endingTZ-beginingTZ)/24.0/3600.0)
def timeZoneCompare(unixTime,hour24F,minutes):
    Difference=unixTime
    while(Difference-24*3600>0):
        Difference-=24*3600
    Difference=hour24F*3600+minutes*60-Difference
    return(int(Difference/3600.0))
def floatStringCheck(numStr):
    try:
        float(numStr)
        return True
    except:
        return False
def stringSignificantFigures(numStr:str):
    if float(numStr)==0:
        return len(numStr)-1
    if numStr.startswith("0"):
        return stringSignificantFigures(numStr[0:])
    if numStr.startswith(".0"):
        return stringSignificantFigures(numStr[1:])
    if numStr.startswith("."):
        return len(numStr)-1
    if integerStringCheck(numStr):
        return(len(numStr))
    return(len(numStr)-1)
def compareValues(correct,given,significantFigures):
    if correct==0:
        return abs(given)<10**(1-significantFigures)
    if abs(correct)<1:
        return compareValues(correct*10,given*10,significantFigures)
    if abs(correct)>=10:
        return compareValues(correct/10.0,given/10.0,significantFigures)
    return abs(correct-given)<10**(1-significantFigures)


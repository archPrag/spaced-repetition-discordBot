# coding: utf-8
import json
import os
import time
import utilities


def basicFiles():
    print("initialyzer: trying to create directories")
    try:
        os.mkdir(".spacedRepetition")
    except:
        print("initialyzer:.spacedRepetition already there")
    try:
        os.mkdir(".spacedRepetition/adminData")
    except:
        print("initialyzer:adminData already there")
    file = open(".spacedRepetition/adminData/userStates.json", "a", encoding="utf-8")
    file.close()
    file = open(".spacedRepetition/adminData/userVars.json", "a", encoding="utf-8")
    file.close()
def getMaterials(userName):
    file=open(".spacedRepetition/" + userName + "_materials_.json", "r", encoding="utf-8")
    materialString=file.read()
    file.close()
    return json.loads(materialString)
def saveMaterials(materials,userName):
    file=open(".spacedRepetition/" + userName + "_materials_.json", "w", encoding="utf-8")
    materialString=json.dumps(materials)
    file.write(materialString)
    file.close()
def addMaterial(name,chapterNames,exercisePerChapter,userName):
    materials=getMaterials(userName)
    materials.append({
        "name":name,
        "chapterNames":chapterNames,
        "exercisePerChapter":exercisePerChapter,
        "lastOpened":[]
    })
    for exercise in exercisePerChapter:
        materials[-1]["lastOpened"].append(time.time())
    saveMaterials(materials,userName)
def deleteMaterials(materialName,userName):
    materials=getMaterials(userName)
    for ind in range(len(materials)):
        if materials[ind]["name"]==materialName:
            materials.pop(ind)
            saveMaterials(materials,userName)
            return
def materialExists(materialName,userName):
    materials=getMaterials(userName)
    for index in range(len(materials)):
        if materials[index]["name"]==materialName:
            return True
    return False
def listMaterials(userName):
    materials=getMaterials(userName)
    currentTime=time.time()
    messagesToSend=["***materials:"]
    messagePH=""
    for index in range(len(materials)):
        messagePH="---"+materials[index]["name"]+"\n"
        for chapter in range(len(materials)):
            messagePH+="-*"+materials[index]["chapterNames"][chapter]
            messagePH+="@"+str(materials[index]["exercisePerChapter"][chapter])+"problems"
            messagePH+="@"+str(utilities.dayDifference(materials[index]["lastOpened"][chapter],currentTime))+"days"
            messagePH+="\n"
        messagesToSend.append(messagePH)
    return messagesToSend
def getProblems(userName):
    file=open(".spacedRepetition/" + userName + ".json", "r", encoding="utf-8")
    problems = file.read()
    file.close()
    return json.loads(problems)

def saveProblems(problems, userName):
    jsonString = json.dumps(problems, indent=4)
    file=open(".spacedRepetition/" + userName + ".json", "w", encoding="utf-8")
    file.write(jsonString)
    file.close()
def addNumericProblem(question, answer, significantFigure, problems, userName):
    problems["numeric"].append(
        {
            "question": question,
            "box": 0,
            "answer": float(answer),
            "significantFigures": int(significantFigure),
            "lastOpened": int(time.time()),
            "errors": 0,
        }
    )
    saveProblems(problems, userName)


def deleteNumericProblem(index, problems, userName):
    problems["numeric"].pop(index)
    saveProblems(problems, userName)


def addTheoreticalProblem(question, answer, problems, userName):
    problems["theoretical"].append(
        {
            "question": question,
            "box": 0,
            "answer": answer,
            "lastOpened": int(time.time()),
            "errors": 0,
        }
    )
    saveProblems(problems, userName)


def deleteTheoreticalExercise(index, problems, userName):
    problems["theoretical"].pop(index)
    saveProblems(problems, userName)


def listProblems(userName):
    problems = getProblems(userName)
    listOfProblems = ["Numeric problems:"]
    for index in range(len(problems["numeric"])):
        problem = problems["numeric"][index]
        listOfProblems.append(
            +problem["question"]
            + "-box:"
            + str(problem["box"])
            + "-errors:"
            + str(problem["errors"])
        )
    listOfProblems.append("Theoretical problems:")
    for index in range(len(problems["theoretical"])):
        problem = problems["theoretical"][index]
        listOfProblems.append(
            str(index)
            + "-"
            + problem["question"]
            + "-box:"
            + str(problem["box"])
            + "-errors:"
            + str(problem["errors"])
        )
    listOfProblems.append("All problems have been listed.")
    return listOfProblems


def listUnfinishedProblems(userName):
    problems = getProblems(userName)
    listOfProblems = ["Numeric problems:"]
    counter = 0
    for index in range(len(problems["numeric"])):
        problem = problems["numeric"][index]
        if problem["box"] < 4:
            listOfProblems.append(
                str(index)
                + "-"
                + problem["question"]
                + "-box:"
                + str(problem["box"])
                + "-errors:"
                + str(problem["errors"])
            )
            counter += 1
    listOfProblems.append("Theoretical problems:")
    for index in range(len(problems["theoretical"])):
        problem = problems["theoretical"][index]
        if problem["box"] < 4:
            listOfProblems.append(
                str(index)
                + "-"
                + problem["question"]
                + "-caixa:"
                + str(problem["box"])
                + "-erros:"
                + str(problem["errors"])
            )
            counter += 1
    listOfProblems.append(
        "All problems have been listed.-" + str(counter) + " unfinished problems."
    )
    return listOfProblems


def getHelp():
    helpFile = open("help.txt", "r", encoding="utf-8")
    helpText = helpFile.read()
    helpFile.close()
    return helpText


def getUserState(userName):
    file=open(".spacedRepetition/adminData/userStates.json", "r", encoding="utf-8")
    states = json.loads(file.read())
    file.close()
    return states[userName]
def getUserVars(userName):
    file=open(".spacedRepetition/adminData/userVars.json", "r", encoding="utf-8")
    vars = json.loads(file.read())
    file.close()
    return vars[userName]
def setUserState(state, userName):
    file=open(".spacedRepetition/adminData/userStates.json", "r", encoding="utf-8")
    states = json.loads(file.read())
    states[userName] = state
    jsonString = json.dumps(states, indent=4)
    file.close
    file=open( ".spacedRepetition/adminData/userStates.json", "w", encoding="utf-8")
    file.write(jsonString)
    file.close()
def setUserVars(variables, userName):
    file=open( ".spacedRepetition/adminData/userVars.json", "r", encoding="utf-8")
    vars = json.loads(file.read())
    vars[userName] = variables
    jsonString = json.dumps(vars, indent=4)
    file.close
    file=open( ".spacedRepetition/adminData/userVars.json", "w", encoding="utf-8")
    file.write(jsonString)
    file.close()
def addUser(userName):
    file = open(".spacedRepetition/" + userName + ".json", "w", encoding="utf-8")
    jsonString=json.dumps({'theoretical':[],'numeric':[]})
    file.write(jsonString)
    file.close()
    file=open(".spacedRepetition/" + userName + "_materials_.json", "w", encoding="utf-8")
    jsonString=json.dumps([])
    file.write(jsonString)
    file.close()
    file=open( ".spacedRepetition/adminData/userStates.json", "r", encoding="utf-8") 
    states = json.loads(file.read())
    states[userName] = {"mode": "normal"}
    jsonString = json.dumps(states, indent=4)
    file.close()
    file=open( ".spacedRepetition/adminData/userStates.json", "w", encoding="utf-8")
    file.write(jsonString)
    file.close()
    file=open( ".spacedRepetition/adminData/userVars.json", "r", encoding="utf-8") 
    vars = json.loads(file.read())
    vars[userName]={"lastRandomized":0,"randomizedString":""}
    jsonString = json.dumps(vars, indent=4)
    file.close()
    file=open( ".spacedRepetition/adminData/userVars.json", "w", encoding="utf-8")
    file.write(jsonString)
    file.close()
def userExists(userName):
    file=open(".spacedRepetition/adminData/userStates.json",encoding='utf-8')
    jsonText=file.read()
    states = json.loads(jsonText)
    file.close()
    for name in states.keys():
        if name == userName:
            return True
    return False
basicFiles()

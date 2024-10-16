# coding: utf-8
import json
import os
import time
import utilities
import requests
import uuid
import shutil


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
    try:
        os.mkdir(".spacedRepetition/images")
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
        for chapter in range(len(materials[index]["chapterNames"])):
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

def addProblem(question, answer, problems,imagePath,userName):
    problems.append(
        {
            "image":imagePath,
            "question": question,
            "box": 0,
            "answer": answer,
            "lastOpened": int(time.time()),
            "errors": 0,
        }
    )
    saveProblems(problems, userName)


def deleteProblem(index, problems, userName):
    problems.pop(index)
    saveProblems(problems, userName)


def listProblems(userName):
    problems = getProblems(userName)
    listOfProblems=[]
    listOfProblems.append("Problems:")
    for index in range(len(problems)):
        problem = problems[index]
        listOfProblems.append(
            str(index)
            + "-"
            + problem["question"]
            + "-box:"
            + str(problem["box"])
            + "-errors:"
            + str(problem["errors"])
        )
        images.append(problems["image"])
    listOfProblems.append("All problems have been listed.")
    return {"messages":listOfProblems,"images":images}


def listUnfinishedProblems(userName):
    problems = getProblems(userName)
    listOfProblems=[]
    images=[]
    counter=0
    listOfProblems.append("Problems:")
    for index in range(len(problems)):
        problem = problems[index]
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
            images.append(problems["image"])
            counter += 1
    listOfProblems.append(
        "All problems have been listed.-" + str(counter) + " unfinished problems."
    )
    return {"messages":listOfProblems,"images":images}


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
    jsonString=json.dumps([])
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
def saveImg(url,userName):
    r=requests.get(url,stream=True)
    path="./.spacedRepetition/images/"+userName+str(uuid.uuid4())+".jpg"
    with open(path,'wb') as outFile:
        print("image gotten")
        shutil.copyfileobj(r.raw,outFile)
    return path
basicFiles()

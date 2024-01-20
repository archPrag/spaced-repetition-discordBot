# coding: utf-8
import json
import os
import time


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


def getProblems(userName):
    with open(".spacedRepetition/" + userName + ".json", "r", encoding="utf-8") as file:
        problems = file.read()
    return json.loads(problems)



def saveProblems(problems, userName):
    jsonString = json.dump(problems, indent=4)
    with open(".spacedRepetition/" + userName + ".json", "w", encoding="utf-8") as file:
        file.write(jsonString)


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
    saveProblems(exerciciosAtuais, userName)


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
    with open(
        ".spacedRepetition/adminData/userStates.json", "r", encoding="utf-8"
    ) as file:
        states = file.read()
    return states[userName]


def setUserState(state, userName):
    with open(
        ".spacedRepetition/adminData/userStates.json", "r", encoding="utf-8"
    ) as file:
        states = json.load(file.read())

    states[userName] = state
    jsonString = json.dump(states, indent=4)
    with open(
        ".spacedRepetition/adminData/userStates.json", "w", encoding="utf-8"
    ) as file:
        file.write(jsonString)
def addUser(userName):
    file = open(".spacedRepetition/"+userName+'.json', "a", encoding="utf-8")
    file.close()
    with open(
        ".spacedRepetition/adminData/userStates.json", "r", encoding="utf-8"
    ) as file:
        states = json.load(file.read())
    states[userName]={'mode':'normal'}
    jsonString = json.dump(states, indent=4)
    with open(
        ".spacedRepetition/adminData/userStates.json", "w", encoding="utf-8"
    ) as file:
        file.write(jsonString)
    


basicFiles()

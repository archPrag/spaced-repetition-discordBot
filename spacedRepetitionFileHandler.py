# coding: utf-8
import os
import time


def directories():
    print("initialyzer: trying to create directories")
    try:
        os.mkdir('.spacedRepetition')
    except:
        print("initialyzer:.spacedRepetition already there")

    try:
        os.mkdir('.spacedRepetition/data')
    except:
        print("initialyzer:.spacedRepetition/data already there")
def initialiseFiles():
    directories()
    # Ensures the existence of data files
    numericQuestionFile = open(
        ".spacedRepetition/data/numericQuestions", "a", encoding="utf-8"
    )
    numericDataFile = open(".spacedRepetition/data/numericData", "a", encoding="utf-8")
    numericQuestionFile.close()
    numericDataFile.close()
    theoreticalQuestionFile = open(
        ".spacedRepetition/data/teoricQuestions", "a", encoding="utf-8"
    )
    theoreticalDataFile = open(
        ".spacedRepetition/data/teoricData", "a", encoding="utf-8"
    )
    theoreticalAnswerFile = open(
        ".spacedRepetition/data/teoricAnswers", "a", encoding="utf-8"
    )
    theoreticalQuestionFile.close()
    theoreticalAnswerFile.close()
    theoreticalDataFile.close()


def getNumericProblems():
    # Get the questions
    numericQuestionFile = open(
        ".spacedRepetition/data/numericQuestions", "a", encoding="utf-8"
    )
    questions = numericQuestionFile.read()
    questions = questions.split("\n")
    numericQuestionFile.close()
    # Get the Data
    numericDataFile = open(".spacedRepetition/data/numericData", "a", encoding="utf-8")
    data = numericDataFile.read()
    data = data.split("\n")
    for index in range(len(data)):
        data[index] = data[index].split(" ")
    numericDataFile.close()
    # Merge everything
    numericProblems = []
    try:  # for dealing with the empty array problem
        for index in range(len(questions)):
            numericProblems.append(
                {
                    "question": questions[index],
                    "box": int(data[index][0]),
                    "answer": float(data[index][1]),
                    "significantFigures": int(data[index][2]),
                    "lastOpened": float(data[index][3]),
                    "errors": int(data[index][4]),
                }
            )
        return numericProblems
    except:
        print("Files: Empty numeric files")
        return []


def getTheoreticalProblems():
    # Get Questions
    theoreticalQuestionFile = open(
        ".spacedRepetition/data/teoricQuestions", "a", encoding="utf-8"
    )
    questions = theoreticalQuestionFile.read()
    questions = questions.split("\n")
    theoreticalQuestionFile.close()
    # Get Answers
    theoreticalAnswerFile = open(
        ".spacedRepetition/data/teoricAnswers", "a", encoding="utf-8"
    )
    answers = theoreticalAnswerFile.read()
    answers = answers.split("\n")
    theoreticalAnswerFile.close()
    theoreticalDataFile = open(
        ".spacedRepetition/data/teoricData", "a", encoding="utf-8"
    )
    data = theoreticalDataFile.read()
    data = data.split("\n")
    for index in range(len(data)):
        data[index] = data[index].split(" ")
    theoreticalDataFile.close()
    # merge into a dictionary
    theoreticalProblems = []
    try:
        for index in range(len(questions)):
            theoreticalProblems.append(
                {
                    "question": questions[index],
                    "box": int(data[index][0]),
                    "answer": answers[index],
                    "lastOpened": float(data[index][1]),
                    "error": int(data[index][2]),
                }
            )
        return theoreticalProblems
    except:
        print("Files: Empty numeric files")
        return []


def saveNumericProblems(problems):
    numericQuestionFile = open(
        ".spacedRepetition/data/numericQuestions", "w", encoding="utf-8"
    )
    numericDataFile = open(".spacedRepetition/data/numericData", "w", encoding="utf-8")
    # writes every information in its respective file
    for index in range(len(problems)):
        problem = problems[index]
        numericQuestionFile.write(problem["question"])
        numericDataFile.write(
            str(problem["box"])
            + " "
            + str(problem["answer"])
            + " "
            + str(problem["significantFigures"])
            + " "
            + str(problem["lastOpened"])
            + " "
            + str(problem["errors"])
        )
        if index + 1 < len(problems):
            numericQuestionFile.write("\n")
            numericQuestionFile.write("\n")
    numericQuestionFile.close()
    numericDataFile.close()


def saveTheoreticalProblems(problems):
    theoreticalQuestionFile = open(
        ".spacedRepetition/data/teoricQuestions", "w", encoding="utf-8"
    )
    theoreticalDataFile = open(
        ".spacedRepetition/data/teoricData", "w", encoding="utf-8"
    )
    theoreticalAnswerFile = open(
        ".spacedRepetition/data/teoricAnswers", "w", encoding="utf-8"
    )
    for index in range(len(problems)):
        theoreticalQuestionFile.write(problems[index]["question"])
        theoreticalDataFile.write(
            str(problems[index]["box"])
            + " "
            + str(problems[index]["lastOpened"])
            + " "
            + str(problems[index]["errors"])
        )
        theoreticalAnswerFile.write(problems[index]["answer"])
        if index + 1 < len(problems):
            theoreticalQuestionFile.write("\n")
            theoreticalDataFile.write("\n")
            theoreticalAnswerFile.write("\n")
    theoreticalAnswerFile.close()
    theoreticalQuestionFile.close()
    theoreticalDataFile.close()


def addNumericProblem(question, answer, significantFigure,problems):
    problems.append(
        {
            "question": question,
            "box": 0,
            "answer": float(answer),
            "significantFigures": int(significantFigure),
            "ultimaAbertura": int(time.time()),
            "erros": 0,
        }
    )
    saveNumericProblems(problems)


def deleteNumericProblem(index, problems):
    problems.pop(index)
    saveNumericProblems(problems)
    return problems


def addTheoreticalcProblem(question, answer, problems):
    problems.append(
        {
            "question": question,
            "box": 0,
            "answer": answer,
            "lastOpened": int(time.time()),
            "errors": 0,
        }
    )
    saveTheoreticalProblem(problems)


def deleteTheoreticalExercise(index, exerciciosAtuais):
    exerciciosAtuais.pop(index)
    saveTheoreticalProblem(exerciciosAtuais)
    return exerciciosAtuais


def listProblems():
    numericProblems = getNumericProblems()
    theoreticalProblems = getTheoreticalProblems()
    listProblems = ["Numeric problems:"]
    for index in range(len(numericProblems)):
        problem = numericProblems[index]
        listProblems.append(
            str(index)
            + "-"
            + problem["question"]
            + "-box:"
            + str(problem["box"])
            + "-errors:"
            + str(problem["errors"])
        )
    listProblems.append("Theoretical problems:")
    for index in range(len(theoreticalProblems)):
        exercise = theoreticalProblems[index]
        listProblems.append(
            str(index)
            + "-"
            + exercise["question"]
            + "-box:"
            + str(exercise["box"])
            + "-errors:"
            + str(exercise["errors"])
        )
    listProblems.append("All problems have been listed.")
    return listProblems


def listUnfinishedProblems():
    numericProblems = getNumericProblems()
    theoreticalProblems = getTheoreticalProblems()
    listProblems = ["Numeric problems:"]
    counter = 0
    for index in range(len(numericProblems)):
        problem = numericProblems[index]
        if problem["box"] < 4:
            listProblems.append(
                str(index)
                + "-"
                + problem["question"]
                + "-box:"
                + str(problem["box"])
                + "-errors:"
                + str(problem["errors"])
            )
            counter += 1
    listProblems.append("Theoretical problems:")
    for index in range(len(theoreticalProblems)):
        problem = theoreticalProblems[index]
        if problem["box"] < 4:
            listProblems.append(
                str(index)
                + "-"
                + problem["question"]
                + "-caixa:"
                + str(problem["box"])
                + "-erros:"
                + str(problem["errors"])
            )
            counter += 1
    listProblems.append("All problems have been listed.-" + str(counter) + " unfinished problems.")
    return listProblems


def getHelp():
    # Leia o que está escrito em ajuda.txt
    helpFile = open("help.txt", "r", encoding="utf-8")
    helpText = helpFile.read()
    helpFile.close()
    return helpText


initialiseFiles()

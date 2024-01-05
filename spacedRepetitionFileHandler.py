# coding: utf-8
import os
import time


def initialiseFiles():
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
    helpFile = open("help.txt", "a", encoding="utf-8")
    helpFile.close


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


def saveTheoreticalExercise(problems):
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


def adicionarExercicioNumerico(enunciado, gabarito, certeza, exerciciosAtuais):
    exerciciosAtuais.append(
        {
            "enunciado": enunciado,
            "caixa": 0,
            "gabarito": float(gabarito),
            "certeza": int(certeza),
            "ultimaAbertura": int(time.time()),
            "erros": 0,
        }
    )
    salvarExerciciosNumericos(exerciciosAtuais)


def deletarExercicioNumericos(index, exerciciosAtuais):
    exerciciosAtuais.pop(index)
    salvarExerciciosNumericos(exerciciosAtuais)
    return exerciciosAtuais


def adicionarExercicioTeorico(enunciado, gabarito, exerciciosAtuais):
    exerciciosAtuais.append(
        {
            "enunciado": enunciado,
            "caixa": 0,
            "gabarito": gabarito,
            "ultimaAbertura": int(time.time()),
            "erros": 0,
        }
    )
    salvarExerciciosTeoricos(exerciciosAtuais)


def deletarExercicioTeorico(index, exerciciosAtuais):
    exerciciosAtuais.pop(index)
    salvarExerciciosTeoricos(exerciciosAtuais)
    return exerciciosAtuais


def listarExercicios():
    exerciciosNumericos = obterExerciciosNumericos()
    exerciciosTeoricos = obterExerciciosTeoricos()
    exerciciosListados = ["Exercícios Numéricos:"]
    for index in range(len(exerciciosNumericos)):
        exercise = exerciciosNumericos[index]
        exerciciosListados.append(
            str(index)
            + "-"
            + exercise["enunciado"]
            + "-caixa:"
            + str(exercise["caixa"])
            + "-erros:"
            + str(exercise["erros"])
        )
    exerciciosListados.append("Exercícios teóricos:")
    for index in range(len(exerciciosTeoricos)):
        exercise = exerciciosTeoricos[index]
        exerciciosListados.append(
            str(index)
            + "-"
            + exercise["enunciado"]
            + "-caixa:"
            + str(exercise["caixa"])
            + "-erros:"
            + str(exercise["erros"])
        )
    exerciciosListados.append("finalizado")
    return exerciciosListados


def listarExerciciosIncompletos():
    exerciciosNumericos = obterExerciciosNumericos()
    exerciciosTeoricos = obterExerciciosTeoricos()
    exerciciosListados = ["Exercícios Numéricos:"]
    contador = 0
    for index in range(len(exerciciosNumericos)):
        exercise = exerciciosNumericos[index]
        if exercise["caixa"] < 4:
            exerciciosListados.append(
                str(index)
                + "-"
                + exercise["enunciado"]
                + "-caixa:"
                + str(exercise["caixa"])
                + "-erros:"
                + str(exercise["erros"])
            )
            contador += 1
    exerciciosListados.append("Exercícios teóricos:")
    for index in range(len(exerciciosTeoricos)):
        exercise = exerciciosTeoricos[index]
        if exercise["caixa"] < 4:
            exerciciosListados.append(
                str(index)
                + "-"
                + exercise["enunciado"]
                + "-caixa:"
                + str(exercise["caixa"])
                + "-erros:"
                + str(exercise["erros"])
            )
            contador += 1
    exerciciosListados.append("finalizado:" + str(contador) + "exercícios incompletos")
    return exerciciosListados


def conseguirAjuda():
    # Leia o que está escrito em ajuda.txt
    fileAjuda = open("help.txt", "r", encoding="utf-8")
    textoDeAjuda = fileAjuda.read()
    fileAjuda.close()
    return textoDeAjuda


initialiseFiles()

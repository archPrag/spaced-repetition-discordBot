# coding: utf-8
import numpy as np


def initializeFiles():
    nameFile = open(
        ".spacedRepetition/data/challenges/names.txt", "a", encoding="utf-8"
    )
    nameFile.close()
    subdivisionsFile = open(
        ".spacedRepetition/data/challenges/subdivisions.txt", "a", encoding="utf-8"
    )
    subdivisionsFile.close()
    problemFile = open(
        ".spacedRepetition/data/challenges/problems.txt", "a", encoding="utf-8"
    )
    problemFile.close()


def checkChallenges(materials):
    for material in materials:
        # verifies if there are as many sections as exercises per section
        if len(material["subdivisions"]) != len(material["exercises"]):
            return False
    return True


def integerStringCheck(checkedString: str):
    try:
        int(checkedString)
    except:
        return False
    return True


def saveChallenges(materials):
    if not checkChallenges(materials):
        return False
    # write the names
    nameFile = open(
        ".spacedRepetition/data/challenges/names.txt", "w", encoding="utf-8"
    )
    for index in range(len(materials)):
        nameFile.write(materials[index]["name"])
        if index + 1 < len(materials):
            nameFile.write("\n")
    nameFile.close()
    # write the subdivisions
    subdivisionsFile = open(
        ".spacedRepetition/data/challenges/subdivisions.txt", "a", encoding="utf-8"
    )
    for index in range(len(materials)):
        subdivisionsPH = ""
        for indexPrime in range(len(materials[index]["subdivisions"])):
            subdivisionsPH += materials[index]["subdivisions"][indexPrime]
            if indexPrime + 1 < len(materials[index]["subdivisions"]):
                subdivisionsPH += "@"
        subdivisionsFile.write(subdivisionsPH)
        if index + 1 < len(materials):
            subdivisionsFile.write("\n")
    subdivisionsFile.close()
    # Write the number of problem
    problemFile = open(
        ".spacedRepetition/data/challenges/problems.txt", "a", encoding="utf-8"
    )
    for index in range(len(materials)):
        problemPH = ""
        for indexPrime in range(len(materials[index]["problems"])):
            problemPH += str(materials[index]["problems"][indexPrime])
            if indexPrime + 1 < len(materials[index]["problems"]):
                problemPH += " "
        problemFile.write(problemPH)
        if index + 1 < len(materials):
            problemFile.write("\n")
    problemFile.close()
    return False


def ConseguirDesafios():
    try:
        # names
        nameFile = open(
            ".spacedRepetition/data/challenges/names.txt", "r", encoding="utf-8"
        )
        namesPH = nameFile.read().split("\n")
        nameFile.close()
        # subdivisions
        subdivisionsFile = open(
            ".spacedRepetition/data/challenges/subdivisions.txt", "r", encoding="utf-8"
        )
        subdivisionsPH = subdivisionsFile.read().split("\n")
        for index in range(len(subdivisionsPH)):
            subdivisionsPH[index] = subdivisionsPH[index].split("@")
        subdivisionsFile.close()
        # number of problems
        problemFile = open(
            ".spacedRepetition/data/challenges/problems.txt", "a", encoding="utf-8"
        )
        problemPH = problemFile.read().split("\n")
        for index in range(len(problemPH)):
            problemPH[index] = problemPH[index].split(" ")
            for indexPrime in range(len(problemPH[index])):
                problemPH[index][indexPrime] = int(problemsPH[index][indexPrime])
        problemFile.close()
        # Concatena o dicionário
        materials = []
        for index in range(len(namesPH)):
            materials.append(
                {
                    "names": namesPH[index],
                    "subdivisions": subdivisionsPH[index],
                    "problems": problemPH[index],
                }
            )
        return materials
    except:
        # here to incapsulate the empty problem
        return []


def probability(materials):
    questionDistribution = []
    for index in range(len(materials)):
        questionDistribution.append(np.sum(np.array(materials[index]["problems"])))
    questionDistribution = np.array(questionDistribution)
    print(questionDistribution)
    # return edge cases
    if len(questionDistribution) == 1:
        return np.array([1])
    elif len(questionDistribution) == 0:
        return np.array([0])
    # The standard is the most heavy challendge book has twice the probability of the smallest and others have in betwens
    # Encontrando os limites
    minimum = np.min(questionDistribution)
    maximum = np.max(questionDistribution)
    # Encontre os pesos
    notNormalizedProbability = (questionDistribution - minimum) / (maximum - minimum) + 1
    # Encontre a probabilidade
    return notNormalizedProbability / np.sum(notNormalizedProbability)


def verificarPresencaArrouba(texto: str):
    for character in texto:
        if character == "@":
            return True
    return False


def materiaisString(materiais):
    textoFinal = ["materiais randomizados :"]
    for index in range(len(materiais)):
        textoPH = str(index) + "-" + materiais[index]["nome"]
        for indexPrime in range(len(materiais[index]["exercicios"])):
            textoPH += (
                "\n  +"
                + materiais[index]["subdivisoes"][indexPrime]
                + "|"
                + str(materiais[index]["exercicios"][indexPrime])
                + " exercícios."
            )
        textoFinal.append(textoPH)
    textoFinal.append("pronto")
    return textoFinal


initializeFiles()

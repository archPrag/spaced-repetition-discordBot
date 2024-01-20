# coding: utf-8
import time

import discord

import settings
import spacedRepetitionFileHandler
import spacedRepetitionUtilities

# variáveis globais
# consiga o enunciado e exercício atual da repetição espaçada


def findQuestionsInGreaterBoxes(lesserBox, userName):
    global placeHolder
    numeberOfWaitingDays = [1, 2, 4, 7]
    colorCode = ["\u001b[0;30m", "\u001b[0;32m", "\u001b[2;33m", "\u001b[0;34m"]
    boldColorCode = ["\u001b[1;30m", "\u001b[1;32m", "\u001b[1;33m", "\u001b[0;34m"]
    writtenNumbers = ["zero", "one", "two", "three"]
    problems = spacedRepetitionFileHandler.getProblems("userName")
    print("Get question:" + str(problems))
    if lesserBox >= 4:
        print("Get questions: Box 4 reached")
        return "End of spaced repetition."
    print("Get exercises:box" + str(lesserBox))
    numericProblems=problems['numeric']
    for index in range(len(numericProblems)):
        print("Get questions: exercise" + str(index))
        if numericProblems[index]["box"] == lesserBox and numeberOfWaitingDays[
            lesserBox
        ] <= spacedRepetitionUtilities.dayDifference(
            numericProblems[index]["lastOpened"], time.time()
        ):
            print("Get questions: chosen exercise " + str(numericProblems[index]))
            placeHolder = {
                "problem": numericProblems[index],
                "index": index,
                "mode": "numeric",
            }
            return (
                "```ansi\n "
                + colorCode[lesserBox]
                + "Numeric box "
                + writtenNumbers[lesserBox]
                + "\n"
                + numericProblems[index]["question"]
                + ".\u001b[0m\n```"
            )
    theoreticalProblems = problems['theoretical']
    for index in range(len(theoreticalProblems)):
        print("get questions: exercise" + str(index))
        if theoreticalProblems[index]["box"] == lesserBox and numeberOfWaitingDays[
            lesserBox
        ] <= spacedRepetitionUtilities.dayDifference(
            theoreticalProblems[index]["lastOpened"], time.time()
        ):
            placeHolder = {
                "problem": theoreticalProblems[index],
                "index": index,
                "mode": "theoreticalWaiting",
            }
            print("Get questions: chosen exercise " + str(theoreticalProblems[index]))
            return (
                "```ansi\n "
                + boldColorCode[lesserBox]
                + "Theoretical box"
                + writtenNumbers[lesserBox]
                + "\n"
                + theoreticalProblems[index]["question"]
                + "\n(Send any question to continue)"
                + ".\u001b[0m\n```"
            )
    # Now try in the next box:
    return findQuestionsInGreaterBoxes(lesserBox + 1,userName)


def theoreticalWaiting():
    # Get dependencies
    global placeHolder
    print("Theoretical waiting: the waiting is over.")
    placeHolder["mode"] = "theoretical"
    return (
        "The answer was: \n"
        + placeHolder["problem"]["answer"]
        + "\n Did you get it right?(y,n)"
    )


def safelyDecreaseBox(initialBox):
    return initialBox - 1 + int(initialBox == 0)


def theoretical(answer):
    # get dependencies
    global placeHolder
    problems = spacedRepetitionFileHandler.getProblems()
    # Apply exercise
    print("theoretical: Did User get it right?" + answer)
    index = placeHolder["index"]
    problems[index]["lastOpened"] = int(time.time())
    answer = answer.lower()
    if answer.startswith("y"):
        problems[index]["box"] += 1
        print("theoretical:" + str(problems))
        spacedRepetitionFileHandler.saveTheoreticalProblems(problems)
        placeHolder = {"mode": "normal"}
        return "Congratulations, you got it right!!!"
    elif answer.startswith("n"):
        problems[index]["box"] = safelyDecreaseBox(problems[index]["box"])
        problems[index]["errors"] += 1
        print("theoretical:" + str(problems))
        spacedRepetitionFileHandler.saveTheoreticalProblems(problems)
        placeHolder = {"mode": "normal"}
        return "Unfortunately you got it wrong. Better luck next time!"
    # make the user put a valid input
    return "Input a valid answer 'y' or 'n'"


def numeric(answer):
    print("Numeric:answer" + answer)
    # verifies if the user inputed a valid answer
    if not spacedRepetitionUtilities.integerStringCheck(answer):
        print("Numeric: invalid non numeric input")
        return "Add a numeric answer"
    number = float(answer)
    # get dependencies
    global placeHolder
    problems = spacedRepetitionFileHandler.getNumericProblems()
    # Apply exercise
    print("Numeric:" + str(problems))
    index = placeHolder["index"]
    problems[index]["lastOpened"] = int(time.time())
    if spacedRepetitionUtilities.compareValues(
        placeHolder["problem"]["answer"],
        number,
        placeHolder["problem"]["significantFigures"],
    ):
        problems[index]["box"] += 1
        print("Numeric:" + str(problems))
        spacedRepetitionFileHandler.saveNumericProblems(problems)
        placeHolder = {"mode": "normal"}
        return "Congratulations, you got it right!!!"
    problems[index]["box"] = safelyDecreaseBox(problems[index]["box"])
    problems[index]["errors"] += 1
    uncertainty = spacedRepetitionUtilities.percentualDeviation(
        problems[index]["answer"], number
    )
    placeHolder = {"mode": "normal"}
    return (
        "Unfortunately you missed by "
        + uncertainty
        + ", the answer was "
        + str(number)
        + ". Better luck next time!"
    )


def numericAddition(answer):
    print("Numeric addition:" + answer)
    # Check if the answer is a number
    if not spacedRepetitionUtilities.floatStringCheck(answer):
        print("Numeric Addition:Non numeric answer")
        return "Add a valid numeric answer."
    # Get dependencies
    global placeHolder
    problems = spacedRepetitionFileHandler.getNumericProblems()
    # Save exercise
    question = placeHolder["problem"]["question"]
    answerFinal = float(answer)
    significantFigures = spacedRepetitionUtilities.stringSignificantFigures(answer)
    spacedRepetitionFileHandler.addNumericProblem(
        question, answerFinal, significantFigures, problems
    )
    placeHolder = {"mode": "normal"}
    print("Numeric addition:problem added")
    return "Problem (" + question + ") Added"


def theoreticalAddition(answer):
    print("Theoretical addition:" + answer)
    # import the dependencies
    global placeHolder
    problems = spacedRepetitionFileHandler.getTheoreticalProblems()
    # save the exercise
    question = placeHolder["problem"]["question"]
    spacedRepetitionFileHandler.addTheoreticalcProblem(question, answer, problems)
    placeHolder = {"mode": "normal"}
    print("Theoretical Addition : problem added")
    return "Problem (" + question + ") added."


def numericDeletion(answer: str):
    print("Numeric Deletion:" + answer)
    if not spacedRepetitionUtilities.integerStringCheck(answer):
        print("Numeric deletion: the answer is not integer")
        return "Not a valid index."
    problems = spacedRepetitionFileHandler.getTheoreticalProblems()
    spacedRepetitionFileHandler.deleteNumericProblem(int(answer), problems)
    return "Exercise deleted."


def theoreticalDeletion(answer: str):
    print("Theoretical Deletion" + answer)
    if not spacedRepetitionUtilities.integerStringCheck(answer):
        print("Theoretical Deletion: the index is not an integer")
        return "Not a valid index."
    # Delete o exercício de índice da resposta
    problems = spacedRepetitionFileHandler.getTheoreticalProblems()
    spacedRepetitionFileHandler.deleteTheoreticalExercise(int(answer), problems)
    return "Exercise deleted."


def run():
    intents = discord.Intents.default()
    intents.message_content = True

    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(client.user)
        print(client.user.id)

    @client.event
    async def on_message(message):  # receba uma mensagem do discord
        # Import global variables
        global placeHolder

        userName = message.author
        if userName == client.user:
            return
        elif message.content.startswith("!Can"):
            # Reestart bots cache
            placeHolder = {"mode": "normal"}
            print("Canceled")
            await message.channel.send("```ansi\n\u001b[0;31mCancelar\u001b[0m\n```")
        elif message.content.startswith("!Help") and placeHolder["mode"] == "normal":
            # list some exercises
            await message.channel.send(spacedRepetitionFileHandler.getHelp())
        elif message.content.startswith("!ListAll") and placeHolder["mode"] == "normal":
            # Send all exercises
            for line in spacedRepetitionFileHandler.listProblems():
                await message.channel.send(line)
        elif message.content.startswith("!List") and placeHolder["mode"] == "normal":
            # liste os exercícios incompletos
            for line in spacedRepetitionFileHandler.listUnfinishedProblems():
                await message.channel.send(line)
        elif (
            message.content.startswith("!Exercise") and placeHolder["mode"] == "normal"
        ):
            await message.channel.send(findQuestionsInGreaterBoxes(0))
        elif placeHolder["mode"] == "numeric":
            await message.channel.send(numeric(message.content))
            await message.channel.send(findQuestionsInGreaterBoxes(0))
        elif placeHolder["mode"] == "theoreticalWaiting":
            await message.channel.send(theoreticalWaiting())
        elif placeHolder["mode"] == "theoretical":
            await message.channel.send(theoretical(message.content))
            await message.channel.send(findQuestionsInGreaterBoxes(0))
        elif message.content.startswith("!NA ") and placeHolder["mode"] == "normal":
            placeHolder = {
                "mode": "numericAddition",
                "problem": {
                    "question": message.content[4:],
                    "answer": 0,
                    "lastOpened": 0,
                    "box": 0,
                    "error": 0,
                },
            }
            await message.channel.send("What is the numeric answer?")
        elif placeHolder["mode"] == "numericAddition":
            await message.channel.send(numericAddition(message.content))
        elif message.content.startswith("!TA ") and placeHolder["mode"] == "normal":
            placeHolder = {
                "mode": "theoreticalAddition",
                "problem": {
                    "question": message.content[4:],
                    "answer": "",
                    "lastOpened": 0,
                    "box": 0,
                    "error": 0,
                },
            }
            await message.channel.send("What is the theoretical answer?")
        elif placeHolder["mode"] == "theoreticalAddition":
            await message.channel.send(theoreticalAddition(message.content))
        elif placeHolder["mode"] == "normal" and message.content.startswith("!ND "):
            await message.channel.send(numericDeletion(message.content[4:]))
        elif placeHolder["mode"] == "normal" and message.content.startswith("!TD "):
            await message.channel.send(theoreticalDeletion(message.content[4:]))
        print(userName)

    client.run(settings.DISCORD_API_SECRET)


if __name__ == "__main__":
    run()

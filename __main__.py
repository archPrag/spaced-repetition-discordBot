# coding: utf-8
import time

import discord

import settings
import spacedRepetitionFileHandler
import spacedRepetitionUtilities

# variáveis globais
# consiga o enunciado e exercício atual da repetição espaçada


def findQuestionsInGreaterBoxes(lesserBox, userName):
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
    numericProblems = problems["numeric"]
    for index in range(len(numericProblems)):
        print("Get questions: exercise" + str(index))
        if numericProblems[index]["box"] == lesserBox and numeberOfWaitingDays[
            lesserBox
        ] <= spacedRepetitionUtilities.dayDifference(
            numericProblems[index]["lastOpened"], time.time()
        ):
            print("Get questions: chosen exercise " + str(numericProblems[index]))
            spacedRepetitionFileHandler.setUserState(
                {
                    "problem": numericProblems[index],
                    "index": index,
                    "mode": "numeric",
                },
                userName,
            )
            return (
                "```ansi\n "
                + colorCode[lesserBox]
                + "Numeric box "
                + writtenNumbers[lesserBox]
                + "\n"
                + numericProblems[index]["question"]
                + ".\u001b[0m\n```"
            )
    theoreticalProblems = problems["theoretical"]
    for index in range(len(theoreticalProblems)):
        print("get questions: exercise" + str(index))
        if theoreticalProblems[index]["box"] == lesserBox and numeberOfWaitingDays[
            lesserBox
        ] <= spacedRepetitionUtilities.dayDifference(
            theoreticalProblems[index]["lastOpened"], time.time()
        ):
            spacedRepetitionFileHandler.setUserState(
                {
                    "problem": theoreticalProblems[index],
                    "index": index,
                    "mode": "theoreticalWaiting",
                },
                userName,
            )
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
    return findQuestionsInGreaterBoxes(lesserBox + 1, userName)


def theoreticalWaiting(userName):
    # Get dependencies
    state = spacedRepetitionFileHandler.getProblems(userName)
    print("Theoretical waiting: the waiting is over.")
    state["mode"] = "theoretical"
    spacedRepetitionFileHandler.setUserState(state, userName)
    return (
        "The answer was: \n"
        + state["problem"]["answer"]
        + "\n Did you get it right?(y,n)"
    )


def safelyDecreaseBox(initialBox):
    return initialBox - 1 + int(initialBox == 0)


def theoretical(answer, userName):
    # get dependencies
    state = spacedRepetitionFileHandler.getUserState(userName)
    problems = spacedRepetitionFileHandler.getProblems(userName)
    # Apply exercise
    print("theoretical: Did User get it right?" + answer)
    index = state["index"]
    problems[index]["lastOpened"] = int(time.time())
    answer = answer.lower()
    if answer.startswith("y"):
        problems["theoretical"][index]["box"] += 1
        print("theoretical:" + str(problems))
        spacedRepetitionFileHandler.saveProblems(problems, userName)
        state = {"mode": "normal"}
        spacedRepetitionFileHandler.setUserState(state, userName)
        return "Congratulations, you got it right!!!"
    elif answer.startswith("n"):
        problems["theoretical"][index]["box"] = safelyDecreaseBox(
            problems["theoretical"][index]["box"]
        )
        problems["theoretical"][index]["errors"] += 1
        print("theoretical:" + str(problems))
        spacedRepetitionFileHandler.saveProblems(problems, userName)
        state = {"mode": "normal"}
        spacedRepetitionFileHandler.setUserState(state, userName)
        return "Unfortunately you got it wrong. Better luck next time!"
    # make the user put a valid input
    return "Input a valid answer 'y' or 'n'"


def numeric(answer,userName):
    print("Numeric:answer" + answer)
    if not spacedRepetitionUtilities.integerStringCheck(answer):
        print("Numeric: invalid non numeric input")
        return "Add a numeric answer"
    number = float(answer)
    state=spacedRepetitionFileHandler.getUserState(userName)
    problems = spacedRepetitionFileHandler.getProblems(userName)
    print("Numeric:" + str(problems))
    index = state["index"]
    problems[index]["lastOpened"] = int(time.time())
    if spacedRepetitionUtilities.compareValues(
        state["problem"]["answer"],
        number,
        state["problem"]["significantFigures"],
    ):
        problems['numeric'][index]["box"] += 1
        print("Numeric:" + str(problems))
        spacedRepetitionFileHandler.saveProblems(problems,userName)
        state = {"mode": "normal"}
        spacedRepetitionFileHandler.setUserState(state,userName)
        return "Congratulations, you got it right!!!"
    problems['numeric'][index]["box"] = safelyDecreaseBox(problems[''][index]["box"])
    problems[numeric][index]["errors"] += 1
    uncertainty = spacedRepetitionUtilities.percentualDeviation(
        problems['numeric'][index]["answer"], number
    )
    state = {"mode": "normal"}
    spacedRepetitionFileHandler.setUserState(state,userName)
    return (
        "Unfortunately you missed by "
        + uncertainty
        + ", the answer was "
        + str(number)
        + ". Better luck next time!"
    )


def numericAddition(answer,userName):
    print("Numeric addition:" + answer)
    # Check if the answer is a number
    if not spacedRepetitionUtilities.floatStringCheck(answer):
        print("Numeric Addition:Non numeric answer")
        return "Add a valid numeric answer."
    # Get dependencies
    state=spacedRepetitionFileHandler.getUserState(userName)
    problems = spacedRepetitionFileHandler.getProblems(userName)
    # Save exercise
    question = state["problem"]["question"]
    answerFinal = float(answer)
    significantFigures = spacedRepetitionUtilities.stringSignificantFigures(answer)
    spacedRepetitionFileHandler.addNumericProblem(
        question, answerFinal, significantFigures, problems,userName
    )
    state = {"mode": "normal"}
    spacedRepetitionFileHandler.setUserState(state,userName)
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

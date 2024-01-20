import time

import fileHandler
import utilities


def findQuestionsInGreaterBoxes(lesserBox, userName):
    numeberOfWaitingDays = [1, 2, 4, 7]
    colorCode = ["\u001b[0;30m", "\u001b[0;32m", "\u001b[2;33m", "\u001b[0;34m"]
    boldColorCode = ["\u001b[1;30m", "\u001b[1;32m", "\u001b[1;33m", "\u001b[0;34m"]
    writtenNumbers = ["zero", "one", "two", "three"]
    problems = fileHandler.getProblems(userName)
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
        ] <= utilities.dayDifference(numericProblems[index]["lastOpened"], time.time()):
            print("Get questions: chosen exercise " + str(numericProblems[index]))
            fileHandler.setUserState(
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
        ] <= utilities.dayDifference(
            theoreticalProblems[index]["lastOpened"], time.time()
        ):
            fileHandler.setUserState(
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
    state = fileHandler.getUserState(userName)
    print("Theoretical waiting: the waiting is over.")
    state["mode"] = "theoretical"
    fileHandler.setUserState(state, userName)
    return (
        "The answer was: \n"
        + state["problem"]["answer"]
        + "\n Did you get it right?(y,n)"
    )


def safelyDecreaseBox(initialBox):
    return initialBox - 1 + int(initialBox == 0)


def theoretical(answer, userName):
    # get dependencies
    state = fileHandler.getUserState(userName)
    problems = fileHandler.getProblems(userName)
    # Apply exercise
    print("theoretical: Did User get it right?" + answer)
    index = state["index"]
    problems["theoretical"][index]["lastOpened"] = int(time.time())
    answer = answer.lower()
    if answer.startswith("y"):
        problems["theoretical"][index]["box"] += 1
        print("theoretical:" + str(problems))
        fileHandler.saveProblems(problems, userName)
        state = {"mode": "normal"}
        fileHandler.setUserState(state, userName)
        return "Congratulations, you got it right!!!"
    elif answer.startswith("n"):
        problems["theoretical"][index]["box"] = safelyDecreaseBox(
            problems["theoretical"][index]["box"]
        )
        problems["theoretical"][index]["errors"] += 1
        print("theoretical:" + str(problems))
        fileHandler.saveProblems(problems, userName)
        state = {"mode": "normal"}
        fileHandler.setUserState(state, userName)
        return "Unfortunately you got it wrong. Better luck next time!"
    # make the user put a valid input
    return "Input a valid answer 'y' or 'n'"


def numeric(answer, userName):
    print("Numeric:answer" + answer)
    if not utilities.integerStringCheck(answer):
        print("Numeric: invalid non numeric input")
        return "Add a numeric answer"
    number = float(answer)
    state = fileHandler.getUserState(userName)
    problems = fileHandler.getProblems(userName)
    print("Numeric:" + str(problems))
    index = state["index"]
    problems["numeric"][index]["lastOpened"] = int(time.time())
    if utilities.compareValues(
        state["problem"]["answer"],
        number,
        state["problem"]["significantFigures"],
    ):
        problems["numeric"][index]["box"] += 1
        print("Numeric:" + str(problems))
        fileHandler.saveProblems(problems, userName)
        state = {"mode": "normal"}
        fileHandler.setUserState(state, userName)
        return "Congratulations, you got it right!!!"
    problems["numeric"][index]["box"] = safelyDecreaseBox(problems[""][index]["box"])
    problems[numeric][index]["errors"] += 1
    uncertainty = utilities.percentualDeviation(
        problems["numeric"][index]["answer"], number
    )
    state = {"mode": "normal"}
    fileHandler.setUserState(state, userName)
    return (
        "Unfortunately you missed by "
        + uncertainty
        + ", the answer was "
        + str(number)
        + ". Better luck next time!"
    )

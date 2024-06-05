import time
import fileHandler
import utilities
import materials

numberOfBoxes=4
basicDivision=[1,2,4,7]
numericalColorCode = ["\u001b[0;30m", "\u001b[0;32m", "\u001b[2;33m", "\u001b[0;34m"]
theoreticalColorCode = ["\u001b[1;30m", "\u001b[1;32m", "\u001b[1;33m", "\u001b[0;34m"]
boxNames = ["zero", "one", "two", "three"]




def findQuestion(userName):
    global numberOfBoxes
    global basicDivision
    global numericalColorCode
    global theoreticalColorCode
    global boxNames
    numberOfWaitingDays=[]
    problems = fileHandler.getProblems(userName)
    variables=fileHandler.getUserVars(userName)
    stringRandom=variables["randomizedString"]
    numericProblems = problems["numeric"]
    print("Get question:" + str(problems))
    if numberOfBoxes<=len(basicDivision):
        for index in range(numberOfBoxes):
            numberOfWaitingDays.append(basicDivision[index])
    if numberOfBoxes>4:
        numberOfWaitingDays=basicDivision
        for index in range(len(basicDivision),numberOfBoxes):
            numberOfWaitingDays.append(basicDivision[-1]*(index-len(basicDivision)+1))
    for box in range(numberOfBoxes):
        print("Get exercises:box" + str(box))
        for index in range(len(numericProblems)):
            print("Get questions: exercise" + str(index))
            if numericProblems[index]["box"] == box and numberOfWaitingDays[ box ] <= utilities.dayDifference(numericProblems[index]["lastOpened"], time.time()):
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
                    + numericalColorCode[box]
                    + "Numeric box "
                    + boxNames[box]
                    + "\n(numeric problem "+str(index)+")"
                    + numericProblems[index]["question"]
                    + ".\u001b[0m\n```"
                )
        theoreticalProblems = problems["theoretical"]
        for index in range(len(theoreticalProblems)):
            print("get questions: exercise" + str(index))
            if theoreticalProblems[index]["box"] == box and numberOfWaitingDays[
                box
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
                    + theoreticalColorCode[box]
                    + "Theoretical box "
                    + boxNames[box]
                    + "\n (theoretical problem "+str(index)+")"
                    + theoreticalProblems[index]["question"]
                    + "\n(Send any question to continue)"
                    + ".\u001b[0m\n```"
                )
    # Now try in the next box:
    print("Get questions: Box 4 reached")
    if utilities.dayDifference(variables["lastRandomized"],time.time())>=1:
        stringRandom=materials.chooseDayMaterials(userName)
        variables["lastRandomized"]=time.time()
        variables["randomizedString"]=stringRandom
        fileHandler.setUserVars(variables,userName)
    return stringRandom


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
    if not utilities.floatStringCheck(answer):
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
    problems["numeric"][index]["box"] = safelyDecreaseBox(
        problems["numeric"][index]["box"]
    )
    problems["numeric"][index]["errors"] += 1
    state = {"mode": "normal"}
    fileHandler.saveProblems(problems,userName)
    fileHandler.setUserState(state, userName)
    return (
        "Unfortunately you missed, the answer was "
        + str(problems['numeric'][index]['answer'])
        + ". Better luck next time!"
    )

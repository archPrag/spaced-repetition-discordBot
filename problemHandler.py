import time
import fileHandler
import utilities
import materials

numberOfBoxes=4
basicDivision=[1,2,4,7]
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
        for index in range(len(problems)):
            print("get questions: exercise" + str(index))
            if problems[index]["box"] == box and numberOfWaitingDays[
                box
            ] <= utilities.dayDifference(
                problems[index]["lastOpened"], time.time()
            ):
                fileHandler.setUserState(
                    {
                        "problem": problems[index],
                        "index": index,
                        "mode": "waiting",
                    },
                    userName,
                )
                print("Get questions: chosen exercise " + str(problems[index]))
                return {"message":"```ansi\n "
                    + theoreticalColorCode[box]
                    + "box "
                    + boxNames[box]
                    + "\n (problem "+str(index)+")"
                    + problems[index]["question"]
                    + "\n(Send any question to continue)"
                    + ".\u001b[0m\n```",
                    "image":problems[index]["image"]
                    }
    # Now try in the next box:
    print("Get questions: Box 4 reached")
    if utilities.dayDifference(variables["lastRandomized"],time.time())>=1:
        stringRandom=materials.chooseDayMaterials(userName)
        variables["lastRandomized"]=time.time()
        variables["randomizedString"]=stringRandom
        fileHandler.setUserVars(variables,userName)
    return stringRandom

def waiting(userName):
    # Get dependencies
    state = fileHandler.getUserState(userName)
    print("Theoretical waiting: the waiting is over.")
    state["mode"] = "problem"
    fileHandler.setUserState(state, userName)
    return (
        "The answer was: \n"
        + state["problem"]["answer"]
        + "\n Did you get it right?(y,n)"
    )


def safelyDecreaseBox(initialBox):
    return initialBox - 1 + int(initialBox == 0)


def problemEnd(answer, userName):
    # get dependencies
    state = fileHandler.getUserState(userName)
    problems = fileHandler.getProblems(userName)
    # Apply exercise
    print("problem: Did User get it right?" + answer)
    index = state["index"]
    problems[index]["lastOpened"] = int(time.time())
    answer = answer.lower()
    if answer.startswith("y"):
        problems[index]["box"] += 1
        print("problem:" + str(problems))
        fileHandler.saveProblems(problems, userName)
        state = {"mode": "normal"}
        fileHandler.setUserState(state, userName)
        return "Congratulations, you got it right!!!"
    elif answer.startswith("n"):
        problems[index]["box"] = safelyDecreaseBox(
            problems[index]["box"]
        )
        problems[index]["errors"] += 1
        print("problem:" + str(problems))
        fileHandler.saveProblems(problems, userName)
        state = {"mode": "normal"}
        fileHandler.setUserState(state, userName)
        return "Unfortunately you got it wrong. Better luck next time!"
    # make the user put a valid input
    return "Input a valid answer 'y' or 'n'"



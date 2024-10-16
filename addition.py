import fileHandler
import utilities
import json

def problem(answer,userName):
    print("Problem addition:" + answer)
    # import the dependencies
    state=fileHandler.getUserState(userName)
    problems = fileHandler.getProblems(userName)
    # save the exercise
    question = state["problem"]["question"]
    path=state["problem"]["imagePath"]
    fileHandler.addProblem(question, answer, problems,path,userName)
    state = {"mode": "normal"}
    fileHandler.setUserState(state,userName)
    print("Theoretical Addition : problem added")
    return "Problem (" + question + ") added."
def materialAdd(answer,userName):
    try:
        answerD=json.loads(answer)
        chapName=answerD["chapName"]
        title=answerD["title"]
        perChap=answerD["perChap"]
        fileHandler.addMaterial(title,chapName,perChap,userName)
        return "material added"
    except:
        return "something went wrong material not added"



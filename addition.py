import fileHandler
import utilities

def numeric(answer,userName):
    print("Numeric addition:" + answer)
    # Check if the answer is a number
    if not utilities.floatStringCheck(answer):
        print("Numeric Addition:Non numeric answer")
        return "Add a valid numeric answer."
    # Get dependencies
    state=fileHandler.getUserState(userName)
    problems = fileHandler.getProblems(userName)
    # Save exercise
    question = state["problem"]["question"]
    answerFinal = float(answer)
    significantFigures = utilities.stringSignificantFigures(answer)
    fileHandler.addNumericProblem(
        question, answerFinal, significantFigures, problems,userName
    )
    state = {"mode": "normal"}
    fileHandler.setUserState(state,userName)
    print("Numeric addition:problem added")
    return "Problem (" + question + ") Added"


def theoretical(answer,userName):
    print("Theoretical addition:" + answer)
    # import the dependencies
    state=fileHandler.getUserState(userName)
    problems = fileHandler.getProblems(userName)
    # save the exercise
    question = state["problem"]["question"]
    fileHandler.addTheoreticalProblem(question, answer, problems,userName)
    state = {"mode": "normal"}
    fileHandler.setUserState(state,userName)
    print("Theoretical Addition : problem added")
    return "Problem (" + question + ") added."

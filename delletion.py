import fileHandler
import utilities

def numeric(answer,userName):
    print("Numeric Deletion:" + answer)
    if not utilities.integerStringCheck(answer):
        print("Numeric deletion: the answer is not integer")
        return "Not a valid index."
    problems = fileHandler.getProblems(userName)
    fileHandler.deleteNumericProblem(int(answer), problems,userName)
    return "Exercise deleted."


def theoretical(answer,userName):
    print("Theoretical Deletion" + answer)
    if not utilities.integerStringCheck(answer):
        print("Theoretical Deletion: the index is not an integer")
        return "Not a valid index."
    problems = fileHandler.getProblems(userName)
    fileHandler.deleteTheoreticalExercise(int(answer), problems,userName)
    return "Exercise deleted."
def materialDel(answer,userName):
    if not fileHandler.materialExists(answer,userName):
        return "Could not find material "+ answer
    fileHandler.deleteMaterials(answer,userName)
    return "material Deleted"

import fileHandler
import utilities


def problemDel(answer,userName):
    print("problemDel" + answer)
    if not utilities.integerStringCheck(answer):
        print("Theoretical Deletion: the index is not an integer")
        return "Not a valid index."
    problems = fileHandler.getProblems(userName)
    fileHandler.deleteProblem(int(answer), problems,userName)
    return "Exercise deleted."
def materialDel(answer,userName):
    if not fileHandler.materialExists(answer,userName):
        return "Could not find material "+ answer
    fileHandler.deleteMaterials(answer,userName)
    return "material Deleted"

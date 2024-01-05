# coding: utf-8
import random
import time

import discord
import numpy as np

import DesafiosFileHandler
import initialiseDirectories
import settings
import spacedRepetitionFileHandler
import spacedRepetitionUtilities

# variáveis globais
placeHolder = {"mode":"normal"}
# consiga o enunciado e exercício atual da repetição espaçada


def findQuestionsInGreaterBoxes(lesserBox):
    #import global variables
    global placeHolder
    numeberOfWaitingDays=[1,2,4,7]
    colorCode=["\001b[0m","\u001b[0;32m","\u001b[2;33m","\u001b[0;34m"]
    boldColorCode=["\001b[1m","\u001b[1;32m","\u001b[1;33m","\u001b[0;34m"]
    writtenNumbers=["zero","one","two","three"]
    numericProblems = spacedRepetitionFileHandler.getNumericProblems()
    theoreticalProblems = spacedRepetitionFileHandler.getTheoreticalProblems()
    print("Get question:" + str(numericProblems) + str(theoreticalProblems))
    #if lesser box is greater than four return(this is a recursion code)
    if lesserBox>=4:
        print("Get questions: Box 4 reached")
        return "End of spaced repetition"
    # Try to find a problem from lesserBox
    print("Get exercises:box"+str(lesserBox))
    for index in range(len(numericProblems)):
        print("Get questions: exercise" + str(index))
        if numericProblems[index][
            "box"
        ] == lesserBox and numeberOfWaitingDays[lesserBox] <= spacedRepetitionUtilities.dayDifference(
            numericExercises[index]["lastOpened"], time.time()
        ):
            print("Get questions: chosen exercise " + str(numericProblems[index]))
            placeHolder = {"problem":numericProblems[index],
            "index":index,
            "mode":"numeric"
            }
            return (
                "```ansi\n "+colorCode[lesserBox]+"Numeric box "+writtenNumber[lesserBox]+"\n"
                + numericProblems[index]["question"]
                + "\u001b[0m\n```"
            )
    #Now try finding from theoretical lesser box
    for index in range(len(theoreticalproblems)):
        print("get questions: exercise" + str(index))
        if theoreticalProblem[index][
            "box"
        ] == lesserBox and numberOfWaitingDays <= spacedRepetitionUtilities.dayDifference(
            theoreticalProblems[index]["lastOpened"], time.time()
        ):
            placeHolder = {"problem":theoreticalProblems[index],
                           "index":index,
                           "mode":"theoreticalWaiting"
                           }
            print("Get questions: chosen exercise " + str(theoreticalProblems[index]))
            modo = "theoreticalWaiting"
            return (
                "```ansi\n "+boldColorCode[lesserBox]+"Theoretical box"+writtenNumber[lesserBox]+"\n"
                + theoreticalProblems[index]["question"]
                + "\n(Send any question to continue)"
                + "\u001b[0m\n```"
            )
    #Now try in the next box:
    return findQuestionInGreaterBoxes(lesserBox+1)




def theoreticalWaiting():
    #Get dependencies
    global placeHolder
    # Finalize o modo de espera teórico
    print("Theoretical waiting: the waiting is over.")
    placeHolder["mode"] = "theoretical"
    return "The answer was: \n" + placeHolder["problem"]["answer"] + "\n Did you get it right?(y,n)"

def safelyDecreaseBox(initialBox):
    return initialBox-1+int(initialBox==0)

def theoretical(answer: str):
    #get dependencies
    global placeHolder
    problems = spacedRepetitionFileHandler.getTheoreticalProblems()
    #Apply exercise
    print("theoretical: Did User get it right?" + answer)
    index=placeHolder["index"]
    problems[index]["lastOpened"] = int(time.time())
    answer = answer.lower()
    if answer.startswith("y"):
        problems[index]["box"] += 1
        print(
            "theoretical:"
                + str(problems)
            )
        spacedRepetitionFileHandler.saveTheoreticalProblems(problems)
        placeHolder = {"mode":"normal"}
        return "Congratulations, you got it right!!!"
    elif resposta.startswith("n"):
        problems[index]["box"]=SafelyDecreaseBox(problems[index]["box"])
        problems[index]["errors"]+=1;
        print(
            "theoretical:"
                + str(problems)
            )
        spacedRepetitionFileHandler.saveTheoreticalProblems(problems)
        placeHolder = {"mode":"normal"}
        return "Unfortunately you got it wrong. Better luck next time!"
    #make the user put a valid input
    return "Input a valid answer 'y' or 'n'"


def numeric(answer: str):
    print("Numeric:answer" + answer)
    #verifies if the user inputed a valid answer
    if not spacedRepetitionUtilities.integerStringCheck(answer):
        print("Numeric: invalid non numeric input")
        return "Add a numeric answer"
    number = float(answer)
    #get dependencies
    global placeHolder
    problems = spacedRepetitionFileHandler.getNumericExercise()
    #Apply exercise
    print(
        "Numeric:"
        + str(problems)
    )
    index=placeHolder["index"]
    problems[index]["lastOpened"]=int(time.time())
    if spacedRepetitionUtilities.compareValueS(
        placeHolder["problem"]["answer"], number, placeHolder["problem"]["significantFigures"]
    ):
        problems[index]["box"]+=1
        print(
            "Numeric:"
            + str(problems)
        )
        spacedRepetitionFileHandler.saveNumericProblems(problems)
        placeHolder={"mode":"normal"}
        return "Congratulations, you got it right!!!"
    problems[index]["box"]=safelyDecreaseBox(problems[index]["box"])
    problems[index]["errors"] += 1
    uncertainty = spacedRepetitionUtilities.percentualDeviation(
    problems[index]["answer"], number
    )
    placeHolder = {"mode":"normal"}
    return "Unfortunately you missed by " + uncertainty + " the answer was "+str(number)+". Better luck next time!"

def numericAddition(answer: str):
    print("Numeric addition:" + answer)
    #Check if the answer is a number
    if not spacedRepetitionUtilities.floatStringCheck(answer):
        print("Numeric Addition:Non numeric answer")
        return "Add a valid numeric answer."
    #Get dependencies
    global placeHolder
    problems = spacedRepetitionFileHandler.getNumericExercise()
    #Save exercise
    question = placeHolder["question"]
    answerFinal = float(answer)
    significantDigits = spacedRepetitionUtilities.stringSignificantFigures(answer)
    spacedRepetitionFileHandler.addNumericProblem(
        question, answerFinal, significantFigures, numericExercises
    )
    placeHolder = {"mode":"normal"}
    print("Numeric addition:problem added")
    return "Problem (" + enunciado + ") Added"


def theoreticalDeletion(answer: str):
    print("Theoretical addition:" + answer)
    #import the dependencies
    global placeHolder
    problems=spacedRepetitionFileHandler.getTheoreticalProblems()
    #save the exercise
    question = placeHolder["answer"]
    spacedRepetitionFileHandler.addTheoreticalcProblem(
        question, answer, theoricExercise
    )
    placeHolder={"mode":"normal"}
    print("Theoretical Addition : problem added")
    return "Problem (" + enunciado + ") added."


def numericDeletion(answer: str):
    print("Numeric Deletion:" + answer)
    if not spacedRepetitionUtilities.integerStringCheck(answer):
        print("Numeric deletion: the answer is not integer")
        return "Not a valid index."
    problems = spacedRepetitionFileHandler.getNumericExercise()
    spacedRepetitionFileHandler.deleteNumericProblem(
        int(answer), problems
    )
    return "Exercise deleted."


def theoreticalDeletion(answer: str):
    print("Theoretical Deletion" + answer)
    if not spacedRepetitionUtilities.integerStringCheck(string):
        print("Theoretical Deletion: the index is not an integer")
        return "Not a valid index."
    # Delete o exercício de índice da resposta
    problems = spacedRepetitionFileHandler.getTheoreticalProblems()
    spacedRepetitionFileHandler.deletarExercicioTeorico(
        int(answer), problems
    )
    return "Deleted Exercise"


def procedimentoDeAdicaoDeMateriais(resposta: str):
    # Consiga Dependencias
    global exercicioAtual
    global modo
    print("Adição de materiais:" + resposta)
    # Comece a adicionar
    exercicioAtual["nome"] = resposta
    modo = "esperaSubdivisao"
    exercicioAtual["subdivisoes"] = []
    return (
        "Começando a adicionar Material " + resposta + "\nQual o nome da subdivisão 1?"
    )


def procedimentoAdicaoSubdivisoes(resposta: str):
    # consiga as dependencias
    global exercicioAtual
    global modo
    # Verifique se a resposta é válida:
    if DesafiosFileHandler.verificarPresencaArrouba(resposta):
        return (
            "Adicione uma resposta sem @,obrigado.\n Qual o nome da subdivisão "
            + str(len(exercicioAtual["subdivisoes"]))
            + "?(Digite c# para terminar)"
        )
    # Verifique se é para cancelar
    print("Adição de subdivisões" + resposta)
    if len(exercicioAtual) != 0 and resposta == "c#":
        modo = "esperaNumeroExercicios"
        exercicioAtual["exercicios"] = []
        return (
            "Pronto. \n Qual o número de exercícios("
            + exercicioAtual["subdivisoes"][0]
            + ")?"
        )
    # Adicione a subdivisão
    exercicioAtual["subdivisoes"].append(resposta)
    return (
        "Qual o nome da subdivisão "
        + str(len(exercicioAtual["subdivisoes"]) + 1)
        + "?(Digite c# para terminar)"
    )


def procedimentoFinalAdicaoMateriais(resposta: str):
    print("Adição de numéro de exercício em material:" + resposta)
    # consiga as dependencias
    global exercicioAtual
    global modo
    # Cheque se é válido:
    if not DesafiosFileHandler.checagemInteiraDeStrings(resposta):
        return (
            "Não é um número inteiro, adicione uma resposta válida\n Qual o número de exercícios("
            + exercicioAtual["subdivisoes"][len(exercicioAtual["exercicios"])]
            + ")?"
        )
    # Adicione o número na dependencia
    exercicioAtual["exercicios"].append(int(resposta))
    if len(exercicioAtual["exercicios"]) == len(exercicioAtual["subdivisoes"]):
        # Verifique se não é o último à adicionar se for finalize
        materiais = DesafiosFileHandler.ConseguirDesafios()
        materiais.append(exercicioAtual)
        print(materiais)
        DesafiosFileHandler.salvarDesafios(materiais)
        stringFinal = "material: " + exercicioAtual["nome"] + " com subdivisões"
        for index in range(len(exercicioAtual["exercicios"])):
            stringFinal += (
                "\n***"
                + exercicioAtual["subdivisoes"][index]
                + "("
                + str(exercicioAtual["exercicios"][index])
                + " exercicios)"
            )
        stringFinal += "adicionado"
        modo = "normal"
        exercicioAtual = {}
        return stringFinal
    return (
        "Qual o número de exercícios("
        + exercicioAtual["subdivisoes"][len(exercicioAtual["exercicios"])]
        + ")?"
    )


def delecaoDeMateriais(resposta: str):
    print("Deleção de materiais: " + resposta)
    # Verifique se é válido
    if not DesafiosFileHandler.checagemInteiraDeStrings(resposta):
        return "resposta inválida"
    # Delete o exercício
    materiais = DesafiosFileHandler.ConseguirDesafios()
    nomeADeletar = materiais[int(resposta)]["nome"]
    materiais.pop(int(resposta))
    DesafiosFileHandler.salvarDesafios(materiais)
    return "Material(" + nomeADeletar + ") deletado."


def randomizarExercicio():
    # Consegue as dependências
    materiais = DesafiosFileHandler.ConseguirDesafios()
    probabilidades = DesafiosFileHandler.probabilidade(materiais)
    print(probabilidades)
    # Joga um dado real de 0 até 1
    dadoIncontavel = 1 - random.random()
    print(dadoIncontavel)
    # Escolha um material
    materialEscolhido = 0
    for index in range(len(probabilidades)):
        if dadoIncontavel < probabilidades[index]:
            materialEscolhido = index
            break
        dadoIncontavel -= probabilidades[index]
    # Escolha um exercício:
    exercicioEscolhido = random.randrange(
        1, np.sum(materiais[materialEscolhido]["exercicios"]) + 1
    )
    # interprete o exercício
    for index in range(len(materiais[materialEscolhido]["exercicios"])):
        if materiais[materialEscolhido]["exercicios"][index] >= exercicioEscolhido:
            return (
                materiais[materialEscolhido]["nome"]
                + "("
                + materiais[materialEscolhido]["subdivisoes"][index]
                + ") exercício "
                + str(exercicioEscolhido)
                + "."
            )
        exercicioEscolhido -= materiais[materialEscolhido]["exercicios"][index]


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
        # importe as variáveis Globais
        global modo
        global exercicioAtual
        # verifique se o bot foi quem enviou
        if message.author == client.user:
            return
        elif message.content.startswith("!Can"):
            # Pare tudo que estiver fazendo e limpe em outras palavras cancele
            modo = "normal"
            exercicioAtual = {}
            print("Cancelado")
            await message.channel.send("```ansi\n\u001b[0;31mCancelar\u001b[0m\n```")
        elif message.content.startswith("!Help") and modo == "normal":
            # mande o textão com os comandos
            await message.channel.send(spacedRepetitionFileHandler.conseguirAjuda())
        elif message.content.startswith("!ListAll") and modo == "normal":
            # liste os exercícios
            for line in spacedRepetitionFileHandler.listarExercicios():
                await message.channel.send(line)
        elif message.content.startswith("!List") and modo == "normal":
            # liste os exercícios incompletos
            for line in spacedRepetitionFileHandler.listarExerciciosIncompletos():
                await message.channel.send(line)
        elif message.content.startswith("!Exercise") and modo == "normal":
            await message.channel.send(conseguirEnunciado())
        elif message.content.startswith("!GenExercise") and modo == "normal":
            await message.channel.send(randomizarExercicio())
        elif modo == "numerico":
            await message.channel.send(procedimentoNumerico(message.content))
            await message.channel.send(conseguirEnunciado())
        elif modo == "esperaTeorica":
            await message.channel.send(procedimentoDeEsperaTeorica())
        elif modo == "teorico":
            await message.channel.send(procedimentoTeorico(message.content))
            await message.channel.send(conseguirEnunciado())
        elif message.content.startswith("!NA ") and modo == "normal":
            exercicioAtual["enunciado"] = message.content[4:]
            modo = "adicaoNumerica"
            await message.channel.send("Qual o gabarito numérico?")
        elif modo == "adicaoNumerica":
            await message.channel.send(adicaoNumerica(message.content))
        elif message.content.startswith("!TA ") and modo == "normal":
            exercicioAtual["enunciado"] = message.content[4:]
            modo = "adicaoTeorica"
            await message.channel.send("Qual o gabarito teórico?")
        elif modo == "adicaoTeorica":
            await message.channel.send(adicaoTeorica(message.content))
        elif modo == "normal" and message.content.startswith("!ND "):
            await message.channel.send(
                procedimentoDeDelecaoNumerica(message.content[4:])
            )
        elif modo == "normal" and message.content.startswith("!TD "):
            await message.channel.send(
                procedimentoDeDelecaoTeorica(message.content[4:])
            )
        elif modo == "normal" and message.content.startswith("!MA "):
            await message.channel.send(
                procedimentoDeAdicaoDeMateriais(message.content[4:])
            )
        elif modo == "normal" and message.content.startswith("!MD "):
            await message.channel.send(delecaoDeMateriais(message.content[4:]))
        elif modo == "normal" and message.content.startswith("!GenList"):
            for line in DesafiosFileHandler.materiaisString(
                DesafiosFileHandler.ConseguirDesafios()
            ):
                await message.channel.send(line)
        elif modo == "esperaSubdivisao":
            await message.channel.send(procedimentoAdicaoSubdivisoes(message.content))
        elif modo == "esperaNumeroExercicios":
            await message.channel.send(
                procedimentoFinalAdicaoMateriais(message.content)
            )
        elif message.content.startswith("!"):
            await message.channel.send(
                "Isso não é um comando válido: digite !Help para ajuda"
            )

    client.run(settings.DISCORD_API_SECRET)


if __name__ == "__main__":
    run()

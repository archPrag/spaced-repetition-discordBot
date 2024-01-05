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
modo = "normal"
exercicioAtual = {}
# consiga o enunciado e exercício atual da repetição espaçada


def getQuestions():
    # importe os exercícios e variáveis globais
    global modo
    global exercicioAtual
    numericProblems = spacedRepetitionFileHandler.getNumericProblems()
    theoreticalProblems = spacedRepetitionFileHandler.getTheoreticalProblems()
    print("Get exercises:" + str(numericProblems) + str(theoreticalProblems))
    # Find a problem from numeric box 0
    for index in range(len(numericProblems)):
        print("Get question: problem " + str(index))
        if numericProblems[index][
            "caixa"
        ] == 0 and 1 <= spacedRepetitionUtilities.dayDifference(
            numericProblems[index]["lastOpened"], time.time()
        ):
            print("Get question" + str(numericProblems[index]))
            exercicioAtual = numericProblems[index]
            modo = "numeric"
            return "Numeric box 0:\n" + numericProblems[index]["question"]
            # didn't find, try again in the next box ...
    for index in range(len(theoreticalProblems)):
        print("Obter enunciado: exercício" + str(index))
        if theoreticalProblems[index][
            "caixa"
        ] == 0 and 1 <= spacedRepetitionUtilities.dayDifference(
            theoreticalProblems[index]["lastOpened"], time.time()
        ):
            print("Obter enunciados:" + str(exerciciosTeoricos[index]))
            exercicioAtual = exerciciosTeoricos[index]
            modo = "esperaTeorica"
            return (
                "Caixa zero teórica:\n"
                + exerciciosTeoricos[index]["enunciado"]
                + "\n(Envie qualquer mensagem para continuar)"
            )
    print("caixa 1")
    # Não achou? ache um da caixa 1 numérica
    for index in range(len(exerciciosNumericos)):
        print("Obter enunciado: exercício" + str(index))
        if exerciciosNumericos[index][
            "caixa"
        ] == 1 and 2 <= spacedRepetitionUtilities.diferencaEmDias(
            exerciciosNumericos[index]["ultimaAbertura"], time.time()
        ):
            print("Obter enunciados:" + str(exerciciosNumericos[index]))
            exercicioAtual = exerciciosNumericos[index]
            modo = "numerico"
            return (
                "```ansi\n \u001b[0;32m Caixa um numérica:\n"
                + exerciciosNumericos[index]["enunciado"]
                + "\u001b[0m\n```"
            )
    # Não achou? ache um da caixa 1 Teórica
    for index in range(len(exerciciosTeoricos)):
        print("Obter enunciado: exercício" + str(index))
        if exerciciosTeoricos[index][
            "caixa"
        ] == 1 and 2 <= spacedRepetitionUtilities.diferencaEmDias(
            exerciciosTeoricos[index]["ultimaAbertura"], time.time()
        ):
            exercicioAtual = exerciciosTeoricos[index]
            print("Obter enunciados:" + str(exerciciosTeoricos[index]))
            modo = "esperaTeorica"
            return (
                "```ansi\n \u001b[1;32m Caixa um teórica:\n"
                + exerciciosTeoricos[index]["enunciado"]
                + "\n(Envie qualquer mensagem para continuar)"
                + "\u001b[0m\n```"
            )
    # Não achou? Ache um da caixa 2 Numérica
    for index in range(len(exerciciosNumericos)):
        print("Obter enunciado: exercício" + str(index))
        if exerciciosNumericos[index][
            "caixa"
        ] == 2 and 4 <= spacedRepetitionUtilities.diferencaEmDias(
            exerciciosNumericos[index]["ultimaAbertura"], time.time()
        ):
            exercicioAtual = exerciciosNumericos[index]
            print("Obter enunciados:" + str(exerciciosNumericos[index]))
            modo = "numerico"
            return (
                "```ansi\n \u001b[2;33m Caixa dois numérica:\n"
                + exerciciosNumericos[index]["enunciado"]
                + "\u001b[0m\n```"
            )
    # Não achou? Ache um da caixa 2 Teórica
    for index in range(len(exerciciosTeoricos)):
        print("Obter enunciado: exercício" + str(index))
        if exerciciosTeoricos[index][
            "caixa"
        ] == 2 and 4 <= spacedRepetitionUtilities.diferencaEmDias(
            exerciciosTeoricos[index]["ultimaAbertura"], time.time()
        ):
            exercicioAtual = exerciciosTeoricos[index]
            print("Obter enunciados:" + str(exerciciosTeoricos[index]))
            modo = "esperaTeorica"
            return (
                "```ansi\n \u001b[1;33m Caixa dois teórica:\n"
                + exerciciosTeoricos[index]["enunciado"]
                + "\n(Envie qualquer mensagem para continuar)"
                + "\u001b[0m\n```"
            )
    # Não achou? Ache um da caixa 3 Numérica
    for index in range(len(exerciciosNumericos)):
        print("Obter enunciado: exercício" + str(index))
        if exerciciosNumericos[index][
            "caixa"
        ] == 3 and 7 <= spacedRepetitionUtilities.diferencaEmDias(
            exerciciosNumericos[index]["ultimaAbertura"], time.time()
        ):
            exercicioAtual = exerciciosNumericos[index]
            print("Obter enunciados:" + str(exerciciosNumericos[index]))
            modo = "numerico"
            return (
                "```ansi\n \u001b[0;34m Caixa três numérica(caixa final):\n"
                + exerciciosNumericos[index]["enunciado"]
                + "\u001b[0m\n```"
            )
    # Não achou? Ache um da caixa 3 Teórica
    for index in range(len(exerciciosTeoricos)):
        print("Obter enunciado: exercício" + str(index))
        if exerciciosTeoricos[index][
            "caixa"
        ] == 3 and 7 <= spacedRepetitionUtilities.diferencaEmDias(
            exerciciosTeoricos[index]["ultimaAbertura"], time.time()
        ):
            print("Obter enunciados:" + str(exerciciosTeoricos[index]))
            exercicioAtual = exerciciosTeoricos[index]
            modo = "esperaTeorica"
            return (
                "```ansi\n \u001b[1;34m Caixa três teórica(caixa final):\n"
                + exerciciosTeoricos[index]["enunciado"]
                + "\n(Envie qualquer mensagem para continuar)"
                + "\u001b[0m\n```"
            )
    # Não achou? Então não há exercícios
    return "Repetição espaçada finalizada"


def procedimentoDeEsperaTeorica():
    # Consiga as dependências
    global modo
    global exercicioAtual
    # Finalize o modo de espera teórico
    print("Espera teórica: A espera parou")
    modo = "teorico"
    return "A resposta era:\n" + exercicioAtual["gabarito"] + "\n você acertou(s/n)"


def procedimentoTeorico(resposta: str):
    # Consiga as dependências
    global modo
    global exercicioAtual
    exerciciosTeoricos = spacedRepetitionFileHandler.obterExerciciosTeoricos()
    # Tome o exercício teórico
    print("Finalização teórica:" + resposta)
    resposta = resposta.lower()
    if resposta.startswith("s"):
        # Salve o exercício no caso de acerto
        for index in range(len(exerciciosTeoricos)):
            if exercicioAtual == exerciciosTeoricos[index]:
                exerciciosTeoricos[index]["caixa"] += 1
                exerciciosTeoricos[index]["ultimaAbertura"] = int(time.time())
                print(
                    "Finalização teórica:"
                    + str(exercicioAtual)
                    + str(exerciciosTeoricos)
                )
                spacedRepetitionFileHandler.salvarExerciciosTeoricos(exerciciosTeoricos)
                break
        modo = "normal"
        exercicioAtual = {}
        return "Parabéns, você acertou!"
    elif resposta.startswith("n"):
        # Salve o exercício no caso de erro
        for index in range(len(exerciciosTeoricos)):
            if exercicioAtual == exerciciosTeoricos[index]:
                exerciciosTeoricos[index]["caixa"] += (
                    int(exerciciosTeoricos[index]["caixa"] == 0) - 1
                )
                exerciciosTeoricos[index]["erros"] += 1
                exerciciosTeoricos[index]["ultimaAbertura"] = int(time.time())
                print(
                    "Finalização teórica:"
                    + str(exercicioAtual)
                    + str(exerciciosTeoricos)
                )
                spacedRepetitionFileHandler.salvarExerciciosTeoricos(exerciciosTeoricos)
                break
        modo = "normal"
        exercicioAtual = {}
        return "Infelizmente você errou, tente novamente outro dia."
    else:
        # Insite o usuário a botar uma resposta válida no caso de não haver respondido corretamente
        return "Adicione uma resposta válida s ou n"


def procedimentoNumerico(resposta: str):
    print("Finalização Numérica" + resposta)
    # Verifique se a resposta é um número para início de conversa
    if not spacedRepetitionUtilities.checagemFlutuanteDeStrings(resposta):
        print("resposta não numérica")
        return "Adicione uma resposta numérica"
    numero = float(resposta)
    # Adquira as dependências
    global modo
    global exercicioAtual
    exerciciosNumericos = spacedRepetitionFileHandler.obterExerciciosNumericos()
    # Tome o exercício
    if spacedRepetitionUtilities.compararValores(
        exercicioAtual["gabarito"], numero, exercicioAtual["certeza"]
    ):
        # salve no caso de acerto
        for index in range(len(exerciciosNumericos)):
            if exercicioAtual == exerciciosNumericos[index]:
                exerciciosNumericos[index]["caixa"] += 1
                exerciciosNumericos[index]["ultimaAbertura"] = int(time.time())
                print(
                    "Finalização numérica:"
                    + str(exercicioAtual)
                    + str(exerciciosNumericos)
                )
                spacedRepetitionFileHandler.salvarExerciciosNumericos(
                    exerciciosNumericos
                )
                break
        modo = "normal"
        exercicioAtual = {}
        return "Parabéns, você acertou"
    else:
        # salve no caso de erro
        for index in range(len(exerciciosNumericos)):
            if exercicioAtual == exerciciosNumericos[index]:
                exerciciosNumericos[index]["caixa"] += (
                    int(exerciciosNumericos[index]["caixa"] == 0) - 1
                )
                exerciciosNumericos[index]["erros"] += 1
                print(
                    "Finalização numérica:"
                    + str(exercicioAtual)
                    + str(exerciciosNumericos)
                )
                exerciciosNumericos[index]["ultimaAbertura"] = int(time.time())
                spacedRepetitionFileHandler.salvarExerciciosNumericos(
                    exerciciosNumericos
                )
                break
        modo = "normal"
        erro = spacedRepetitionUtilities.erroPercentual(
            exercicioAtual["gabarito"], numero
        )
        exercicioAtual = {}
        return "infelizmente você errou por" + erro + ", tente novamente outro dia."


def adicaoNumerica(resposta: str):
    print("Adição numérica:" + resposta)
    # verifique se a resposta é de fato um número
    if not spacedRepetitionUtilities.checagemFlutuanteDeStrings(resposta):
        print("Adição numérica:resposta não numérica")
        return "Adicione um gabarito numérico válido."
    # Importe as dependências nescessárias
    global modo
    global exercicioAtual
    exerciciosNumericos = spacedRepetitionFileHandler.obterExerciciosNumericos()
    # salve o exercício
    enunciado = exercicioAtual["enunciado"]
    gabarito = float(resposta)
    certeza = spacedRepetitionUtilities.algarismosSignificativosEmString(resposta)
    spacedRepetitionFileHandler.adicionarExercicioNumerico(
        enunciado, gabarito, certeza, exerciciosNumericos
    )
    exercicioAtual = {}
    modo = "normal"
    print("Adição numérica: exercício adicionado.")
    return "Exercício(" + enunciado + ") adicionado."


def adicaoTeorica(resposta: str):
    print("Adição teórica:" + resposta)
    # importe as dependências nescessárias
    global modo
    global exercicioAtual
    exerciciosTeoricos = spacedRepetitionFileHandler.obterExerciciosTeoricos()
    # Salve o exercício
    enunciado = exercicioAtual["enunciado"]
    spacedRepetitionFileHandler.adicionarExercicioTeorico(
        enunciado, resposta, exerciciosTeoricos
    )
    modo = "normal"
    exercicioAtual = {}
    print("Adição teórica: exercício adicionado")
    return "Exercício(" + enunciado + ") adicionado."


def procedimentoDeDelecaoNumerica(resposta: str):
    print("Deleção numérica:" + resposta)
    # verifique se é um inteiro
    if not spacedRepetitionUtilities.checagemInteiraDeStrings(resposta):
        print("Deleção numérica:Resposta não numérica")
        return "Resposta não numérica"
    exerciciosNumericos = spacedRepetitionFileHandler.obterExerciciosNumericos()
    spacedRepetitionFileHandler.deletarExercicioNumericos(
        int(resposta), exerciciosNumericos
    )
    return "Exercício Deletado"


def procedimentoDeDelecaoTeorica(resposta: str):
    print("Deleção teórica:" + resposta)
    # verifique se é um inteiro
    if not spacedRepetitionUtilities.checagemInteiraDeStrings(resposta):
        print("Deleção teórica:Resposta não numérica")
        return "Resposta não numérica"
    # Delete o exercício de índice da resposta
    exercíciosTeóricos = spacedRepetitionFileHandler.obterExerciciosTeoricos()
    spacedRepetitionFileHandler.deletarExercicioTeorico(
        int(resposta), exercíciosTeóricos
    )
    return "Exercício Deletado"


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

# coding: utf-8
import time

import discord

import settings

# variáveis globais
# consiga o enunciado e exercício atual da repetição espaçada





def numericDeletion(answer,userName):
    print("Numeric Deletion:" + answer)
    if not spacedRepetitionUtilities.integerStringCheck(answer):
        print("Numeric deletion: the answer is not integer")
        return "Not a valid index."
    problems = spacedRepetitionFileHandler.getProblems()
    spacedRepetitionFileHandler.deleteNumericProblem(int(answer), problems,userName)
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

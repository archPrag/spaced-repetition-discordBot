# coding: utf-8
import time

import discord

import settings

import fileHandler
import problemHandler

import addition

import delletion

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
        userName = str(message.author)[1:]

        if message.author == client.user:
            return
        elif not fileHandler.userExists(userName):
            fileHandler.addUser(userName)

        state=fileHandler.getUserState(userName)
            
        if message.content.startswith("!Can"):
            # Reestart bots cache
            print("Canceled")
            state={'mode':'normal'}
            fileHandler.setUserState(state,userName)
            await message.channel.send("```ansi\n\u001b[0;31mCanceled\u001b[0m\n```")
        elif message.content.startswith("!Help") and state["mode"] == "normal":
            await message.channel.send(fileHandler.getHelp())
        elif message.content.startswith("!ListAll") and state["mode"] == "normal":
            for line in fileHandler.listProblems(userName):
                await message.channel.send(line)
        elif message.content.startswith("!List") and state["mode"] == "normal":
            # liste os exercícios incompletos
            for line in fileHandler.listUnfinishedProblems(userName):
                await message.channel.send(line)
        elif (
            message.content.startswith("!Exercise") and state["mode"] == "normal"
        ):
            await message.channel.send(problemHandler.findQuestionsInGreaterBoxes(0,userName))
        elif state["mode"] == "numeric":
            await message.channel.send(problemHandler.numeric(message.content,userName))
            await message.channel.send(problemHandler.findQuestionsInGreaterBoxes(0,userName))
        elif state["mode"] == "theoreticalWaiting":
            await message.channel.send(problemHandler.theoreticalWaiting(userName))
        elif state["mode"] == "theoretical":
            await message.channel.send(problemHandler.theoretical(message.content,userName))
            await message.channel.send(problemHandler.findQuestionsInGreaterBoxes(0,userName))
        elif message.content.startswith("!NA ") and state["mode"] == "normal":
            state = {
                "mode": "numericAddition",
                "problem": {
                    "question": message.content[4:],
                    "answer": 0,
                    "lastOpened": 0,
                    "box": 0,
                    "error": 0,
                },
            }
            fileHandler.setUserState(state,userName)
            await message.channel.send("What is the numeric answer?")
        elif state["mode"] == "numericAddition":
            await message.channel.send(addition.numeric(message.content,userName))
        elif message.content.startswith("!TA ") and state["mode"] == "normal":
            state = {
                "mode": "theoreticalAddition",
                "problem": {
                    "question": message.content[4:],
                    "answer": "",
                    "lastOpened": 0,
                    "box": 0,
                    "error": 0,
                },
            }
            fileHandler.setUserState(state,userName)
            await message.channel.send("What is the theoretical answer?")
        elif state["mode"] == "theoreticalAddition":
            await message.channel.send(addition.theoretical(message.content,userName))
        elif state["mode"] == "normal" and message.content.startswith("!ND "):
            await message.channel.send(delletion.numeric(message.content[4:],userName))
        elif state["mode"] == "normal" and message.content.startswith("!TD "):
            await message.channel.send(delletion.theoretical(message.content[4:],userName))
        print(userName)

    client.run(settings.DISCORD_API_SECRET)


if __name__ == "__main__":
    run()

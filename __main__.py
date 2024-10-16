# coding: utf-8
import time

import discord

import asyncio

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
        elif (
            message.content.startswith("!Exercise") and state["mode"] == "normal"
        ):
            dataTS=problemHandler.findQuestion(userName)
            if dataTS["image"]=="none":
                await message.channel.send(dataTS["message"])
            else:
                await message.channel.send(dataTS["message"],file=discord.File(dataTS["image"]))
        elif state["mode"] == "waiting":
            await message.channel.send(problemHandler.waiting(userName))
        elif state["mode"] == "problem":
            await message.channel.send(problemHandler.problemEnd(message.content,userName))
            await message.channel.send(problemHandler.findQuestion(userName))
        elif message.content.startswith("!PA ") and state["mode"] == "normal":
            if len(message.attachments)==0:
                path="none"
            else:
                url=message.attachments[0].url
                path=fileHandler.saveImg(url,userName)
            print("url path gotten")
            state = {
                "mode": "addition",
                "problem": {
                    "question": message.content[4:],
                    "imagePath": path,
                    "lastOpened": 0,
                    "box": 0,
                    "error": 0,
                },
            }
            fileHandler.setUserState(state,userName)
            await message.channel.send("What is the theoretical answer?")
        elif message.content.startswith("!MA ") and state["mode"] == "normal":
            await message.channel.send(addition.materialAdd(message.content[4:],userName))
        elif state["mode"] == "addition":
            await message.channel.send(addition.problem(message.content,userName))
        elif state["mode"] == "normal" and message.content.startswith("!MD "):
            await message.channel.send(delletion.materialDel(message.content[4:],userName))
        elif state["mode"] == "normal" and message.content.startswith("!PD "):
            await message.channel.send(delletion.problemDel(message.content[4:],userName))
        #listing must have a separated if block
        if message.content.startswith("!LAP") and state["mode"] == "normal":
            for line in fileHandler.listProblems(userName):
                await message.channel.send(line)
            time.sleep(2)
            for line in fileHandler.listMaterials(userName):
                await message.channel.send(line)
        elif message.content.startswith("!LM") and state["mode"] == "normal":
            for line in fileHandler.listMaterials(userName):
                await message.channel.send(line)
        elif message.content.startswith("!LP") and state["mode"] == "normal":
            # list unfinished problems
            for line in fileHandler.listUnfinishedProblems(userName):
                await message.channel.send(line)
        print(userName)
        print(message.attachments)
        print(message.content)

    client.run(settings.DISCORD_API_SECRET)


if __name__ == "__main__":
    run()

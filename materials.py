import fileHandler
import time
import numpy as np
import random
weightHalfLife=2.0*7*24*3600
materialsToSugest=4
def materialProbability(materials):
    global weightHalfLife
    currentTime=time.time()
    weightsPH=[]
    weight=0.0
    halfLifesPH=0.0
    for index in range(len(materials)):
        weightPH=0.0
        for chapter in range(len(materials[index]["chapterNames"])):
            halfLifesPH=(currentTime-materials[index]["lastOpened"][chapter])/weightHalfLife
            weight+=materials[index]["exercisePerChapter"][chapter]*(1-2**(-halfLifesPH))
        weightsPH.append(weightPH)
    return list(np.array(weightsPH)/sum(weightsPH))
def materialSubProbability(material):
    weightsPH=[]
    halfLifesPH=0.0
    currentTime=time.time()
    for chapter in range(len(material["chapterNames"])):
        halfLifesPH=(currentTime-material["lastOpened"][chapter])/weightHalfLife
        weightsPH.append(material["exercisePerChapter"][chapter]*(1-2**(-halfLifesPH)))
    return list(np.array(weightsPH)/sum(weightsPH))
def chooseIndexInProbabilityDistribution(distribution):
    dice=random.random()
    for index in range(len(distribution)):
        dice-=distribution[index]
        if dice<=0:
            return index
    return 0
def chooseDayMaterials(userName):
    global materialsToSugest
    materials=fileHandler.getMaterials(userName)
    distribution=[]
    chosenMaterial=0
    chosenChapter=0
    problem=0
    material={}
    materialString=""
    for index in range(materialsToSugest):
        distribution=materialProbability(materials)
        chosenMaterial=chooseIndexInProbabilityDistribution(distribution)
        distribution=materialSubProbability(materials[chosenMaterial])
        chosenChapter=chooseIndexInProbabilityDistribution(distribution)
        material=materials[chosenMaterial]
        problem=random.randint(1,material["exercisePerChapter"][chosenChapter])
        materials[chosenMaterial]["lastOpened"][chosenChapter]=time.time()
        materialString+=material["name"]+": "+material["chapterNames"][chosenChapter]+", problem "+str(problem)+"\n"
    fileHandler.saveMaterials(materials,userName)
    return materialString

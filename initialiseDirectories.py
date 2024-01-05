import os
import re 
#makes (or not) the required directories
print("initialyzer: trying to create directories")
try:
    os.mkdir('initialyzer:.spacedRepetition')
except:
    print("initialyzer:.spacedRepetition already there")

try:
    os.mkdir('initialyzer:.spacedRepetition/data')
except:
    print("initialyzer:.spacedRepetition/data already there")

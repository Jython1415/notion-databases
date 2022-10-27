import json
import os
from tkinter import getint

# main function
def main():
    folders = findFolders()
    listFolders(folders)
    selection = getIntInput("Select folder: ")
    moveToSubfolder(folders[selection])

# Find folders
def findFolders():
    folders = os.listdir()
    # Remove files that are on the "filesToIgnore" list
    for file in filesToIgnore:
        try:
            folders.remove(file)
        except ValueError:
            pass
    return folders
# Files in the project directly that should be ignored when looking for code
filesToIgnore = [".DS_Store", ".gitignore", ".git", "formulaViewer.py"]

# List folders
# List folder options to the user
def listFolders(folders):
    i = 0
    for folder in folders:
        print(str(i).zfill(2) + " " + folder)
        i += 1

# Get int selection from the user
def getIntInput(prompt, prompt2 = "Try again "):
    selection = input(prompt)
    try:
        return = int(selection)
    except ValueError:
        return getIntInput(prompt2, prompt2)

# Move to subfolder
# Returns cwd (current working directory) after the switch
def moveToSubfolder(folderName):
    os.chdir(os.getcwd() + "/" + folderName)
    return os.getcwd()

# Find the json files
files = os.listdir()
for file in files:
    if file[-4:] != "json":
        files.remove(file)

# Open the extract contents of the json files
jsonStrings = []
jsonDicts = []
for file in files:
    f = open(os.getcwd() + "/" + file, "r")
    lines = f.readlines()
    s = ""
    for line in lines:
        s += line
    jsonDicts.append(json.loads(s))

# Merge dictionaries
jsonDict = {}
for dict in jsonDicts:
    jsonDict = jsonDict | dict

# List formulas
formulas = jsonDict.get("formulas")
i = 0
for formula in formulas:
    print(str(i).zfill(2) + " " + formula.get("propertyTitle"))
    i += 1

# Select formula (user)
selection = int(input("Select formula: "))

# Print formula
formula = formulas[selection]
print(formula.get("propertyTitle"))
print(formula.get("description"))
print("\n" + formula.get("indentedLines"))
print("\n" + formula.get("raw"))

main()
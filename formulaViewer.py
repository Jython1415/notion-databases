import json
import os

# Files in the project directly that should be ignored when looking for code
filesToIgnore = [".DS_Store", ".gitignore", ".git", "formulaViewer.py"]

# Find folders
folders = os.listdir()
# Remove files that are on the "filesToIgnore" list
for file in filesToIgnore:
    try:
        folders.remove(file)
    except ValueError:
        pass

# List folder options to the user
i = 0
for folder in folders:
    print(str(i).zfill(2) + " " + folder)
    i += 1

# Get selection from the user
selection = int(input("Select folder: "))

# Move to the directly
os.chdir(os.getcwd() + "/" + folders[selection])
dir = os.getcwd()

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
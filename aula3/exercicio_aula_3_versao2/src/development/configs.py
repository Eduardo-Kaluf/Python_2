import os

current = os.getcwd()

for i, x, y in os.walk(current):
    if i[-5:] == "files":
        FILES = i
        break

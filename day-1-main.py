# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#open file
moose_puzzle_input = open("day-1-puzzle-input-moose.txt", "r")

#read file
data = moose_puzzle_input.read()

data_into_list = data.split('\n')

highest_calories = 0
x = 0
for i in data_into_list:
    if i == "":
        x = 0
        continue
    x += int(i)
    if highest_calories < x:
        highest_calories = x
print(highest_calories)

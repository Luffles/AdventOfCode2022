# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#open file
moose_puzzle_input = open("day-1-puzzle-input-moose.txt", "r")

#read file
data = moose_puzzle_input.read()

data_into_list = data.split('\n')

highest_calories = [0, 0, 0]
x = 0
for i in data_into_list:
    if i != "":
        x += int(i)

    else:
        if x > highest_calories[0]:
            highest_calories[0] = x
        elif x > highest_calories[1]:
            highest_calories[1] = x
        elif x > highest_calories[2]:
            highest_calories[2] = x
        x = 0
print(highest_calories[0], '\n', highest_calories[1], '\n', highest_calories[2])
print(sum(highest_calories))

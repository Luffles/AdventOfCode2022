# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#open file
moose_puzzle_input = open("day-1-puzzle-input-moose.txt", "r")

#read file

calories = 0
calories_list = []
for line in moose_puzzle_input.readlines():
    if line == "\n":
        calories_list.append(calories)
        calories = 0
    else:
        calories += int(line)
sum_top_calories = sum(sorted(calories_list)[-3:])
print(sum_top_calories)


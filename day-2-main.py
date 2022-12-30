def main():
    print("Day 2 Advent")
    moose_puzzle_input = open('day-2-moose.txt', 'r')
    moose_puzzle_input2 = open('day-2-moose.txt', 'r')
    task_1(moose_puzzle_input)
    task_2(moose_puzzle_input2)


def task_1(file):
    score = 0
    total_score = 0
    opponent_letter = ''
    player_letter = ''
    opponent_number = 0
    player_number = 0
    for line in file.readlines():
        opponent_letter = line[0]
        player_letter = line[2]
        if opponent_letter == 'A':
            opponent_number = 1
        elif opponent_letter == 'B':
            opponent_number = 2
        elif opponent_letter == 'C':
            opponent_number = 3
        if player_letter == 'X':
            player_number = 1
        elif player_letter == 'Y':
            player_number = 2
        elif player_letter == 'Z':
            player_number = 3

        if opponent_number == player_number:
            score = player_number + 3
        elif opponent_number == 1 and player_number == 2:
            score = player_number + 6
        elif opponent_number == 1 and player_number == 3:
            score = player_number
        elif opponent_number == 2 and player_number == 1:
            score = player_number
        elif opponent_number == 2 and player_number == 3:
            score = player_number + 6
        elif opponent_number == 3 and player_number == 1:
            score = player_number + 6
        elif opponent_number == 3 and player_number == 2:
            score = player_number
        total_score += score

    print(total_score)


def task_2(file):
    score = 0
    total_score = 0
    opponent_letter = ''
    player_result = ''
    opponent_number = 0
    player_number = 0
    for line in file.readlines():
        opponent_letter = line[0]
        player_result = line[2]
        if opponent_letter == 'A':
            opponent_number = 1
        elif opponent_letter == 'B':
            opponent_number = 2
        elif opponent_letter == 'C':
            opponent_number = 3
        if player_result == 'X' and opponent_number == 1:
            player_number = 3
        elif player_result == 'X' and opponent_number == 2:
            player_number = 1
        elif player_result == 'X' and opponent_number == 3:
            player_number = 2
        elif player_result == 'Y':
            player_number = opponent_number
        elif player_result == 'Z' and opponent_number == 1:
            player_number = 2
        elif player_result == 'Z' and opponent_number == 2:
            player_number = 3
        elif player_result == 'Z' and opponent_number == 3:
            player_number = 1

        if opponent_number == player_number:
            score = player_number + 3
        elif opponent_number == 1 and player_number == 2:
            score = player_number + 6
        elif opponent_number == 1 and player_number == 3:
            score = player_number
        elif opponent_number == 2 and player_number == 1:
            score = player_number
        elif opponent_number == 2 and player_number == 3:
            score = player_number + 6
        elif opponent_number == 3 and player_number == 1:
            score = player_number + 6
        elif opponent_number == 3 and player_number == 2:
            score = player_number
        total_score += score
    print(total_score)


if __name__ == "__main__":
    main()

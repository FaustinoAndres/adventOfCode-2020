def readFile():

    f = open("day3_data.txt", "r")
    lines = f.readlines()

    puzzle_input = list()

    for line in lines:
        puzzle_input.append([char for char in line if char != '\n'])

    return puzzle_input



def main():

    right = 3
    tree = '#'

    tree_counter = 0

    puzzle_input = readFile()
    length_pattern = len(puzzle_input[0])
    length_forest = len(puzzle_input)

    count_pattern = 0

    for i in range(length_forest):

        if puzzle_input[i][count_pattern] == tree:
            tree_counter+=1

        count_pattern += right
        if count_pattern >= length_pattern:
            count_pattern -= length_pattern

    print(tree_counter)



if __name__ == "__main__":

    main()
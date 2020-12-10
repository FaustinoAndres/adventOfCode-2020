def readFile():

    f = open("day3_data.txt", "r")
    lines = f.readlines()
    
    puzzle_input = list()
    
    for line in lines:
        puzzle_input.append([char for char in line if char != '\n'])

    return puzzle_input


def count_trees(right, down, puzzle_input):

    tree = '#'
    tree_counter = 0

    length_pattern = len(puzzle_input[0])
    length_forest = len(puzzle_input)

    count_pattern = 0

    for i in range(0, length_forest, down):

        if puzzle_input[i][count_pattern] == tree:
            tree_counter+=1

        count_pattern += right
        if count_pattern >= length_pattern:
            count_pattern -= length_pattern

    return tree_counter

def main():

    puzzle_input = readFile()
    
    # Right 1, down 1.
    # Right 3, down 1. (This is the slope you already checked.)
    # Right 5, down 1.
    # Right 7, down 1.
    # Right 1, down 2.

    pairs = [[1,1], [3,1], [5,1], [7,1], [1,2]]

    result = 1

    for pair in pairs:
        
        result *= (count_trees(pair[0], pair[1], puzzle_input))

    print(result)

if __name__ == "__main__":

    main()
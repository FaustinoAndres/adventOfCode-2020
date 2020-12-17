def readFile():

    f = open("Day8_data.txt", "r")
    lines = f.readlines()

    input = list()

    for line in lines:
        input.append(line.split())

    return input

def program(input_instructions):

    index = 0
    accumulator = 0
    appears = []

    while True:

        if index not in appears:
            appears.append(index)
            instruction = input_instructions[index][0]
            value = int(input_instructions[index][1])
            if instruction == 'acc':
                accumulator += value
                index += 1
            elif instruction == 'nop':
                index += 1
            elif instruction == 'jmp':
                index += value

        else:
            break

    print(accumulator)

    return accumulator

def main():

    input_instructions = readFile()
    #print(input_instructions)
    accumulator = program(input_instructions)

if __name__=='__main__':

    main()




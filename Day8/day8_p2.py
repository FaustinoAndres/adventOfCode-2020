def readFile():

    f = open("Day8_data.txt", "r")
    lines = f.readlines()

    input = list()

    for line in lines:
        input.append(line.split())

    return input

def program_infty_loop(input_instructions):

    index = 0
    accumulator = 0
    appears = []
    appear_nop_jmp = []

    while True:

        if index not in appears:
            appears.append(index)
            instruction = input_instructions[index][0]
            value = int(input_instructions[index][1])
            if instruction == 'acc':
                accumulator += value
                index += 1
            elif instruction == 'nop':
                appear_nop_jmp.append(['jmp', index])
                index += 1
            elif instruction == 'jmp':
                appear_nop_jmp.append(['nop', index])
                index += value

        else:
            break

    infinite_loop = appears
    return infinite_loop, appear_nop_jmp

def program(input_instructions):


    index = 0
    accumulator = 0
    appears = []
    check = True

    while check :

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
            check = False

        if index >= len(input_instructions) - 1:

            check = True
            return accumulator, check, appears

    return accumulator, check, appears


def main():

    input_instructions = readFile()
    infinite_loop, appear_nop_jmp = program_infty_loop(input_instructions)

    for i in range(len(input_instructions)):

        if input_instructions[i][0] == 'jmp':
            input_instructions[i][0] = 'nop'

            acc, check, appears = program(input_instructions)
            if check:
                print(acc)
                break
            input_instructions[i][0] = 'jmp'

        elif input_instructions[i][0] == 'nop':
            input_instructions[i][0] = 'jmp'
            acc, check, appears = program(input_instructions)
            if check:
                print(acc)
                break
            input_instructions[i][0] = 'nop'


if __name__=='__main__':

    main()




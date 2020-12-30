def readFile():

    f = open('data.txt', 'r')
    lines = f.readlines()
    instructions = list()
    for line in lines:
        instructions.append((line[:-1]))
    return instructions

def read_instruction(raw_instruction):

    instruction = ''
    value = ''
    for char in raw_instruction:
        if char.isdigit():
            value += char
        else:
            instruction += char

    return instruction, int(value)

def move_global(instructions, x=0, y=0, orientation='E'):

    for raw_instruction in instructions:
        instruction, value = read_instruction(raw_instruction)
        if instruction in ['L', 'R']:
            orientation = rotate(instruction, value, orientation)
        elif instruction == 'F':
            x, y = forward(value, orientation, x, y)
        elif instruction in ['N', 'W', 'S', 'E']:
            x, y = move(instruction, value, x, y)

    return manhattan_distance(x,y)

def move(instruction, value, x, y):

    if instruction == 'W':
        x -= value
    elif instruction == 'E':
        x += value
    elif instruction == 'N':
        y += value
    elif instruction == 'S':
        y -= value

    return x, y

def forward(value, orientation, x, y):

    if orientation == 'W':
        x -= value
    elif orientation == 'E':
        x += value
    elif orientation == 'N':
        y += value
    elif orientation == 'S':
        y -= value

    return x, y

def rotate(instruction, angle, orientation):

    directions = ['N', 'W', 'S', 'E']
    position = directions.index(orientation)
    new_direction = None
    value = int(angle/90)
    if instruction == 'R':
        position -= value
    elif instruction == 'L':
        position = (position + value) % 4
    new_direction = directions[position]

    return new_direction

def manhattan_distance(x, y, xi=0, yi=0):

    distance = abs(x-xi) + abs(y-yi)
    return distance

def main():

    instructions = readFile()
    distance = move_global(instructions)
    print(distance)

if __name__ == '__main__':

    main()
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

def move_global(instructions, x=0, y=0, x_wp=10, y_wp=1):

    print(instructions[:5])

    for raw_instruction in instructions:
        instruction, value = read_instruction(raw_instruction)
        if instruction in ['L', 'R']:
            x_wp, y_wp = rotate(instruction, value,x, y, x_wp, y_wp)
        elif instruction == 'F':
            x, y, x_wp, y_wp = forward(value, x, y, x_wp, y_wp)
        elif instruction in ['N', 'W', 'S', 'E']:
            x_wp, y_wp = move(instruction, value, x_wp, y_wp)

    return manhattan_distance(x,y)

def move(instruction, value, x_wp, y_wp):

    if instruction == 'W':
        x_wp -= value
    elif instruction == 'E':
        x_wp += value
    elif instruction == 'N':
        y_wp += value
    elif instruction == 'S':
        y_wp -= value

    return x_wp, y_wp

def forward(value, x, y, x_wp, y_wp):

    delta_x = x_wp - x
    delta_y = y_wp - y
    x_times = value*abs(delta_x)
    y_times = value*abs(delta_y)

    if delta_x > 0:
        x += x_times
        x_wp += x_times
    elif delta_x < 0:
        x -= x_times
        x_wp -= x_times

    if delta_y > 0:
        y += y_times
        y_wp += y_times
    elif delta_y < 0:
        y -= y_times
        y_wp -= y_times

    return x, y, x_wp, y_wp

def rotate(instruction, angle, x, y, x_wp, y_wp):

    x_aux = x_wp - x
    y_aux = y_wp - y
    value = int(angle/90)

    if instruction == 'R':
        if value == 1:
            x_aux, y_aux = y_aux, -x_aux
        elif value == 2:
            x_aux, y_aux = -x_aux, -y_aux
        elif value == 3:
            x_aux, y_aux = -y_aux, x_aux
    elif instruction == 'L':
        if value == 1:
            x_aux, y_aux = -y_aux, x_aux
        elif value == 2:
            x_aux, y_aux = -x_aux, -y_aux
        elif value == 3:
            x_aux, y_aux = y_aux, -x_aux

    x_wp = x_aux + x
    y_wp = y_aux + y
    return x_wp, y_wp

def manhattan_distance(x, y, xi=0, yi=0):

    distance = abs(x-xi) + abs(y-yi)
    return distance

def main():

    instructions = readFile()
    distance = move_global(instructions)
    print(distance)

if __name__ == '__main__':

    main()
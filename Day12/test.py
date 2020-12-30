COMPASS = ['E', 'S', 'W', 'N']
INSTRUCTIONS = open("data.txt", "r").read().splitlines()

def returnInstruction(ins):
    return ins[0], int(ins[1:])

def movePosition(positions, facing, instruction):
    direction, num = returnInstruction(instruction)
    direction = COMPASS[facing] if direction == 'F' else direction
    opposite = (COMPASS.index(direction) + 2) % 4
    opValue = positions[COMPASS[opposite]]  

    if opValue > 0:
        if num > opValue:
            positions[COMPASS[opposite]] = 0
            positions[direction] += (num - opValue) 
        else:
            positions[COMPASS[opposite]] = opValue - num 
    else:
        positions[direction] += num    
    return positions

# solution one 
def manhattanDistanceNoWaypoint():
    facing = 0
    positions = {
        'N': 0,
        'S': 0,
        'E': 0,
        'W': 0
    }

    for instruction in INSTRUCTIONS:
        direction, num = returnInstruction(instruction)
        if direction == 'L' or direction == 'R':
            if direction == 'L':
                facing = (facing + ((360 - num) // 90)) % 4
            else:
                facing = ((facing + ((num // 90) % 4)) % 4)
        else:
            positions = movePosition(positions, facing, instruction)

    return sum(positions.values())

# solution two
def manhattanDistanceWaypoint():
    ship = [0, 0]  
    waypointCoords = [10, 1]

    for instruction in INSTRUCTIONS:
        direction, num = returnInstruction(instruction)

        if direction == 'F':
            ship[0] += num * waypointCoords[0]
            ship[1] += num * waypointCoords[1]
        elif direction == 'L' or direction == 'R':
            pos = -1 if direction == 'L' else 1
            degree = ((num // 90) * pos) % 4
            if degree == 1:
                waypointCoords = [waypointCoords[1], -waypointCoords[0]]
            elif degree == 2:
                waypointCoords = [-waypointCoords[0], -waypointCoords[1]]
            elif degree == 3:
                waypointCoords = [-waypointCoords[1], waypointCoords[0]]
        elif direction == 'N' or direction == 'S':
            pos = 1 if direction == 'N' else -1
            waypointCoords[1] += num * pos 
        else:
            pos = 1 if direction == 'E' else -1
            waypointCoords[0] += num * pos            

    return abs(ship[0]) + abs(ship[1])    


print(manhattanDistanceNoWaypoint())
print(manhattanDistanceWaypoint())
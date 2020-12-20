def readFile():

    f = open('data.txt', 'r')
    lines = f.readlines()

    seats = list()

    for line in lines:
        seats.append([char for char in line if char != '\n'])

    return seats

def right(row, col, seats):

    count = 0
    for j in range(col + 1, len(seats[0])):
        if seats[row][j] == '#':
            count += 1
            break
        elif seats[row][j] == 'L':
            break
    return count

def left(row, col, seats):

    count = 0
    for j in range(col - 1, -1, -1):
        if seats[row][j] == '#':
            count += 1
            break
        elif seats[row][j] == 'L':
            break
    return count

def up(row, col, seats):

    count = 0
    for i in range(row - 1, -1, -1):
        if seats[i][col] == '#':
            count += 1
            break
        elif seats[i][col] == 'L':
            break
    return count

def down(row, col, seats):

    count = 0
    for i in range(row + 1, len(seats)):
        if seats[i][col] == '#':
            count += 1
            break
        elif seats[i][col] == 'L':
            break
    return count

def right_up(row, col, seats):

    count = 0
    for j in range(col + 1, len(seats[0])):
        row -= 1
        if row < 0:
            break
        if seats[row][j] == '#' and row >= 0:
            count += 1
            break
        elif seats[row][j] == 'L' and row >= 0:
            break
    return count

def left_up(row, col, seats):

    count = 0
    for j in range(col - 1, -1, -1):
        row -= 1
        if row < 0:
            return 0
        if seats[row][j] == '#' and row >= 0:
            count += 1
            break
        elif seats[row][j] == 'L' and row >= 0:
            break
    return count

def right_down(row, col, seats):

    count = 0
    for j in range(col + 1, len(seats[0])):
        row += 1
        if row >= len(seats):
            return 0
        if seats[row][j] == '#' and row < len(seats):
            count += 1
            break
        elif seats[row][j] == 'L' and row < len(seats):
            break
    return count

def left_down(row, col, seats):

    count = 0
    for j in range(col - 1, -1, -1):
        row += 1
        if row >= len(seats):
            return 0
        if seats[row][j] == '#' and row < len(seats):
            count += 1
            break
        elif seats[row][j] == 'L' and row < len(seats):
            break
    return count

def occupied_seat(seats):

    seats_future = [[None for _ in seats[0]] for _ in seats]

    for i in range(len(seats_future)):
        for j in range(len(seats_future[0])):
            if seats[i][j] == '.':
                seats_future[i][j] = '.'
            else:
                counter = 0
                if (i==0 and j==0):
                    counter += right(i,j,seats) + down(i,j,seats) + right_down(i,j,seats)
                elif (i==0 and j==len(seats_future[0])-1):
                    counter += left(i,j,seats) + down(i,j,seats) + left_down(i,j,seats)
                elif (i==len(seats_future)-1 and j==0):
                    counter += up(i,j,seats) + right(i,j,seats) + right_up(i,j,seats)
                elif (i==len(seats_future)-1 and j == len(seats_future[0])-1):
                    counter += left(i,j,seats) + up(i,j,seats) + left_up(i,j,seats)
                elif (i==0 and (j!=len(seats_future[0])-1 and j!=0)):
                    counter += right(i,j,seats) + down(i,j,seats) + right_down(i,j,seats) + left(i,j,seats) + left_down(i,j,seats)
                elif (i==len(seats_future)-1 and (j!=0 or j!=len(seats_future[0])-1)):
                    counter += right(i,j,seats) + left(i,j,seats) + up(i,j,seats) + right_up(i,j,seats) + left_up(i,j,seats)
                elif (j==0 and (i!=0 and i!=len(seats_future)-1)):
                    counter += up(i,j,seats) + down(i,j,seats) + right(i,j,seats) + right_down(i,j,seats) + right_up(i,j,seats)
                elif (j==len(seats_future[0])-1 and (i!=0 and i!=len(seats_future)-1)):
                    counter += up(i,j,seats) + down(i,j,seats) + left(i,j,seats) + left_down(i,j,seats) + left_up(i,j,seats)
                else:
                    counter += up(i,j,seats) + down(i,j,seats) + left(i,j,seats) + left_down(i,j,seats) + left_up(i,j,seats) + right(i,j,seats) + right_down(i,j,seats) + right_up(i,j,seats)

                if seats[i][j] == 'L' and counter == 0:
                    seats_future[i][j] = '#'
                elif seats[i][j] == '#' and counter >= 5:
                    seats_future[i][j] = 'L'
                else:
                    seats_future[i][j] = seats[i][j]
    return seats_future

def get_number_occuped_seat(seats):

    count = 0
    for line in seats:
        for seat in line:
            if seat == '#': count += 1

    return count

def main():

    seats = readFile()
    seats_future = occupied_seat(seats)

    while seats != seats_future:

        seats = seats_future
        seats_future = occupied_seat(seats)

    print(get_number_occuped_seat(seats_future))

if __name__ == '__main__':

    main()

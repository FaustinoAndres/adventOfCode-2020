def readFile():

    f = open("day5_data.txt", "r")
    lines = f.readlines()
    boarding_passes = list()

    for line in lines:
        boarding_passes.append([char for char in (line[:-1])])

    return boarding_passes

def seat_search(boarding_pass, rows, columns):

    init_row = 0
    finish_row = rows - 1
    init_col = 0
    finish_col = columns - 1
    #middle_row = int(columns/2)

    for char in boarding_pass[:7]:
        middle_row = int((finish_row-init_row)/2) + 1
        if char == 'F':
            finish_row = finish_row - middle_row
        elif char == 'B':
            init_row = init_row + middle_row

    row = init_row
        #print(init_row, finish_row)
    for char in boarding_pass[7:]:
        middle_col = int((finish_col-init_col)/2) + 1
        if char == 'L':
            finish_col = finish_col - middle_col
        elif char == 'R':
            init_col = init_col + middle_col

    col = init_col

    return row, col


def seat_people(seats, boarding_passes, rows, columns):

    seat_ids = list()

    for boarding_pass in boarding_passes:
        row, col = seat_search(boarding_pass, rows, columns)
        seats[row][col] = True
        seat_id = row*8 + col
        seat_ids.append(seat_id)

    highest_seat_id = max(seat_ids)

    print(highest_seat_id)


def main():

    rows = 128
    columns = 8
    column_seats = [False for j in range(8)]
    seats = [column_seats for i in range(128)]
    boarding_passes = readFile()
    seat_people(seats, boarding_passes, rows, columns)

if __name__ == '__main__':

    main()
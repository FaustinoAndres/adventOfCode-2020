def readFile():

    f = open('data.txt', 'r')
    lines = f.readlines()

    seats = list()

    for line in lines:
        seats.append([char for char in line if char != '\n'])

    return seats


def occupied_seat(seats):

    seats_future = [[None for _ in seats[0]] for _ in seats]

    for i in range(len(seats_future)):
        for j in range(len(seats_future[0])):
            if seats[i][j] == '.':
                seats_future[i][j] = '.'
            else:
                counter = 0
                if (i==0 and j==0):
                    counter += int(seats[i][j+1]=='#') + int(seats[i+1][j+1]=='#') + int(seats[i+1][j]=='#')
                elif (i==0 and j==len(seats_future[0])-1):
                    counter += int(seats[i][j-1]=='#') + int(seats[i+1][j-1]=='#') + int(seats[i+1][j]=='#')
                elif (i==len(seats_future)-1 and j==0):
                    counter += int(seats[i-1][j]=='#') + int(seats[i-1][j+1]=='#') + int(seats[i][j+1]=='#')
                elif (i==len(seats_future)-1 and j == len(seats_future[0])-1):
                    counter += int(seats[i-1][j-1]=='#') + int(seats[i-1][j]=='#') + int(seats[i][j-1]=='#')
                elif (i==0 and (j!=len(seats_future[0])-1 and j!=0)):
                    counter += int(seats[i][j+1]=='#') + int(seats[i+1][j+1]=='#') + int(seats[i+1][j]=='#') + int(seats[i+1][j-1]=='#') + int(seats[i][j-1]=='#')
                elif (i==len(seats_future)-1 and (j!=0 or j!=len(seats_future[0])-1)):
                    counter += int(seats[i-1][j-1]=='#') + int(seats[i-1][j]=='#') + int(seats[i-1][j+1]=='#')
                    counter += int(seats[i][j-1]=='#') + int(seats[i][j+1]=='#')
                elif (j==0 and (i!=0 and i!=len(seats_future)-1)):
                    counter += int(seats[i-1][j]=='#') + int(seats[i-1][j+1]=='#')
                    counter += int(seats[i][j+1]=='#')
                    counter += int(seats[i+1][j]=='#') + int(seats[i+1][j+1]=='#')
                elif (j==len(seats_future[0])-1 and (i!=0 and i!=len(seats_future)-1)):
                    counter += int(seats[i-1][j-1]=='#') + int(seats[i-1][j]=='#')
                    counter += int(seats[i][j-1]=='#')
                    counter += int(seats[i+1][j-1]=='#') + int(seats[i+1][j]=='#')
                else:
                    counter += int(seats[i-1][j-1]=='#') + int(seats[i-1][j]=='#') + int(seats[i-1][j+1]=='#')
                    counter += int(seats[i][j-1]=='#') + int(seats[i][j+1]=='#')
                    counter += int(seats[i+1][j-1]=='#') + int(seats[i+1][j]=='#') + int(seats[i+1][j+1]=='#')

                if seats[i][j] == 'L' and counter == 0:
                    seats_future[i][j] = '#'
                elif seats[i][j] == '#' and counter >= 4:
                    seats_future[i][j] = 'L'
                else:
                    seats_future[i][j] = seats[i][j]
    return seats_future

def get_number_occuped_seat(seats):

    count = 0
    for line in seats:
        for i in line:
            if i == '#': count += 1

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

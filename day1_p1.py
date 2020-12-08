
def readFile():

    f = open("day1_p1_data.txt", "r")
    lines = f.readlines()
    input_numbers = list()
    for line in lines:
        input_numbers.append(int(line[:-1]))
    return input_numbers

def main():

    objective = 2020
    input_numbers = readFile()
    complement = dict()

    for number in input_numbers:
        complement[number] = True
        to_find = objective - number

        if to_find in complement:

            print(to_find*number)
            break

if __name__ == '__main__':

    main()
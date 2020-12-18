def readFile():

    f = open("Day9_data.txt", "r")
    lines = f.readlines()

    input = list()

    for line in lines:
        input.append(int(line.rstrip('\n')))

    return input

def XMAS(file):

    preamble = file[:25]
    print(preamble)
    print(len(preamble))

    for next_number in file[25:]:
        complement = dict()
        check = False
        for number in preamble:
            complement[number] = True
            to_find = next_number - number
            if to_find in complement:
                check = True

        preamble.pop(0)
        preamble.append(next_number)

        if check == False:
            return next_number


def main():

    input_file = readFile()
    fail_number = XMAS(input_file)
    print(fail_number)

if __name__ == '__main__':

    main()
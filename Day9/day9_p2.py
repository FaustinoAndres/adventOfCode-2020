def readFile():

    f = open("Day9_data.txt", "r")
    lines = f.readlines()

    input = list()

    for line in lines:
        input.append(int(line.rstrip('\n')))

    return input

def XMAS(file):

    preamble = file[:25]

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

def encryption_weakness(invalid_number, file):

    numbers = file[:(file.index(invalid_number))]

    for i in range(len(numbers)):

        sumandos = []

        init = numbers[i]
        suma = numbers[i] + numbers[i+1]
        sumandos.append(init)
        sumandos.append(numbers[i+1])
        i = i+1
        while suma < invalid_number:
            i = i + 1
            suma += numbers[i]
            sumandos.append(numbers[i])
            # print(suma)
            if suma == invalid_number:

                largest = max(sumandos)
                smallest = min(sumandos)
                return largest + smallest


def main():

    input_file = readFile()
    fail_number = XMAS(input_file)
    key = encryption_weakness(fail_number, input_file)
    print(key)

if __name__ == '__main__':

    main()
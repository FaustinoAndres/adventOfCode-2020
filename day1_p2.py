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

    for number1 in input_numbers:
        for number2 in input_numbers:
            for number3 in input_numbers:
                if number1 + number2 + number3 == objective:
                    print(number1*number2*number3)
                    break

if __name__ == '__main__':

    main()
checked = {}

def readFile():

    f = open("day10_data.txt", "r")
    lines = f.readlines()

    output_joltage = [0]

    for line in lines:
        output_joltage.append(int(line.rstrip('\n')))

    output_joltage.sort()
    output_joltage.append(output_joltage[-1] + 3)

    return output_joltage


def all_ways(output_joltage, index = 0):

    global checked

    if index == len(output_joltage) - 1:
        return 1

    if index in checked:
        return checked[index]

    total_ways = 0
    for i in range(index+1, len(output_joltage)):
        if output_joltage[i] - output_joltage[index] <= 3:
            total_ways += all_ways(output_joltage, i)

    checked[index] = total_ways
    return total_ways

def main():

    output_joltage = readFile()
    print(all_ways(output_joltage))

if __name__ == '__main__':

    main()

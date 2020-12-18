def readFile():

    f = open("day10_data.txt", "r")
    lines = f.readlines()

    output_joltage = [0]

    for line in lines:
        output_joltage.append(int(line.rstrip('\n')))

    output_joltage.sort()
    output_joltage.append(output_joltage[-1] + 3)

    return output_joltage


def jolt_differences(output_joltage):

    jolt_diff_1 = 0
    jolt_diff_3 = 0

    for i in range(len(output_joltage)-1):

        diff = output_joltage[i+1] - output_joltage[i]

        if diff == 1:
            jolt_diff_1 +=1
        elif diff == 3:
            jolt_diff_3 += 1

    return jolt_diff_1*jolt_diff_3

def main():

    output_joltage = readFile()
    print(jolt_differences(output_joltage))


if __name__ == '__main__':

    main()

def readFile():

    f = open("Day2_data.txt", "r")
    lines = f.readlines()
    
    input_password = list()
    
    for line in lines:
        input_password.append(line.split())
    
    return input_password

def clean_input_password(input_password):

    clean_input = list()
    for element in input_password:

        clean_data = [element[0].split("-"), element[1].rstrip(":"), element[2]]
        clean_input.append(clean_data)

    return clean_input

def counter(clean_data):

    count = 0
    for data in clean_data:
        count_char = data[2].count(data[1])
        if int(data[0][0]) <= count_char <= int(data[0][1]):
            count += 1

    return count

def main():

    clean_input = clean_input_password(readFile())
    count = counter(clean_input)
    print(count)

if __name__ == "__main__":

    main()
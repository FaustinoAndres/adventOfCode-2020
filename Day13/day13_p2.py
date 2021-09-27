import math

def readFile():

    f = open('data.txt', 'r')
    lines = f.readlines()
    f.close()
    sequence = lines[1].rstrip('\n').split(',')
    return sequence

def mod_inverse(a, m):
    """
    https://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/
    """
    for x in range(1, m):
        if (((a%m) * (x%m)) % m == 1):
            return x
    return -1


def main():

    sequence = readFile()

    #Inspired by the explanation of the following link
    #https://www.youtube.com/watch?v=3oVWRPzT2JA
    #Other sources consulted
    #Apply Chinese remainder theorem
    #https://en.wikipedia.org/wiki/Chinese_remainder_theorem

    bus_ids_info = []
    fullProduct = 1
    for index, item in enumerate(sequence):
        if item != 'x':
            id = int(item)
            #each bus -> (t===id-index mod(id), id, index)
            bus_ids_info.append(((id-index)%id, id, index))
            fullProduct *= id

    total = 0

    for mod, id, index in bus_ids_info:
        partialProduct = int(fullProduct / id)
        inverse = mod_inverse(partialProduct, id)
        term = inverse * partialProduct * mod
        total += term

    print(total % fullProduct)


if __name__ == '__main__':

    main()


import math

def readFile():

    f = open('data.txt', 'r')
    lines = f.readlines()
    f.close()

    earliest_timestamp = int(lines[0].rstrip('\n'))
    bus_ids = [int(i) for i in lines[1].rstrip('\n').split(',') if i!='x']

    return earliest_timestamp, bus_ids


def main():

    earliest_timestamp, bus_ids = readFile()
    bus = None
    minimum = math.inf

    for bus_id in bus_ids:

        div = earliest_timestamp / bus_id
        if type(div) != 'int':
            time_forward = (int(div)+1)*bus_id - earliest_timestamp
            if time_forward < minimum:
                minimum = time_forward
                bus = bus_id

        else:
            bus = bus_id
            break

    print(bus*minimum)

if __name__ == '__main__':

    main()
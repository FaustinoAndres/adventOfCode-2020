bag_set = set()

def readFile():

    f = open("day7_data.txt", "r")
    lines = f.readlines()
    rules = list()
    for line in lines:
        rules.append(line[:-1])
    return rules

def split_rule(rule):

    bags = rule.split(' bags contain ')
    key = bags[0]
    bags = bags[1].rstrip('.').split(',')
    value = {}
    for bag in bags:
        bag = bag.lstrip(' ').rstrip('bag').rstrip('bags').rstrip(' ')
        value[bag[2:]] = int(bag[0])

    return key, value

def hash_map_rules(rules):

    map_rules = {}
    for rule in rules:
        if 'no other bags' in rule:
            bags = rule.split(' bags contain ')
            key = bags[0]
            value = 0
        else:
            key, value = split_rule(rule)

        map_rules[key] = value

    return map_rules

def search(map_rules, wanted):

    global bag_set

    for bag, sub_bags in map_rules.items():
        if sub_bags == 0:
            pass
        else:
            try:
                sub_bags[wanted]
                if bag not in bag_set:
                    bag_set.add(bag)
                    search(map_rules, wanted=bag)
            except:
                pass

def main():

    rules = readFile()
    map_rules = hash_map_rules(rules)
    search(map_rules, 'shiny gold')
    print(len(bag_set))


if __name__ == '__main__':

    main()
import string

def readFile():

    f = open("day4_data.txt", "r")
    lines = f.readlines()

    passport_input = list()
    user_passport = list()

    for line in lines:

        if line != '\n':
            for user_passport_field in line.rstrip('\n').split(' '):
                user_passport.append(user_passport_field)
        elif line == '\n':
            passport_input.append(user_passport)
            user_passport = []

    if len(user_passport) != 0:
        passport_input.append(user_passport)
        user_passport = []

    return passport_input

def list_to_dict(passport_input):

    user_passports = []

    for user_passport in passport_input:

        dict_user_passport = {}

        for item_passport in user_passport:

            dict_items = item_passport.split(':')
            key = dict_items[0]
            value = dict_items[1]
            dict_user_passport[key] = value

        user_passports.append(dict_user_passport)

    return user_passports

def passport_validator(user_passports, fields):

    validated_passport = 0
    for user_passport in user_passports:
        if len(user_passport) == len(fields):
            validated_passport += int(passport_filter(user_passport, fields))
        elif len(user_passport) == len(fields[:-1]) and fields[-1] not in user_passport:
            validated_passport += int(passport_filter(user_passport, fields))

    print(validated_passport)

def passport_filter(user_passport, fields):

    check = True

    if len(user_passport[fields[0]]) != 4 or int(user_passport[fields[0]]) < 1920 or int(user_passport[fields[0]]) > 2002:
        check = False
    if len(user_passport[fields[1]]) != 4 or int(user_passport[fields[1]]) < 2010 or int(user_passport[fields[1]]) > 2020:
        check = False
    if len(user_passport[fields[2]]) != 4 or int(user_passport[fields[2]]) < 2020 or int(user_passport[fields[2]]) > 2030:
        check = False
    if ((('in' not in user_passport[fields[3]]) and ('cm' not in user_passport[fields[3]]) ) or () or 'in' in user_passport[fields[3]] and not (59<= int(user_passport[fields[3]][:-2]) <=76)) or ('cm' in user_passport[fields[3]] and not (150<= int(user_passport[fields[3]][:-2]) <=193)):
        check = False
    if user_passport[fields[4]][0] != '#' or all(digit not in string.hexdigits for digit in user_passport[fields[4]][:-1]):
        check = False
    if user_passport[fields[5]] not in 'amb blu brn gry grn hzl oth'.split(' '):
        check = False
    if len(user_passport[fields[6]]) != 9 or type(int(user_passport[fields[6]])) != int:
        check = False

    return check


def main():

    fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
    passport_input = readFile()
    user_passports = list_to_dict(passport_input)
    passport_validator(user_passports, fields)


if __name__ == "__main__":

    main()

    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    # hgt (Height) - a number followed by either cm or in:
    #     If cm, the number must be at least 150 and at most 193.
    #     If in, the number must be at least 59 and at most 76.
    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    # cid (Country ID) - ignored, missing or not.

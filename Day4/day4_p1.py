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
    count_1 = 0
    for user_passport in user_passports:
        check = True
        
        if len(user_passport) == len(fields):
            validated_passport += 1
        elif len(user_passport) == len(fields[:-1]) and fields[-1] not in user_passport:
            validated_passport += 1
            
        
        # for field in fields[:-1]:
        #     if field not in user_passport:
        #      j  check = False
            
        # if check == True:
        #     validated_passport += 1

    print(validated_passport)

def main():

    fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
    # print(fields[:-1])
    passport_input = readFile()
    user_passports = list_to_dict(passport_input)
    print((user_passports[0]))
    print((user_passports[-1]))
    passport_validator(user_passports, fields)
    

if __name__ == "__main__":

    main()
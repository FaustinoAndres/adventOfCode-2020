def readFile():

    f = open("day6_data.txt", "r")
    lines = f.readlines()

    group_answers = list()
    groups_answers = list()

    for line in lines:

        if line != '\n':
            for user_answer in line.rstrip('\n').split(' '):
                group_answers.append(user_answer)
        elif line == '\n':
            groups_answers.append(group_answers)
            group_answers = []

    if len(group_answers) != 0:
        groups_answers.append(group_answers)
        group_answers = []

    return groups_answers

def counts_answers(ALPHABET, groups_answers):

    yes_answer = []

    for group_answer in groups_answers:

        alphabet = hash_map(ALPHABET)
        for person_answer in group_answer:
            for answer in person_answer:
                if alphabet[answer] == 0:
                    alphabet[answer] = 1
        yes_answer.append(sum(alphabet.values()))
    return yes_answer


def hash_map(ALPHABET):

    alphabet = {}
    for letter in ALPHABET:
        alphabet[letter] = 0

    return alphabet

def main():

    ALPHABET = list(map(chr, range(97, 123)))
    groups_answers = readFile()
    yes_answers = counts_answers(ALPHABET, groups_answers)
    print(sum(yes_answers))

if __name__ == '__main__':

    main()
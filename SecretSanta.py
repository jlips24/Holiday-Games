import random

def make_matches(people):
    for person in people:
        match = random.randint(0, 5)
        while (people[match] == person) or (people[match][3] == True):
            match = random.randint(0, 5)
        person[2] = match
        people[match][3] = True
    return people

def print_matches(people):
    for person in people:
        print(f"\n{person[0]} is {people[person[2]][0]}'s Santa!")

def main():
    # [name, email, match, chosen]
    people = [
        ["Jake", "jake_lipson@yahoo.com", -1, False],
        ["Lukas", "", -1, False],
        ["Jason", "", -1, False],
        ["Chris", "", -1, False],
        ["Besnik", "", -1, False],
        ["Mike", "", -1, False],
    ]

    people = make_matches(people)
    print_matches(people)

if __name__ == "__main__":
    main()
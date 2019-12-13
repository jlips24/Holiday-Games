# TODO: Update readme to reflect new menu
# TODO: Create CSV import logic

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

def main_code_import():
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


def main():
    # Main menu
    import_type = input("\nWould you like to:\n\n1. import names from a CSV?\n2. Import names from code\n\n(Please type the number corresponding to your answer and then press enter)\n")
    while (import_type != '1') and (import_type != '2'):
        print("That response was invalid. Please choose from the options")
        import_type = input("\nWould you like to:\n\n1. import names from a CSV?\n2. Import names from code\n\n(Please type the number corresponding to your answer and then press enter)\n")
    # Menu logic
    import_type = int(import_type)
    if (import_type == 1):
        pass
    elif (import_type == 2):
        main_code_import()


if __name__ == "__main__":
    main()
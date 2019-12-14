import random
from helpers.CSVHelpers import csv_import


class SecretSanta(object):

    def make_matches(self, people):
        for person in people:
            match = random.randint(0, 5)
            while (people[match] == person) or (people[match][3] == True):
                match = random.randint(0, 5)
            person[2] = match
            people[match][3] = True
        return people


    def print_matches(self, people):
        for person in people:
            print(f"\n{person[0]} is {people[person[2]][0]}'s Santa!")
        print("\n")


    def main_code_import(self):
        # [name, email, match, chosen]
        people = [
            ["Person", "email@email.com", -1, False],
        ]

        people = self.make_matches(people)
        self.print_matches(people)


    def main_csv_import(self):
        people = csv_import("config/people.csv")
        self.print_matches(people)


    def start(self):
        # Main menu
        import_type = input("\nWould you like to:\n\n1. Import names from a CSV\n2. Import names from code\n\n(Please type the number corresponding to your answer and then press enter)\n\n")
        while (import_type != '1') and (import_type != '2'):
            print("That response was invalid. Please choose from the options")
            import_type = input("\nWould you like to:\n\n1. import names from a CSV?\n2. Import names from code\n\n(Please type the number corresponding to your answer and then press enter)\n\n")
        # Menu logic
        import_type = int(import_type)
        if (import_type == 1):
            self.main_csv_import()
        elif (import_type == 2):
            self.main_code_import()
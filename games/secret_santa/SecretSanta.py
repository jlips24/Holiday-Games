import random
import os
from helpers.CSVHelpers import csv_import
from helpers.EmailHelpers import send_emails


class SecretSanta(object):

    def make_matches(self, people):
        for person in people:
            match = random.randint(0, (len(people) - 1))
            print(people[match][3])
            while (people[match] == person) or (people[match][3] == True):
                match = random.randint(0, (len(people) - 1))
            person[2] = match
            people[match][3] = True
        return people


    def print_matches(self, people):
        for person in people:
            print(f"\n{person[0]} is {people[person[2]][0]}'s Santa!")
        print("\n")


    def main_csv_import(self):
        return csv_import("config/people.csv")

    def start(self):
        people = self.main_csv_import()
        people = self.make_matches(people)
        send_emails(people)
        
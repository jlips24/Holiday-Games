import random
import os
from helpers.CSVHelpers import csv_import
from helpers.EmailHelpers import send_emails


class SecretSanta(object):

    def make_matches(self, people):
        count = 0
        for person in people:
            match = random.randint(0, (len(people) - 1))
            while (people[match] == person) or (people[match][3] == True or (len(people) > 2 and people[match][2] == count)):
                match = random.randint(0, (len(people) - 1))
            person[2] = match
            people[match][3] = True
            count += 1
        return people


    def print_matches(self, people):
        for person in people:
            print(f"\n{person[0]} is {people[person[2]][0]}'s Santa!")
        print("\n")


    def start(self):
        people = csv_import("config/people.csv")
        people = self.make_matches(people)
        send_emails(people, "SecretSanta")

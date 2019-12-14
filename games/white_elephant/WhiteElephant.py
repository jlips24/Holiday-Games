import random
from helpers.CSVHelpers import csv_import
from helpers.EmailHelpers import send_emails


class WhiteElephant(object):

    def compile_master_list(self, people):
        txt = ""
        people = sorted(people, key = lambda x: int(x[2]))
        for person in people:
            txt += f"{person[2]}. {person[0]}\n"
        return txt

    def give_numbers(self, people):
        numbered_people = []
        count = 1
        while (people != []):
            random_index = random.randint(0, len(people) - 1)
            random_person = people.pop(random_index)
            random_person[2] = count
            random_person[3] = True
            numbered_people.append(random_person)
            count += 1
        return numbered_people

    
    def start(self):
        game_master_name = input("What is the name of the most trustworthy person you're playing with?\n")
        game_master_email = input("What is their email address?\n")

        people = csv_import("config/people.csv")
        people = self.give_numbers(people)
        print(people)
        send_emails(people, "WhiteElephant")
        send_emails([[game_master_name, game_master_email, 0, True]], "WhiteElephantMaster", extra=self.compile_master_list(people))
        


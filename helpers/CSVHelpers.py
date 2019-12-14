import csv

def csv_import(filename):
    people = []
    with open(filename, "rt") as f:
        data = csv.reader(f)
        count = 0
        for row in data:
            if (count != 0):
                # [name, email, match/number, chosen]
                person = [row[0], row[1], -1, False]
                people.append(person)
            count += 1
    return people

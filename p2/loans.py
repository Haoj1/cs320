
race_lookup = {
    "1": "American Indian or Alaska Native",
    "2": "Asian",
    "21": "Asian Indian",
    "22": "Chinese",
    "23": "Filipino",
    "24": "Japanese",
    "25": "Korean",
    "26": "Vietnamese",
    "27": "Other Asian",
    "3": "Black or African American",
    "4": "Native Hawaiian or Other Pacific Islander",
    "41": "Native Hawaiian",
    "42": "Guamanian or Chamorro",
    "43": "Samoan",
    "44": "Other Pacific Islander",
    "5": "White",
}

class Applicant:
    def __init__(self, age, race):
        self.age = age
        self.race = set()
        for r in race:
            if r in race_lookup:
                self.race.add(race_lookup[r])

    def __repr__(self):
        applicants = [r for r in self.race]
        Applicant = (self.age, applicants)
        return 'Applicant' + str(Applicant)

    def lower_age(self):
        age = self.age.replace('>', '')
        age = age.replace('<', '')
        return int(age.split('-')[0])

    def __lt__(self, other):
        if self.lower_age() < other.lower_age():
            return True
        else:
            return False


class Loan:
    def __init__(self, values):
        self.loan_amount = float(values["loan_amount"]) if 'NA' not in values["loan_amount"] and \
                                                           'Exempt' not in values["loan_amount"] else float(-1)
        # add lines here
        self.property_value = float(values["property_value"]) \
            if 'NA' not in values["property_value"] and 'Exempt' not in values["property_value"] else float(-1)
        self.interest_rate = float(values["interest_rate"]) \
            if 'NA' not in values["interest_rate"] and 'Exempt' not in values["interest_rate"] else float(-1)
        # if 'NA' or 'Exempt' in self.loan_amount:
        #     self.loan_amount = float(-1)
        # else:
        #     self.loan_amount = float(self.loan_amount)
        # if 'NA' or 'Exempt' in self.property_value:
        #     self.property_value = float(-1)
        # else:
        #     self.property_value = float(self.property_value)
        race = []
        for key in values:
            if key.startswith("applicant_race-"):
                race.append(values[key])
        self.applicants = [Applicant(values["applicant_age"], race)]
        if values["co-applicant_age"] != "9999":
            co_race = []
            for key in values:
                if key.startswith("co-applicant_race-"):
                    co_race.append(values[key])
            self.applicants.append(Applicant(values["co-applicant_age"], co_race))

    def __str__(self):
        return '<Loan: ' + str(self.interest_rate) + '% on $' + str(self.property_value) + " with " \
               + str(len(self.applicants)) + ' applicant(s)>'

    def __repr__(self):
        return self.__str__()

    def yearly_amounts(self, yearly_payment):
        # TODO: assert interest and amount are positive
        assert self.interest_rate > 0 and self.loan_amount > 0
        amt = self.loan_amount

        while amt > 0:
            yield amt
            # TODO: add interest rate multiplied by amt to amt
            amt = amt * self.interest_rate * 0.01 + amt
            # TODO: subtract yearly payment from amt
            amt = amt - yearly_payment

import csv
import json
from zipfile import ZipFile
from io import TextIOWrapper


class Bank:
    def __init__(self, name):
        with open("banks.json") as f:
            banks = json.load(f)
        for bank in banks:
            if bank['name'] == name:
                self.lei = bank['lei']
        self.loans = []
        with ZipFile("wi.zip", "r") as zipfile:
            with zipfile.open("wi.csv") as csvfile:
                reader = csv.DictReader(TextIOWrapper(csvfile))
                for values in reader:
                    if values['lei'] == self.lei:
                        self.loans.append(Loan(values))

    def __len__(self):
        return len(self.loans)

    def __getitem__(self, lookup):
        return self.loans[lookup]

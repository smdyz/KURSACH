import json
import datetime


def acceptance_oper():
    with open("operations.json") as file:
        json_dict = file.read()
    print(json.loads(json_dict))


def print_oper(date, description, from_, to_, amount, currency):
    pass
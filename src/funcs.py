import json
from datetime import date
import datetime


# work
def acceptance_oper():
    with open("operations.json", "r", encoding="UTF-8") as file:
        data = file.read()
        dict_array = json.loads(data)
        final_dict = []
        for element in dict_array:
            if len(element) > 1:
                final_dict.append(element)
        return final_dict


# work
def date_for_oper(date_oper):
    date_oper = date_oper[:10].split("-")
    date_oper = date(int(date_oper[0]), int(date_oper[1]), int(date_oper[2]))
    return date_oper


# work
def latest_opers():
    new_list = []
    for_list = {}

    for i in acceptance_oper():

        if i['state'] == "EXECUTED" and i['date'].startswith("2019-"):

            date1 = date_for_oper(i["date"])

            for j in acceptance_oper():

                if j['state'] == "EXECUTED" and j['date'].startswith("2019-"):

                    date2 = date_for_oper(j["date"])

                    if date2 > date1 and j not in new_list:
                        date1 = date2
                        for_list = j

            new_list.append(for_list)
            if len(new_list) >= 5:
                return new_list


# work
def hidden_num(card: str):
    if card != '':
        card = card.split()
        num = card[-1]
        if card[0].startswith("Счет"):
            hid_num = f"**{num[-4:]}"
        else:
            hid_num = f"{num[:4]} {num[4:6]}** **** {num[-4:]}"
        card[-1] = hid_num
        return " ".join(card)
    else:
        return ""


def print_oper(data, description, to_, amount, currency, from_=""):
    print(f"""{date_for_oper(data).strftime("%d.%m.%Y")} {description}
{hidden_num(from_)} -> {hidden_num(to_)}
{amount} {currency}""")

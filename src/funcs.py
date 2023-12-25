import json
import datetime
import locale

locale.setlocale(locale.LC_ALL, 'ru_RU.utf8')


# dont work
def acceptance_oper():
    # with open("operations.json") as f:
    #     data = json.load(f)
    with open("operations.txt") as file:
        for i in file:
            print(i)


# work
def date_for_oper(date_oper: str):
    date_oper = date_oper[:10].split("-")
    return f"{date_oper[-1]}.{date_oper[-2]}.{date_oper[-3]}"


# work
def hidden_num(card: str):
    card = card.split()
    num = card[-1]
    if card[0].startswith("Счет"):
        hid_num = f"**{num[-4:]}"
    else:
        hid_num = f"{num[:4]} {num[4:6]}** **** {num[-4:]}"
    card[-1] = hid_num
    return " ".join(card)


date = "2018-08-19T04:27:37.904916"
description = "Перевод с карты на карту"
from_ = "Visa Classic 6831982476737658"
to_ = "Visa Platinum 8990922113665229"
amount = "56883.54"
currency = "USD"


def print_oper(date, description, from_, to_, amount, currency):
    print(f"""{date_for_oper(date)} {description}
{hidden_num(from_)} -> {hidden_num(to_)}
{amount} {currency}""")


print_oper(date, description, from_, to_, amount, currency)

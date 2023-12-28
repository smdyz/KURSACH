from src.funcs import acceptance_oper
from src.funcs import date_for_oper
from src.funcs import latest_opers
from src.funcs import hidden_num
from src.funcs import print_oper
import datetime


def test_acceptance_oper():
    assert acceptance_oper() != ''


def test_date_for_oper():
    assert date_for_oper(acceptance_oper()[0]["date"]) == datetime.date(2019, 8, 26)


def test_latest_opers():
    assert latest_opers() == [{'date': '2019-12-08T22:46:21.935582',
  'description': 'Открытие вклада',
  'id': 863064926,
  'operationAmount': {'amount': '41096.24',
                      'currency': {'code': 'USD', 'name': 'USD'}},
  'state': 'EXECUTED',
  'to': 'Счет 90424923579946435907'},
 {'date': '2019-12-07T06:17:14.634890',
  'description': 'Перевод организации',
  'from': 'Visa Classic 2842878893689012',
  'id': 114832369,
  'operationAmount': {'amount': '48150.39',
                      'currency': {'code': 'USD', 'name': 'USD'}},
  'state': 'EXECUTED',
  'to': 'Счет 35158586384610753655'},
 {'date': '2019-11-19T09:22:25.899614',
  'description': 'Перевод организации',
  'from': 'Maestro 7810846596785568',
  'id': 154927927,
  'operationAmount': {'amount': '30153.72',
                      'currency': {'code': 'RUB', 'name': 'руб.'}},
  'state': 'EXECUTED',
  'to': 'Счет 43241152692663622869'},
 {'date': '2019-11-13T17:38:04.800051',
  'description': 'Перевод со счета на счет',
  'from': 'Счет 38611439522855669794',
  'id': 482520625,
  'operationAmount': {'amount': '62814.53',
                      'currency': {'code': 'RUB', 'name': 'руб.'}},
  'state': 'EXECUTED',
  'to': 'Счет 46765464282437878125'},
 {'date': '2019-11-05T12:04:13.781725',
  'description': 'Открытие вклада',
  'id': 801684332,
  'operationAmount': {'amount': '21344.35',
                      'currency': {'code': 'RUB', 'name': 'руб.'}},
  'state': 'EXECUTED',
  'to': 'Счет 77613226829885488381'}]


def test_hidden_num():
    assert hidden_num(acceptance_oper()[0]["from"]) == "Maestro 1596 83** **** 5199"


# def test_print_oper():
#     assert print_oper(acceptance_oper()[0]["date"], acceptance_oper()[0]["description"],
#                       acceptance_oper()[0]["to"], acceptance_oper()[0]["operationAmount"]["amount"],
#                       acceptance_oper()[0]["operationAmount"]["currency"]["name"], acceptance_oper()[0]["from"]) == """26.08.2019 Перевод организации
# Maestro 1596 83** **** 5199 -> Счет **9589
# 31957.58 руб."""

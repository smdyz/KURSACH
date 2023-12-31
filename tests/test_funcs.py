from src.funcs import acceptance_oper
from src.funcs import date_for_oper
from src.funcs import latest_opers
from src.funcs import hidden_num
from src.funcs import print_oper


def test_acceptance_oper():
    assert acceptance_oper() != ''


def test_date_for_oper():
    assert date_for_oper(acceptance_oper()[0]["date"]) == "2019-08-26"


def test_latest_opers():
    assert latest_opers() == """08.12.2019 Открытие вклада
 -> Счет **5907
41096.24 USD




07.12.2019 Перевод организации
Visa Classic 2842 87** **** 9012 -> Счет **3655
48150.39 USD




03.12.2019 Перевод с карты на карту
MasterCard 1796 81** **** 9527 -> Visa Classic 7699 85** **** 9288
17628.50 USD




19.11.2019 Перевод организации
Maestro 7810 84** **** 5568 -> Счет **2869
30153.72 руб.




13.11.2019 Перевод со счета на счет
Счет **9794 -> Счет **8125
62814.53 руб.



"""


def test_hidden_num():
    assert hidden_num(acceptance_oper()[0]["from"]) == "Maestro 1596 83** **** 5199"


def test_print_oper():
    assert print_oper(acceptance_oper()[0]["date"], acceptance_oper()[0]["description"],
                      acceptance_oper()[0]["to_"], acceptance_oper()[0]["operationAmount"]["amount"],
                      acceptance_oper()[0]["operationAmount"]["currency"]["name"], acceptance_oper()[0]["from"]) == """26.08.2019 Перевод организации
Maestro 1596 83** **** 5199 -> Счет **9589
31957.58 руб."""

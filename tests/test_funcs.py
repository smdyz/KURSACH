from src.funcs import acceptance_oper
from src.funcs import date_for_oper
from src.funcs import latest_opers
from src.funcs import hidden_num
from src.funcs import print_oper


def test_acceptance_oper():
    assert acceptance_oper() != ''


def test_date_for_oper():
    assert date_for_oper(acceptance_oper()[0]["date"])


def test_latest_opers():
    assert latest_opers()


def test_hidden_num():
    assert hidden_num(acceptance_oper()[0]["from"])


def test_print_oper():
    assert print_oper(acceptance_oper()[0]["date"], acceptance_oper()[0]["description"],
                      acceptance_oper()[0]["to_"], acceptance_oper()[0]["operationAmount"]["amount"],
                      acceptance_oper()[0]["operationAmount"]["currency"]["name"], acceptance_oper()[0]["from"]) == """26.08.2019 Перевод организации
Maestro 1596 83** **** 5199 -> Счет **9589
31957.58 руб."""

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
    pass


def test_print_oper():
    pass
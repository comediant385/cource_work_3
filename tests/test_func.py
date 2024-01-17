from src.func import *

def test_get_user_operations():
    assert len(get_user_operations()) == 5

def test_print_user_operations():
    operation = Operation("2019-04-04T23:20:05.206878", "Перевод со счета на счет", "Счет 19708645243227258542",
                            "Счет 75651667383060284188", "48223.05", "руб.")
    assert operation.hide_info_where_from() == 'Счет **8542'
    assert operation.hide_info_to() == 'Счет **4188'
    assert operation.format_date() == '04.04.2019'
    assert operation.print_info() == ('04.04.2019 Перевод со счета на счет\n' 'Счет **8542 -> Счет **4188\n' '48223.05 руб.\n')

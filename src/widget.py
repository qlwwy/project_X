from masks import get_mask_card_number, get_mask_account

def mask_account_card(card_name):
    """
    Принимает один аргумент — строку, содержащую тип и номер карты или счета
    """
    if "Счет" in card_name:
        return get_mask_account(card_name)
    else:
        return get_mask_card_number(card_name)


def get_date(date_str):
    """
    Принимает строку с датой в формате "2024-03-11T02:26:18.671407" и возвращает строку с датой в формате "ДД.ММ.ГГГГ"
    """
    date_part = date_str.split("T")[0]
    year, month, day = date_part.split("-")
    return f"{day}.{month}.{year}"


card_name = input()
print(mask_account_card(card_name))

date_str = input()
print(get_date(date_str))

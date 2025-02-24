from src import masks
def mask_account_card(card_name):
    """
    Принимает один аргумент — строку, содержащую тип и номер карты или счета
    """
    if "Счет" in card_name:
        return masks.get_mask_account(card_name)
    else:
        return masks.get_mask_card_number(card_name)


def get_date(date_str):
    """
    Принимает строку с датой в формате "2024-03-11T02:26:18.671407" и возвращает строку с датой в формате "ДД.ММ.ГГГГ"
    """
    date_part = date_str.split("T")[0]
    year, month, day = date_part.split("-")
    return f"{day}.{month}.{year}"

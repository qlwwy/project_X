def get_mask_card_number(card_number: int) -> str:
    """
    Принимает на вход номер карты в виде числа и возвращает маску номера по правилу XXXX XX** **** XXXX
    """
    card_str = str(card_number)
    return f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"


def get_mask_account(account_number: int) -> str:
    """
    Принимает на вход номер счета в виде числа и возвращает маску номера по правилу **XXXX
    """
    account_str = str(account_number)
    return f"**{account_str[-4:]}"


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
    Принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407" и возвращает строку с датой в формате "ДД.ММ.ГГГГ"
    """
    date_part = date_str.split("T")[0]
    year, month, day = date_part.split("-")
    return f"{day}.{month}.{year}"


if __name__ == "__main__":
    card_str = input()
    account_str = input()
    date_str = input()

    print(mask_account_card(card_str))
    print(mask_account_card(account_str))
    print(get_date(date_str))

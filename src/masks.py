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


card_number = int(input())
from datetime import datetime
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
    try:
        # Проверяем, что строка содержит 'T', что указывает на наличие времени
        if 'T' not in date_str:
            raise ValueError("Неверный формат даты")

        date_obj = datetime.fromisoformat(date_str)
        return date_obj.strftime("%d.%m.%Y")
    except ValueError:
        raise ValueError("Неверный формат даты")

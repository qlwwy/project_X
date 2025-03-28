def filter_by_currency(transactions, currency_code):
    """Функция возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной."""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency_code:
            yield transaction


def transaction_descriptions(transactions):
    """принимает список словарей с транзакциями и возвращает описание каждой операции по очереди."""
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start, end):
    """Генератор принимает начальное и конечное значения для генерации диапазона номеров."""
    for number in range(start, end + 1):
        yield f"{number:016}"

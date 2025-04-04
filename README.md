# Виджет банковских операций клиента
## Описание:
Это виджет, который показывает несколько последних успешных банковских операций клиента.
## Установка: 
### Клонируйте репозиторий:
```
https://github.com/qlwwy/project_X
```
## Создайте виртуальное окружение для изоляции зависимостей проекта. 
Это можно сделать с помощью venv или virtualenv. Используя venv (встроенный модуль Python): python -m venv venv
## Тестирование:
### Информация о тестировании:

Проект включает тесты для проверки корректности работы функций. Тесты находятся в каталоге tests/ и используют pytest

# Запуск тестов:

Убедитесь, что pytest установлен:

    pip install pytest

Запустите тесты командой:

    pytest -v

# Описание тестов
### Модуль masks:
get_mask_card_number: Проверка корректности маскирования номера банковской карты.
get_mask_account: Проверка правильности маскирования номера счета.
### Модуль widget:
mask_account_card: Тестирование корректного распознавания и применения маскировки в зависимости от типа входных данных (карта или счет).
get_date: Проверка правильности преобразования даты.
### Модуль processing:
filter_by_state: Тестирование фильтрации списка словарей по заданному статусу.
sort_by_date: Проверка сортировки списка словарей по датам в порядке убывания и возрастания.
### Модуль generators:
filter_by_currency: Генератор, фильтрующий транзакции по заданной валюте.
transaction_descriptions: Генератор, возвращающий описание каждой транзакции.
card_number_generator: Генератор, выдающий номера банковских карт в заданном диапазоне.
# Логирование выполнения функций
### Модуль decorators:
log: Декоратор для логирования выполнения функции. Логи могут быть записаны в файл или выведены на экран.
### Модуль financial_operations:
Считывание данных из CSV файлов.
Считывание данных из Excel файлов.

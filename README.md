# Task3-DIplom

Автотесты для UI
## Дипломный проект. Задание 3: Автотесты для UI Stellar Burgers
<hr>

## Студентка: Елена Нурыева

## <h>Когорта: #21</h>
<hr>

## <h>Project: Stellar Burgers API</h>

## <h>Инструкция по запуску:</h>

### <h>1. Установите зависимости:</h>

> pip install -r requirements.txt</h>

### <h>2. Запустить все тесты:</h>

> pytest -v

### <h>3. Посмотреть отчет по прогону html</h>

> allure serve allure_results


<hr>

<h3 align="left" style="color:green">Project files and description:</h3>

| Название файла              | Содержание файла                        |
|-----------------------------|-----------------------------------------|
| allure_results.dir          | Папка с отчетами Allure                 |
| locators dir                | Директория с локатора                   |
| auth_locators.py            | Локаторы для авторизации                |
| constructor_locators.py     | Локаторы для страницы конструктора      |
| order_feed_locators.py      | Локаторы для страницы Лента заказов     |
| pages dir                   | Директория с методами страниц           |
| auth_page.py                | Методы авторизации                      |
| base_page.py                | Основные методы                         |
| constructor_page.py         | Методы главной страницы с конструктором |
| order_feed_page.py          | Методы страницы лента заказов           |
| tests dir                   | Директория с тестами                    |
| conftest.py                 | Фикстуры                                |
| test_basic_functionality.py | Тесты основной функциональности         |
| test_order_feed.py          | Тесты ленты заказов                     |
| curl.py                     | Файл с URL                              |
| data.py                     | Файл с данными                          |
| helpers.py                  | Хэлпер                                  |
| requirements.txt            | Файл с зависимостями                    |


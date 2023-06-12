# JohnDeereParser
![made by](https://img.shields.io/badge/made_by-slychagin-green)
![python](https://img.shields.io/badge/python-v3.10.5-blue)
![selenium](https://img.shields.io/badge/selenium-green)
![playwrite](https://img.shields.io/badge/playwrite-blue)
![pandas](https://img.shields.io/badge/pandas-red)

Parser get data from JohnDeere site

#### Parts parser from https://partscatalog.deere.com/jdrc/search
#
Парсинг данных с данного сайта осуществил в двух вариантах (см. selenium_parser и playwrite_parser):
- с использованием Selenium;
- с использованием Playwright.
Playwright оказался быстрее примерно в 1,5 раза.

Касательно того как ускорить парсинг 1000 000 позиций - тут нужна работа напрямую с json из response.
У меня получилось вытянуть данные только с помощью Selenium и Playwrite, а они медленные.
Соответсвенно при работе напрямую (я уже делал так в парсере Coindesck https://github.com/slychagin/CoindeskParser)
я бы использовал асинхронную библиотеку aiohttp.

#### Вы можете запустить этот проект локально просто сделав следующее:
- `git clone https://github.com/slychagin/JohnDeereParser.git`;
- у вас должен быть установлен Python;
- установите все зависимости из файла requirements.txt;
- запустить файлы selenium_parser и playwrite_parser.

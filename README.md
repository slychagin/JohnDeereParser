# JohnDeereParser
![made by](https://img.shields.io/badge/made_by-slychagin-green)
![python](https://img.shields.io/badge/python-v3.10.5-blue)
![selenium](https://img.shields.io/badge/selenium-green)
![playwright](https://img.shields.io/badge/playwright-blue)
![pandas](https://img.shields.io/badge/pandas-red)

Parser get data from JohnDeere site

#### Parts parser from https://partscatalog.deere.com/jdrc/search
#
Парсинг данных с данного сайта в двух вариантах (см. selenium_parser и playwrite_parser):
- с использованием Selenium;
- с использованием Playwright.
Playwright оказался быстрее примерно в 1,5 раза.

#### Вы можете запустить этот проект локально просто сделав следующее:
- `git clone https://github.com/slychagin/JohnDeereParser.git`;
- у вас должен быть установлен Python;
- установите все зависимости из файла requirements.txt;
- запустить файлы selenium_parser и playwright_parser;
- количество деталей, которые необходимо спарсить, соответсвенно можно изменить в файле articles.txt.

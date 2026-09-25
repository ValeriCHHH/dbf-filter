# 🛠️ dbf-filter
[![Build and Release](https://github.com/ValeriCHHH/dbf-filter/actions/workflows/release.yml/badge.svg)](https://github.com/ValeriCHHH/dbf-filter/actions/workflows/release.yml)
[![GitHub Release](https://img.shields.io/github/v/release/ValeriCHHH/dbf-filter?color=blue)](https://github.com/ValeriCHHH/dbf-filter/releases/latest)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](LICENSE)
Универсальная кроссплатформенная утилита командной строки для поиска, фильтрации, сортировки и конвертации баз данных **DBF** ---
## 🚀 Возможности
* 🔍 **Поиск и фильтрация:** поиск ключевых слов в указанной колонке таблицы (поддержка поиска нескольких фраз одновременно).
* 🔀 **Сортировка:** сортировка итогового списка по любому выбранному полю.
* 🌐 **Поддержка кириллицы:** корректно обрабатывает исходные кодировки `CP866`, `Windows-1251` и сохраняет CSV в `UTF-8* ⚡ **Эффективность:** поток чтения обрабатывает большие таблицы с минимальным потреблением оперативной памяти.
* 📦 **Кроссплатформенность:** автоматическая сборка готовых пакетов под Linux (`.deb`, `.rpm`) и Windows (`.exe`).
---
## 📥 Установка и скачивание
Скачать свежую версию под вашу операционную систему можно в разделе **[Releases / Релизы](https://github.com/ValeriCHHH/dbf-filter/releases/latest)**.
### Debian / Ubuntu / Linux Mint / Astra Linux
Скачайте `.deb` файл и установите его:

(dBase / FoxPro / Clipper) в формат **CSV** с поддержкой русских кодировок.
BOM (без проблем открывается в Microsoft Excel и LibreOffice Calc).
sudo apt install ./dbf-filter_1.0.0_all.deb 
### Fedora / RHEL / ALT Linux / ROSA
 Скачайте `.rpm` файл и установите его:
```bash
sudo rpm -i dbf-filter-1.0.0.noarch.rpm
``` 
### Windows
Скачайте автономный исполняемый файл `dbf-filter.exe`. Он готов к работе через командную строку (`cmd` или `PowerShell`) и не требует установки интерпретатора Python.
---
## 💻 Использование
Базовый синтаксис команды:
```bash
dbf-filter -i <ВХОДНОЙФАЙЛ> -o <ВЫХОДНОЙФАЙЛ> [ДОП_ПАРАМЕТРЫ]
```
### Доступные параметры
 | Флаг | Полный параметр | Описание | Обязательный? |
| --- | --- | --- | --- |
| `-i` | `--input` | Путь к исходному `.dbf` файлу | **Да** |
| `-o` | `--output` | Путь для сохранения результирующего `.csv` файла | **Да** |
| `-f` | `--field` | Название поля (колонки) для поиска | Нет |
| `-q` | `--query` | Одно или несколько ключевых слов для поиска (через пробел) | Нет |
| `-s` | `--sort` | Название поля (колонки), по которому нужно отсортировать выборку | Нет |
| `-e` | `--encoding` | Кодировка исходного DBF файла *(по умолчанию: `cp866`)* | Нет |
 ---
## 💡 Примеры команд
 **1. Поиск по полю адреса:**
Найти все строки, у которых в колонке `ADRES` встречаются слова «мурманск» или «мурманский район»:

dbf-filter -i DATA.DBF -o result.csv -f ADRES -q мурманск “мурманский район” **2. Поиск с сортировкой результатов:**
Найти совпадения по адресу и отсортировать итоговый файл по колонке `NAME`:

dbf-filter -i DATA.DBF -o sorted_result.csv -f ADRES -q уфа -s NAME 
 **3. Полная конвертация DBF в CSV (без фильтров):**

dbf-filter -i data.dbf -o full_export.csv 
 **4. Вызов справки:**

dbf-filter –help 
 ---
## 🛠️ Запуск из исходного кода
 Если вы хотите запустить проект непосредственно через Python:
 1. Клонируйте репозиторий:

git clone git@github.com:ValeriCHHH/dbf-filter.git cd dbf-filter 
  2. Установите зависимости:

pip install -r requirements.txt 
  3. Запустите скрипт:

python3 src/dbf_filter.py -i input.dbf -o output.csv -f ADRES -q саранск 
``` 
 📄 Лицензия 
Проект распространяется под свободным лицензионным соглашением GNU General Public License v3.0

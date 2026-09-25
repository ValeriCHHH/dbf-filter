# 🛠️ dbf-filter

[![Build and Release](https://github.com/ValeriCHHH/dbf-filter/actions/workflows/release.yml/badge.svg)](https://github.com/ValeriCHHH/dbf-filter/actions/workflows/release.yml)
[![GitHub Release](https://img.shields.io/github/v/release/ValeriCHHH/dbf-filter?color=blue)](https://github.com/ValeriCHHH/dbf-filter/releases/latest)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Быстрая консольная утилита для фильтрации, поиска, сортировки и конвертации таблиц **DBF** (dBase / FoxPro) в формат **CSV** с поддержкой кодировок `CP866`, `Windows-1251` и `UTF-8`.

---

## 🚀 Возможности

* 🔍 **Поиск и фильтрация:** Поиск ключевых слов в выбранном поле таблицы (с поддержкой нескольких фраз одновременно).
* 🔀 **Сортировка:** Упорядочивание результатов по любой колонке.
* 🌐 **Поддержка кодировок:** Корректно читает кириллицу из старых баз dBase (`CP866`) и сохраняет в CSV с меткой UTF-8 BOM (без проблем открывается в MS Excel и LibreOffice).
* ⚡ **Высокая скорость:** Потоковая обработка данных с минимальным потреблением оперативной памяти.
* 📦 **Кроссплатформенность:** Готовые исполняемые файлы под Linux (`.deb`, `.rpm`) и Windows (`.exe`).

---

## 📥 Установка и скачивание

Готовые бинарные файлы для всех ОС доступны на странице **[Releases / Релизы](https://github.com/ValeriCHHH/dbf-filter/releases/latest)**.

### Linux (Ubuntu / Debian / Astra Linux)
Скачайте `.deb` пакет и установите его через терминал:
```bash
sudo apt install ./dbf-filter_1.0.0_all.deb
```

### Fedora/RHEL/ALT Linux/ROSA
Скачайте `.rpm` файл и установите его:
```bash
sudo rpm -i dbf-filter-1.0.0.noarch.rpm
```

### Windows
Скачайте автономный исполняемый файл `dbf-filter.exe`. Он готов к работе через командную строку (`cmd` или `PowerShell`) и не требует установки.

## 💻 Использование
Базовый синтаксис команды:
```bash
dbf-filter -i <ВХОДНОЙ ФАЙЛ> -o <ВЫХОДНОЙ ФАЙЛ> [ДОП_ПАРАМЕТРЫ]
```
Доступные параметры:
`-i`, `--input` - Путь к исходному `.dbf` файлу (обязательный параметр)
`-o`, `--output` - Путь для сохранения результирующего `.csv` файла (обязательный параметр)
`-f`, `--field` - Название поля (колонки) для поиска (не обязательный параметр)
`-q`, `--query` - Одно или несколько ключевых слов для поиска (через пробел) (не обязательный параметр)
`-s`, `--sort` - Название поля (колонки), по которому нужно отсортировать выборку (не обязательный параметр)
`-e`, `--encoding` - Кодировка исходного DBF файла (по умолчанию: `cp866`)

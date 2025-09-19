Expense Tracker (PySide6 + PostgreSQL)

Небольшое настольное приложение:

GUI на PySide6

БД на PostgreSQL

Кнопки: Создать схему и таблицы, Внести данные, Показать данные

Параметризованные запросы, транзакции, фильтры в отчёте

1) Требования

Python 3.12+

PostgreSQL 13+ (локально)

Git

Рекомендуется ставить и запускать в виртуальном окружении (.venv).

2) Установка (Windows / macOS / Linux)
2.1 Клонирование репозитория
git clone <URL_ВАШЕГО_РЕПО> expenses-tracker
cd expenses-tracker

2.2 Создать и активировать виртуальное окружение
Windows (PowerShell)
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip

macOS / Linux (bash/zsh)
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip

2.3 Установить зависимости
pip install -r requirements.txt

3) Подготовка PostgreSQL
3.1 Создать пустую базу

Подключитесь к серверу Postgres (psql/pgAdmin/IDE) и выполните ОДИН раз:

CREATE DATABASE expenses_db;


Примечание: база создаётся один раз вручную. Таблицы/типы создаёт само приложение по кнопке «Создать схему и таблицы».

3.2 Настроить подключение

Отредактируйте app/config_example.json (UTF-8):

{
  "dbname": "expenses_db",
  "user": "postgres",
  "password": "ВАШ_ПАРОЛЬ",
  "host": "127.0.0.1",
  "port": 5432
}


Если пароль/хост содержат экзотические символы, используйте ASCII и убедитесь, что файл сохранён в UTF-8 (без BOM тоже ок).

4) Запуск приложения
python -m app.main


В главном окне:

Нажмите «Создать схему и таблицы» – выполнится schema.sql, создадутся ENUM и таблицы.

«Внести данные» – модальная форма добавления расхода (вставка через транзакцию).

«Показать данные» – окно отчёта с JOIN и фильтрами (даты, категория, поиск).

5) Работа с UI-файлами (опционально)

Проект использует .ui из Qt Designer.

Где найти Designer

Если используете локальный venv:

Windows: .venv\Scripts\pyside6-designer.exe

macOS/Linux: .venv/bin/pyside6-designer

Если venv не активирован — Designer может быть в глобальном Python.

Редактируете .ui → генерируете .py
pyside6-uic app/ui/mainwindow.ui    -o app/ui/ui_mainwindow.py
pyside6-uic app/ui/add_expense.ui   -o app/ui/ui_add_expense.py
pyside6-uic app/ui/report_dialog.ui -o app/ui/ui_report_dialog.py


После каждой правки .ui перегенерируйте соответствующий ui_*.py.

Стили (QSS)

Глобальный стиль лежит в app/style.qss.
Он автоматически подхватывается в app/main.py при запуске.

6) Схема БД

По умолчанию используется схема public.
schema.sql идемпотентный – можно запускать повторно:

создаёт/добавляет ENUM expense_category, payment_method;

создаёт таблицы app_user, merchant, expense;

добавляет демо-пользователя demo (ON CONFLICT DO NOTHING).

Хотите свою схему (например, finance)? Добавьте в начало schema.sql:

CREATE SCHEMA IF NOT EXISTS finance;
SET search_path = finance, public;

7) Частые проблемы и решения

UnicodeDecodeError / utf-8 при нажатии кнопок
→ Файлы schema.sql и app/config_example.json должны быть сохранены в UTF-8.
В main.py чтение schema.sql идёт как utf-8-sig, чтобы съедать BOM.

uuid_generate_v4() неизвестна
→ Либо используйте вариант схемы без расширений (BIGINT IDENTITY в schema.sql), либо выполните:

CREATE EXTENSION IF NOT EXISTS pgcrypto; -- и используйте gen_random_uuid()
-- или:
-- CREATE EXTENSION IF NOT EXISTS "uuid-ossp";


(Требуются права суперпользователя/DBA.)

«Тип уже существует»/«Таблица уже существует»
→ schema.sql уже идемпотентен. Если используете собственный скрипт — добавьте IF NOT EXISTS или ALTER TYPE ... ADD VALUE IF NOT EXISTS ....

Нет папки .venv
→ Значит вы устанавливали в глобальный Python. Создайте локальный venv по инструкции из раздела 2.2 и укажите его в IDE.

Стрелки у QComboBox/QDateEdit исчезли после стилизации
→ Либо не стилезуйте ::drop-down, либо задайте ::down-arrow с иконкой. См. комментарии в style.qss.

8) Полезные команды
Обновить зависимости
pip install -U -r requirements.txt

Заморозить зависимости (если добавляли свои)
pip freeze > requirements.txt

Деинсталляция окружения (если нужно переустановить всё)

Деактивируйте: deactivate

Удалите папку .venv/

Повторите шаги 2.2–2.3

9) Структура проекта
expenses-tracker/
├─ app/
│  ├─ main.py               — входная точка (QApplication)
│  ├─ dialogs.py            — диалог «Внести данные»
│  ├─ views.py              — окно/диалог отчёта
│  ├─ db.py                 — подключение к БД, транзакции, helpers
│  ├─ logging_conf.py       — логирование в app.log
│  ├─ style.qss             — стили Qt
│  └─ ui/
│     ├─ mainwindow.ui      — главное окно (Designer)
│     ├─ add_expense.ui     — форма добавления (Designer)
│     ├─ report_dialog.ui   — отчёт (Designer)
│     ├─ ui_*.py            — файлы, сгенерированные pyside6-uic
├─ schema.sql               — DDL (идемпотентный)
├─ requirements.txt
└─ README.md

10) Лицензия

Укажите здесь вашу лицензию (MIT/Apache-2.0/…).

Быстрый старт (компактно)
git clone <URL> expenses-tracker && cd expenses-tracker
# Windows
py -3.12 -m venv .venv && .\.venv\Scripts\Activate.ps1
# macOS/Linux
# python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
# создайте базу в Postgres: CREATE DATABASE expenses_db;
# отредактируйте app/config_example.json под свои креды
python -m app.main
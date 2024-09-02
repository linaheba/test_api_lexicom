# test_api_lexicom
Тестовое задание для Lexicom

**Задание 1.**

Для запуска задания 1 требуется переименовать файл `.env.example` в `.env` 
и из директории с файлом `docker-compose.yml` сбилдить и запустить докер с помощью команд:


```docker-compose build```

```docker-compose up -d```

**Задание 2.**

Решение #1 на SQL:

выполняем запрос:


```
UPDATE full_names
SET status = short_names.status
FROM short_names
WHERE short_names.name = SPLIT_PART(full_names.name, '.', 1);
```

Здесь мы обновляем поле status, сравнивая имена из двух таблиц и используя для этого разделение строки.



Решение #2 на SQL:

для начала создаём индексы в обеих таблицах:

```CREATE INDEX index_short_name ON short_names (name);```

```CREATE INDEX index_full_name ON full_names (name);```

выполняем запрос:

```
UPDATE full_names
SET status = short_names.status
FROM short_names
WHERE full_names.name LIKE CONCAT(short_names.name, '.%');
```

Здесь мы обновляем поле status, сравнивая имена из двух таблиц и используя для этого оператор like (но перед этим создаём индексы).

Это решение гораздо хуже и медленнее первого.


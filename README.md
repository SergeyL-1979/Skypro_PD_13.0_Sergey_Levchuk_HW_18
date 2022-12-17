# Skypro_PD_13.0_Sergey_Levchuk_HW_18

Выполнена работа сложной версии (https://github.com/skypro-008/flask-hard-blank)

### Не понял для чего и зачем нужен файл **[constants.py](constants.py)**?
Что в него необходимо добавить? Нужен визуальный пример, как работать с данным файлом
Что например из моего проекто можно перенести в этот файл **constants.py**?
---
*Весь описанный функционал выполнен*

**Допишите код views жанров:**

- [ ]  GET /genres — получить все жанры.
- [ ]  GET /genres/3 — получить жанр по ID.

**Допишите код views режиссеров:**

- [ ]  GET /directors — получить всех режиссеров.
- [ ]  GET /directors/3 — получить режиссера по ID.

**Допишите код views фильмов:**

- [ ]  GET /movies — получить все фильмы.
- [ ]  GET /movies/3 — получить фильм по ID.
- [ ]  GET /movies?director_id=15 — получить все фильмы режиссера.
- [ ]  GET /movies?genre_id=3 — получить все фильмы жанра.
- [ ]  GET /movies?year=2007 — получить все фильмы за год.
- [ ]  POST /movies — создать фильм.
- [ ]  PUT /movies/1 — изменить информацию о фильме.
- [ ]  DELETE /movies/1 — удалить фильм.
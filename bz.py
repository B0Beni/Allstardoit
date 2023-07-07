# SELECT перечень полей FROM имя таблицы
#     WHERE условие
#  PEP-8 phyton enhancement proposal Предложение по улучшению
#  PEP-249 phyton database  API specification Спецификация API базы данных
#  ПОдключение (Connection)- обьект
#  cursor Курсор - обьект с помощью которого производится работа внутри базы данных БД
# execute выполнение
#  ОБРАЩАЕМСЯ К ПОДКЛЮЧЕННОЙ БАЗЕ ДАННЫХ ИЗ ПИТОНА
import sqlite3

# подключаемся
# connection = sqlite3.connect('films_db.sqlite')
# создаем курсор
# cursor = connection.cursor()
# запрос делаем (по правилам 3кавычки ("""   """)) fetchall доставка
# resultat = cursor.execute("""SELECT * FROM films
# WHERE year = 2010""").fetchall()
# (248, 'Алиса в стране чудес', 2010, 13, 201)
# (4382, 'Железный человек 2', 2010, 11, 287)
# (9138, 'Ноттингем', 2010, 11, 188)
# (15495, 'Утомленные солнцем: Предстояние', 2010, 2, 139)
# resultat = cursor.execute("""SELECT * FROM films
# WHERE year = 2010""").fetchone()
# 248
# Алиса в стране чудес
# 2010
# 13
# 201
# resultat = cursor.execute("""SELECT * FROM films
# WHERE year = 2010""").fetchmany(2)
# (248, 'Алиса в стране чудес', 2010, 13, 201)
# (4382, 'Железный человек 2', 2010, 11, 287)
# resultat = cursor.execute("""SELECT * FROM films
# WHERE year = ? AND duration > ?""", (2010, 90)).fetchall()  # можно так
# print(f'найдено {len(resultat)} результатов')
#
# вывод на экран
# for item in resultat:
#     print(item)
# отключение от BD
# connection.close()
# fetchall доставка . метод фетчол доставляет все полученные по запросу элементы
# fetchone только первый элемент
# fetchmany(N) доставляет заданное количество элементов
#

#
# подключаемся или создаем, если не существует такой файл
# connection = sqlite3.connect('films_db.sqlite')
# создаем курсор
# cursor = connection.cursor()
# result = cursor.execute("""INSERT INTO genres VALUES(50, 'Сказки'), (51, 'Басням нет')""")
# подверждение действия без него не работае внизу
# print(result)
# Изменение записей UPDATE апдэйт имя таблицы SET сэт название поля = значение вее WHERE условие
# result = cursor.execute("""UPDATE films SET duration = '283' WHERE title = 'Аватар'""")
# print(result)
# connection.commit()
# отключение от BD
# connection.close()
# удалить из таблицы фильмы до 1900 года
# result = cursor.execute("""DELETE from films year <1900""")

# подключаемся или создаем, если не существует такой файл
connection = sqlite3.connect('shop.sqlite')
cursor = connection.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS users(
userid INT PRIMARY KEY,
fname TEXT,
lname TEXT,
gender TEXT);
""")
cursor.execute("""CREATE TABLE IF NOT EXISTS orders(
orderid INT PRIMARY KEY,
date TEXT,
userid INT,
total INT);
""")
# 1 способ
# cursor.execute("""
# INSERT INTO users (userid, fname, lname, gender)
# VALUES(6, 'BOB', 'AEROMAN', 'male')
# """)
# 2 способ
# user = (7, 'Ro','Man', 'male')
# cursor.execute("""INSERT INTO users VALUES(?, ?, ?, ?)""", user)
# 3 способ
# many_user = [
#     (3, 'Tatyana', 'Reznik', 'female'),
#     (4, 'Tatyta', 'Bo', 'female'),
#     (5, 'Roman', 'Ra', 'male')
# ]
# cursor.executemany("""INSERT INTO users VALUES(?, ?, ?, ?)""", many_user)
# 4 способ в  самой таблице формами
# добавляем покупки
# cursor.execute("""
# INSERT INTO orders(userid, date, userid, total)
# VALUES(1, '12.01.2023', '2', '3000')
# """)
# # 2 способ
# orders = (2, '16.04.2023' ,'1', '1000')
# cursor.execute("""INSERT INTO orders VALUES(?, ?, ?, ?)""", orders)
# # 3 способ
# many_orders = [
#     (3, '16.04.2023', '5', '1000'),
#     (4, '22.05.2023', '3', '500'),
#     (5, '30.06.2023', '1', '2222')
# ]
# cursor.executemany("""INSERT INTO orders VALUES(?, ?, ?, ?)""", many_orders)
# # ниже смотрим  все покупки
result = cursor.execute("""SELECT * FROM orders""").fetchall()
print(result)
# # ниже смотрим покупки конкретного человека
result = cursor.execute("""SELECT fname FROM users""").fetchall()
print(result)
# # ниже смотрим покупки конкретного человека
result = cursor.execute("""SELECT SUM(total) FROM orders
WHERE userid =(
 SELECT userid FROM users WHERE fname = 'Roman')""").fetchall()
print(result)
# # ниже смотрим сумму покупок всех
result = cursor.execute("""SELECT SUM(total) FROM orders
WHERE userid =(
 SELECT userid FROM users)""").fetchall()
print(result)
# выводим имя и фамилии сделавших заказы
result = cursor.execute("""SELECT users.fname, users.lname
FROM orders LEFT JOIN users ON users.userid = orders.userid""").fetchall()
print(result)
#  удаляем все заказы сделанные романом
result = cursor.execute("""DELETE FROM orders
WHERE userid =(
 SELECT userid FROM users WHERE fname = 'Roman')""").fetchall()
#  убить дропом тублицу
cursor.execute("""drop table sozdal""")
print(result)

connection.commit()
connection.close()
# [(None, '12.01.2023', 1, 3000), (2, '16.04.2023', 1, 1000), (4, '22.05.2023', 3, 500), (5, '30.06.2023', 1, 2222)]
# [('BO',), ('Ro',), ('BOB',), ('Ro',), ('Tatyana',), ('Tatyta',), ('Roman',)]
# [(None,)]
# [(6222,)]
# [('BO', 'Beni'), ('BO', 'Beni'), ('Tatyana', 'Reznik'), ('BO', 'Beni')]
# []

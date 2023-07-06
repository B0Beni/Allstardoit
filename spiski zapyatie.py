# Работа с данными
# csv - comm separated values - значения разделенные запятыми
import csv

# with open('sq1.csv', 'w', newline='') as f:
#     writer = csv.writer(f, delimiter=';', quotechar='"',
#                         quoting=csv.QUOTE_MINIMAL)
#     for i in range(10):
#         writer.writerow([i, i ** 2, f'Квадрат числа {i} = {i**2}'])
# with open('sq1.csv', 'r', newline='') as f:
#     reader = csv.reader(f, delimiter=';', quotechar='"')
#     for i in reader:
#         x, y, z = i
#         print(i)  # так себе
#         print(x, y, z)  #  50на50
        # print(z)  # красивый вид

# товар ценаf

# goods = [('Коврик', 300), ('Щетка', 45), ('Ведро оцинкованное', 600),
#          ('Камера велосипедная', 800)]
# with open('sq2.csv', 'w', newline='') as f:
#     reader = csv.writer(f, delimiter=';', quotechar='"',
#                         quoting=csv.QUOTE_MINIMAL)
#     for i in goods:
#         reader.writerow([i])
# goods = [('Коврик', 300), ('Щетка', 45), ('Ведро оцинкованное', 600),
#          ('Камера велосипедная', 800)]
# with open('sq2.csv', 'r', newline='') as f:
#     reader = csv.writer(f, delimiter=';', quotechar='"',
#                         quoting=csv.QUOTE_MINIMAL)
#     for i in goods:
#         goods = i
#         print(i)  # так себе

data = [{
    'lastename': 'Кузнецов',
    'firstname': 'Петруха',
    'class_number': '9',
    'class_letter': 'A'
}, {'lastename': 'Петрухин',
    'firstname': 'Вася',
    'class_number': '9',
    'class_letter': 'B'
}]
with open('form.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=list(data[0].keys()),
                            delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
    writer.writeheader()
    for i in data:
        writer.writerow(i)
with open('form.csv', 'r', newline='') as f:
    reader = csv.DictReader(f, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
    header = next(reader)
    # print(header)
    # print(reader)
    for i in reader:
        for k, v in i.items():
            print(k, v)
# k - ключ 'lastename'
# v - значение 'Петруха'
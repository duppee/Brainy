import sqlite3

# Создание БД
db = sqlite3.connect('Brainy.db')

c = db.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY NOT NULL,
    login text,
    pass text
)""")

c.execute("""CREATE TABLE IF NOT EXISTS subjects(
    id INTEGER PRIMARY KEY NOT NULL,
    name text
)""")

c.execute("""CREATE TABLE IF NOT EXISTS level(
    id INTEGER PRIMARY KEY NOT NULL,
    lvl text
)""")

c.execute("""CREATE TABLE IF NOT EXISTS tests(
    id INTEGER PRIMARY KEY NOT NULL,
    sub_id INTEGER,
    lvl_id INTEGER,
    FOREIGN KEY(lvl_id) REFERENCES level(id),
    FOREIGN KEY(sub_id) REFERENCES subjects(id)
)""")

c.execute("""CREATE TABLE IF NOT EXISTS variant(
    id INTEGER NOT NULL,
    test_id INTEGER,
    question text,
    answer text,
    mis_one text,
    mis_two text,
    mis_three text,
    otv text,
    FOREIGN KEY (test_id) REFERENCES tests (id)
)""")

# Заполнение таблиц с предметами и уровнями сложностями

c.execute("""INSERT INTO subjects(id, name) VALUES(1, 'math')""")
c.execute("""INSERT INTO subjects(id, name) VALUES(2, 'physics')""")
c.execute("""INSERT INTO subjects(id, name) VALUES(3, 'russian')""")
c.execute("""INSERT INTO subjects(id, name) VALUES(4, 'history')""")

c.execute("""INSERT INTO level(id, lvl) VALUES(1, 'easy')""")
c.execute("""INSERT INTO level(id, lvl) VALUES(2, 'normal')""")
c.execute("""INSERT INTO level(id, lvl) VALUES(3, 'hard')""")
c.execute("""INSERT INTO level(id, lvl) VALUES(4, 'crazy')""")


# Создание первого теста(матан)

c.execute("""INSERT INTO tests(id, sub_id, lvl_id) VALUES(1, 1, 1)""")

c.execute("""INSERT INTO variant(id, test_id, question, answer, mis_one, mis_two, mis_three) VALUES(1, 1, 'Во сколько раз надо увеличить число 7, чтобы получилось 2800?', '400', '250', '500', '300')""")
c.execute("""INSERT INTO variant(id, test_id, question, answer, mis_one, mis_two, mis_three) VALUES(2, 1, 'Увеличь 400 в 3 раза', '1200', '1000', '1600', '403')""")
c.execute("""INSERT INTO variant(id, test_id, question, answer, mis_one, mis_two, mis_three) VALUES(3, 1, 'Периметр квадрата 16 см. Чему равна одна сторона?', '4', '16', '8', '2')""")
c.execute("""INSERT INTO variant(id, test_id, question, answer, mis_one, mis_two, mis_three) VALUES(4, 1, 'Машина проехала 240 км за 3 часа. С какой скоротью двигалась машина?', '80', '40', '50', '60')""")
c.execute("""INSERT INTO variant(id, test_id, question, answer, mis_one, mis_two, mis_three) VALUES(5, 1, 'Найдите сумму чисел 2377 и 923.', '3300', '2900', '3500', '3700')""")
c.execute("""INSERT INTO variant(id, test_id, question, answer, mis_one, mis_two, mis_three) VALUES(6, 1, 'Чему равно произведение чисел 35 и 36?', '1260', '71', '1400', '430')""")
c.execute("""INSERT INTO variant(id, test_id, question, answer, mis_one, mis_two, mis_three) VALUES(7, 1, 'Турист прошёл 25км за 5 часов. С какой скоростью шёл турист?(км/ч)', '5', '15', '3', '8')""")
c.execute("""INSERT INTO variant(id, test_id, question, answer, mis_one, mis_two, mis_three) VALUES(8, 1, 'Найдите периметр прямоугольника со сторонами 13 и 17.', '60', '30', '40', '80')""")
c.execute("""INSERT INTO variant(id, test_id, question, answer, mis_one, mis_two, mis_three) VALUES(9, 1, 'Какое число получится при делении 2849 на 7?', '407', '338', '417', '377')""")
c.execute("""INSERT INTO variant(id, test_id, question, answer, mis_one, mis_two, mis_three) VALUES(10, 1, 'Найдите площадь квадрата со стороной 21.', '441', '84', '444', '121')""")

# второй тест(матан)

c.execute("""INSERT INTO tests(id, sub_id, lvl_id) VALUES(2, 1, 2)""")

c.execute("""INSERT INTO variant(id, test_id, question, answer, mis_one, mis_two, mis_three) VALUES(1, 2, 'Найди число, если 7/8 его равны 56', '64', '68', '60', '62')""")
c.execute("""INSERT INTO variant(id, test_id, question, answer, mis_one, mis_two, mis_three) VALUES(2, 2, 'Отец в 4 раза старше дочери, а 3 года назад он был в 5 раз старше дочери.Сколько лет отцу?', '48', '40', '44', '42')""")
c.execute("""INSERT INTO variant(id, test_id, question, answer, mis_one, mis_two, mis_three) VALUES(3, 2, 'Сумма двух чисел 32, причём первое слагаемое в 3 раза больше, чем второе.На сколько первое число больше чем второе?', '16', '24', '8', '4')""")
c.execute("""INSERT INTO variant(id, test_id, question, answer, mis_one, mis_two, mis_three) VALUES(4, 2, 'Маша задумала число.Если к этому числу прибавить 16,а к полученной сумме прибавить 87,то получится 134.Какое число задумала Маша?', '31', '30', '28', '32')""")
c.execute("""INSERT INTO variant(id, test_id, question, answer, mis_one, mis_two, mis_three) VALUES(5, 2, 'Подели 46 на 100', '0.46', '460', '4600', '4.6')""")
c.execute("""INSERT INTO variant(id, test_id, question, answer, mis_one, mis_two, mis_three) VALUES(6, 2, 'Умножь 19 на 0.1', '1.9', '190', '0.19', '19.1')""")
c.execute("""INSERT INTO variant(id, test_id, question, answer, mis_one, mis_two, mis_three) VALUES(7, 2, 'На улице 40 домов, 20% из них - кирпичные. Сколько кирпичных домов на улице?', '8', '10', '7', '6')""")
c.execute("""INSERT INTO variant(id, test_id, question, answer, mis_one, mis_two, mis_three) VALUES(8, 2, 'В саду 200 яблонь и вишен. Яблони составляют 35% всех деревьев. Сколько вишен в саду?', '130', '70', '165', '60')""")
c.execute("""INSERT INTO variant(id, test_id, question, answer, mis_one, mis_two, mis_three) VALUES(9, 2, 'Товар на распродаже уценили на 20%, при этом он стал стоить 1680 р. Сколько стоил товар до распродажи?', '2100', '1700', '1800', '2400')""")
c.execute("""INSERT INTO variant(id, test_id, question, answer, mis_one, mis_two, mis_three) VALUES(10, 2, 'Если 25% выпускников сдали все экзамены на отлично. Сколько всего выпускников, если отличников 40 человек?', '160', '180', '200', '175')""")


# третий тест(физика уже будет)

c.execute("""INSERT INTO tests(id, sub_id, lvl_id) VALUES(3, 2, 1)""")

c.execute("""INSERT INTO variant(id, test_id, question, answer, mis_one, mis_two, mis_three) VALUES(1, 3, 'Скорость движения автомобиля за 40 с возросла от 5 м/с до 15 м/с. Определите ускорение автомобиля.(м/с^2)', '0.25', '0.3', '0.40', '0.32')""")
c.execute("""INSERT INTO variant(id, test_id, question, answer, mis_one, mis_two, mis_three) VALUES(2, 3, 'Какую скорость приобретает отходящий от станции поезд через 7 с от начала движения, если его ускорение равно 0,9 м/с2? (м/с)', '6.3', '6', '5.5', '5.8')""")
c.execute("""INSERT INTO variant(id, test_id, question, answer, mis_one, mis_two, mis_three) VALUES(3, 3, 'Ласточка летит со скоростью 36 км/ч. Какой путь она преодолеет за 0,5 ч? (км)', '18', '36', '9', '12')""")
c.execute("""INSERT INTO variant(id, test_id, question, answer, mis_one, mis_two, mis_three) VALUES(4, 3, 'Конькобежец может развивать скорость до 13 м/с. За какое время он пробежит дистанцию длиной 2,6 км? (с)', '200', '210', '215', '220')""")
c.execute("""INSERT INTO variant(id, test_id, question, answer, mis_one, mis_two, mis_three) VALUES(5, 3, 'Определите среднюю скорость движения плота, если за 20 минут он переместился на 900 м. (км/ч)', '2.7', '2.6', '2.4', '2.2')""")
c.execute("""INSERT INTO variant(id, test_id, question, answer, mis_one, mis_two, mis_three) VALUES(6, 3, 'Автомобиль двигается со скоростью 80 км/ч. Сколько километров он проедет за 3 часа?', '240', '160', '220', '180')""")
c.execute("""INSERT INTO variant(id, test_id, question, answer, mis_one, mis_two, mis_three) VALUES(7, 3, 'На автомобиле за 3 часа проехали 180 км с одной и той же скоростью. Чему равна скорость автомобиля? (км/ч)', '60', '80', '40', '45')""")
c.execute("""INSERT INTO variant(id, test_id, question, answer, mis_one, mis_two, mis_three) VALUES(8, 3, 'Вертолет преодолел расстояние в 600 км со скоростью 120 км/ч. Сколько времени он был в полете?(ч)', '5', '4', '3', '7')""")
c.execute("""INSERT INTO variant(id, test_id, question, answer, mis_one, mis_two, mis_three) VALUES(9, 3, 'Вертолет летел 6 часов со скоростью 160 км/ч. Какое расстояние он преодолел за это время? (км)', '960', '840', '1020', '1140')""")
c.execute("""INSERT INTO variant(id, test_id, question, answer, mis_one, mis_two, mis_three) VALUES(10, 3, 'Пуля, выпущенная из винтовки, долетела до цели, находящейся на расстоянии 1 км, за 2.5 секунды. Найдите скорость пули. (м/с)', '400', '600', '800', '300')""")




c.execute("""INSERT INTO users(login, pass) VALUES('Karl', 'asdf1234')""")


db.commit()
db.close()

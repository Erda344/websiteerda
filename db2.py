import sqlite3
from random import randint

def create_db2():
    '''Создает базу данных и таблицу
    questions где будут храниться все вопросы и ответы
    на приложение "викторина"'''
    conn = sqlite3.connect('database2.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY,
        question VARCHAR,
        answer VARCHAR,
        wrong1 VARCHAR,
        wrong2 VARCHAR,
        wrong3 VARCHAR)''')
    conn.commit()
    cursor.close()
    conn.close()

def insert_db2():
    '''Вставляет вопросы в базу данных'''
    conn = sqlite3.connect('database2.db')
    cursor = conn.cursor()
    questions = [
        ('Кого из птиц называют санитаром леса?', 'Дятла', 'Синицу', 'Сову', 'Кукушку'),
        ('Какая страна самая большая?', 'Россия', 'Казахстан', 'США', 'Китай'),
        ('Кого называют «царь зверей»?', 'Льва', 'Медведя', 'Тигра', 'Слона'),
        ('Сколько лапок у паука?', '8', '6', '10', '4'),
        ('Где правили фараоны?', 'Египет', 'Аляска', 'Бразилия', 'Австралия'),
        ('Сколько классов в начальной школе?', '4', '8', '2', '1')
    ]
    cursor.executemany('''INSERT INTO questions (question, answer, wrong1, wrong2, wrong3) VALUES (?,?,?,?,?)''', questions)
    conn.commit()
    cursor.close()
    conn.close()

def clear_db2():
    '''Удаляет таблицу из базы данных'''
    conn = sqlite3.connect('database2.db')
    cursor = conn.cursor()
    cursor.execute('''DROP TABLE IF EXISTS questions''')
    conn.commit()
    cursor.close()
    conn.close()

def get_random_question_db2():
    '''Функция возвращает 1 случайное поле
    с вопросом, ответом и 3 неправильных ответа'''
    conn = sqlite3.connect('database2.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM questions''')
    all_data = cursor.fetchall()
    result = all_data[randint(0, len(all_data)-1)]
    conn.commit()
    cursor.close()
    conn.close()
    return result
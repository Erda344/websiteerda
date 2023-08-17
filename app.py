from flask import Flask, render_template
import db
import db2

db.clear_db()
db.create()
db.insert_db()

db2.clear_db2()
db2.create_db2()
db2.insert_db2()

# Создаем объект нашего приложения
app = Flask(__name__)

@app.route('/')
def index():
    '''Функция возвращает html документ
    когда мы обращаемся на главную страницу ('/') '''
    return render_template('index.html')

@app.route('/test')
def test():
    result = db.get_random_question()
    question = result[1]
    answer = result[2]
    wrong1 = result[3]
    wrong2 = result[4]
    wrong3 = result[5]
    return render_template(
        'test.html',
        question = question,
        answer=answer,
        wrong1=wrong1,
        wrong2=wrong2,
        wrong3=wrong3
    )

@app.route('/test2')
def test2():
    result = db2.get_random_question_db2()
    question_db2 = result[1]
    answer_db2 = result[2]
    wrong1_db2 = result[3]
    wrong2_db2 = result[4]
    wrong3_db2 = result[5]
    return render_template(
        'test2.html',
        question_db2 = question_db2,
        answer_db2=answer_db2,
        wrong1_db2=wrong1_db2,
        wrong2_db2=wrong2_db2,
        wrong3_db2=wrong3_db2
    )

# Если это главный файл - запусти приложение
if __name__ == "__main__":
    app.run()
from flask import Flask, session, redirect, url_for, render_template

def sotrydniki_():
    sotrydniki = {
        "Отдел разработки:": {
            "Главный разработчик": "Фёдоров Руслан",
            "Младший разработчик": ["Иванова Ирина", "Васильев Михаил", "Мальцев Егор"],
            "Тестировщик": ["Романов Пётр", "Потёмкин Ян"]
        },
        "Бухгалтерия:": {
            "Старший бухгалтер": "Петров Иван",
            "Бухгалтер": ["Антонова Ольга", "Коркина Мария"]
        }
    }
    return render_template("sotrudniki.html", sotrydniki = sotrydniki)



app = Flask(__name__)  
app.add_url_rule('/', 'sotrydniki_', sotrydniki_)   # создаёт правило для URL '/'

if __name__ == '__main__':
    app.run()

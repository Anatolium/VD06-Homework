from flask import render_template, request, redirect, url_for

from app import app

# этот список будем заполнять словарями
posts = []

@app.route("/", methods=["GET", "POST"])
def index():
    # используем метод POST, так как информация будет отправляться; request.method сравнивает данные с HTTP-запросом
    if request.method == 'POST':
        # функция request.form извлекает значение из соответствующих полей
        title = request.form.get('title')
        content = request.form.get('content')
        # создаём условие для проверки наличия данных в полях title и content
        if title and content:
            posts.append({'title': title, 'content': content})
            # используем для обновления страницы и предотвращения повторной отправки формы; index – имя этой функции;
            # перенаправляем пользователя на url, связанный с функцией index, то есть снова заходим на страницу,
            # на которой были
            return redirect(url_for('index'))

    # возвращаем отрендеренный шаблон с переданными данными постов
    # posts будет подставляться в строку {% for post in posts %} в user_data_form.html
    return render_template('user_data_form.html', posts=posts)

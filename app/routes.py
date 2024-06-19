from flask import render_template, request, redirect, url_for

from app import app

posts = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        # функция request.form.get извлекает значение из соответствующих полей
        user = request.form.get('user')
        age = request.form.get('age')
        city = request.form.get('city')
        hobby = request.form.get('hobby')
        if user and age and city:
            posts.append({'user': user, 'age': age, 'city': city, 'hobby': hobby})
            # перезаходим на страницу: обновляем её и предотвращаем повторную отправку формы
            # (перенаправляем пользователя на url, связанный с данной функцией index)
            return redirect(url_for('index'))

    # возвращаем шаблон с переданными данными постов;
    # список posts будет подставляться в строку {% for post in posts %} в user_data_form.html
    return render_template('user_data_form.html', posts=posts)

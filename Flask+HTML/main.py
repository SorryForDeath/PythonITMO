from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# Отображаем HTML-страницу
@app.route('/')
def index():
    return render_template('htmlka.html')

# Эндпоинт для сложения
@app.route('/add', methods=['POST'])
def add():
    try:
        # Получаем данные из формы
        a = float(request.form.get('a', 0))
        b = float(request.form.get('b', 0))
    except ValueError:
        return jsonify({'error': 'Параметры a и b должны быть числами'}), 400

    # Вычисляем сумму
    result = a + b

    # Возвращаем результат в формате JSON
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
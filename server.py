import gunicorn
from flask import Flask, request, Response
from ai.yandex_gpt import generate_text

app = Flask(__name__)


@app.route('/api/generate')
def generate():
    prompt = request.args.get('prompt')
    if not prompt:
        return "Нет запроса", 400
    try:
        response = generate_text(prompt)
        return Response(response, content_type='text/html; charset=utf-8')

    except Exception as e:
        print("Ошибка при генерации текста:", str(e))
        return "Ошибка сервера", 500



@app.route('/')
def home():
    html = open('./index.html', encoding='utf-8').read()
    return Response(html, content_type='text/html; charset=utf-8')

@app.route('/api/api')
def api():
    return f"<p>Это API </p>"


if __name__ == '__main__':
    #app.run()# локально
    app.run(host='0.0.0.0', port=8080)# на хостинге



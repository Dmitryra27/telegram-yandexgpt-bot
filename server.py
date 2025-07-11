from flask import Flask, request
from ai.yandex_gpt import generate_text

app = Flask(__name__)


@app.route('/api/generate')
def generate():
    prompt = request.args.get('prompt')
    if not prompt:
        return "Нет запроса", 400
    return generate_text(prompt)


@app.route('/')
def home():
    return open('webapp/index.html').read()


if __name__ == '__main__':
    app.run()

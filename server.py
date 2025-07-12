import os
from flask import Flask, request, Response, jsonify
from ai.yandex_gpt import generate_text

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"Welcome to your Flask app !!"})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Привет, это моё приложение на Render!</h1><p>Работает на моём собственном сервере!</p>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

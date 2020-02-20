from flask import Flask

app = Flask(__name__)

@app.route('/')
def defaultHit():
    return "server working fine"


@app.route('/hello')
def hello():
    return "hello world"

if __name__ == '__main__':
    app.run(debug=True)
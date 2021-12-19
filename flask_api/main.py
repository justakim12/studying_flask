from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/user')
def hello_user():
    return 'Hello, User!'


@app.route('/user/<userName>')
def hello_specific_user(userName):
    return 'Hello, %s'%(userName)


if __name__ == "__main__":
    app.run()

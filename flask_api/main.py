from flask import Flask
import json


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


@app.route('/json')
def json_dump():
    return json.dumps({'name': 'david',
                       'email': 'david@naver.com'})


if __name__ == "__main__":
    app.run()

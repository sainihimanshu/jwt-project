from flask import Flask, g, request
from response import Response
from models import database, User


class JWT:

    def __init__(self):
        pass

    def encode(self):
        pass

    def decode(self):
        pass

app = Flask(__name__)


@app.before_request
def before_request():
    g.db = database
    g.db.connect()


@app.after_request
def after_request(response):
    g.db.close()
    return response


@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username', None)
    password = request.form.get('password', None)

    if username and password:
        if User.select().where(User.username == username).count() > 0:
            return Response().msg('Username already taken', 400)
        User.create(username=username, password=password)
        return Response().msg('Welcome to jwt project ' + username, 200)

    return Response().msg('Username and password are required', 400)


@app.route('/authenticate', methods=['POST'])
def authenticate():
    username = request.form.get('username', None)
    password = request.form.get('password', None)

    if username and password:  
        try:   
            _user = User.get(User.username == username)
            if _user.password == password:
                return Response().msg('cool, will get a token soon')
        except:
            pass
        return Response().msg('Username or password invalid', 400)
    
    return Response().msg('Username and password are required', 400)

@app.route('/refresh-token', methods=['POST'])
def refresh_token():
    pass


@app.route('/secure', methods=['GET'])
def secure():
    pass


@app.route('/insecure', methods=['GET'])
def insecure():
    pass

if __name__ == '__main__':
    app.run(debug=True)

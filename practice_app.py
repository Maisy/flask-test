from flask import Flask
from flask import render_template
from flask import request
from app.logging_config import setup_logger

app = Flask(__name__)
logger = setup_logger()

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    
    # ?key=value를 사용할때는
    searchword = request.args.get('key', '')
    logger.info(searchword)

    # 아래의 코드는 요청이 GET 이거나, 인증정보가 잘못됐을때 실행된다.
    # return render_template('login.html', error=error)
    return 'login.html template does not exist'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/projects/') # /project로 입력해도 /projects/로 고쳐줌
def projects():
    return 'The project page'

@app.route('/about') # /about/ 요청 시 404
def about():
    return 'The about page'





if __name__ == '__main__':
    app.debug = True # 개발모드
    app.run()
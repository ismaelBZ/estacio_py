
# from flask import Flask, request
#
# app = Flask(__name__)
# app.debug = True
#
#
# @app.route('/login', methods=['GET', 'POST'])
# def login_page():
#     if request.method == 'POST':
#         return '<h1>Logout</h1>'
#     else:
#         return'<h1>Login</h1>'
#
# if __name__ == '__main__':
#     app.run()



# from flask import Flask
# app = Flask(__name__)
# @app.route('/')
# def home():
#     hello = '<h1>Hello!</h1>'
#     redirect = '<p>Go to <a href="/login">Login</a></p>'
#     return hello + redirect
#
# @app.route('/login')
# def login():
#     return '<p><a href="/">Back Home<a><p>'
#
# if __name__ == "__main__":
#     app.run()



# from flask import Flask
#
# app = Flask(__name__)
#
# @app.route('/')
# @app.route('/<name>')
# def home(name=""):
#     if name:
#         return '<h1>Olá ' + name + '. Senti saudades!</h1>'
#     else:
#         return '<h1>Olá, seja bem vindo!</h1>'
#
# if __name__ == '__main__':
#     app.run()



# from flask import Flask
#
# app = Flask(__name__)
#
# @app.route('/')
# def home():
#     return '<h1>Seja bem vindo!'
#
# @app.route('/<name>')
# def logged(name):
#     return '<h1>Senti saudades ' + name
#
# if __name__ == '__main__':
#     app.run()



# from flask import Flask
#
# app = Flask(__name__)
#
# @app.route('/')
# def home_page():
#     return '<h1>Home Page</h1>'
#
# @app.route('/login')
# def login():
#     return '<h1>Login</h1>'
#
# if __name__ == '__main__':
#     app.run()

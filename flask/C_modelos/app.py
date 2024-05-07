from flask import Flask, render_template

app = Flask(__name__)
app.debug = True

isLogged = True

@app.route('/')
@app.route('/<name>')
def home(name=""):
    return render_template('indice.html', name=name, isLogged=isLogged)

if __name__ == '__main__':
    app.run()


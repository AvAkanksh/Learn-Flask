from flask import Flask

app = Flask(__name__)


@app.route('/home')
@app.route('/')
def hello():
    return '<h1>Hello hi text</h1>'

@app.route('/about')
def ab():
    return '<h1>About hello Page</h1>'


if(__name__ == '__main__'):
    app.run(debug=True)
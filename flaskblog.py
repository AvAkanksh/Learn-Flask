from flask import Flask , render_template , url_for

app = Flask(__name__)


posts = [
    {
        'author'    : 'Akanksh',
        'title'     : 'Blog Post 1',
        'content'   : 'First post content',
        'date_posted': ' June 11 , 2021'
    },
    {
        'author'    : 'Akshitha',
        'title'     : 'Blog Post 2',
        'content'   : 'Second post content',
        'date_posted': ' June 10 , 2021'
    }
]


@app.route('/home')
@app.route('/')
def home():
    return render_template('home.html', posts = posts, title='Home')

@app.route('/about')
def about():
    return render_template('about.html', title='About')


if(__name__ == '__main__'):
    app.run(debug=True)
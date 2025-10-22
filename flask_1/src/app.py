# Go to address http://127.0.0.1:5000/ to see the Flask app in action.

from flask import Flask

app = Flask(__name__)

print(app)
print(__name__)

def make_bold(fn):
    def wrapper(*args, **kwargs):
        return f'<b>{fn(*args, **kwargs)}</b>'
    return wrapper

def make_emphasis(fn):
    def wrapper(*args, **kwargs):
        return f'<em>{fn(*args, **kwargs)}</em>'
    return wrapper

def make_underlined(fn):
    def wrapper(*args, **kwargs):
        return f'<u>{fn(*args, **kwargs)}</u>'
    return wrapper

@app.route('/', endpoint='home_page')
@make_emphasis
@make_underlined
@make_bold
def homepage():
    return 'Home Page'

@app.route('/namenum/<string:name>/<int:num>', endpoint='namenum_page')
@make_emphasis
@make_underlined
@make_bold
def namenum(name, num):
    return f'Your name is {name}, your number is {num}.'

@app.route('/wholepath/<path:val>', endpoint='wholepath_page')
@make_emphasis
@make_underlined
@make_bold
def wholepath(val):
    return f'This is the whole path you wrote: {val}.'

@app.route('/returnhtml')
def returnhtml():
    return '<h1 style="text-align: center">Hello, there!</h1> \
        <p>This is a paragraph.</p> \
        <img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2' \
            'F%2Fmedia.tenor.com%2FlWlcmRdqshwAAAAd%2Fkenobi-hello-there-' \
                'meme.gif&f=1&nofb=1&ipt=19a41387df383623f2889f03df72f9a941' \
                    'd066a961f8d0aa891da874f9b6fc02" width=200\>'

if __name__ == '__main__':
    # Get access to Flask debugger with debug=True
    app.run(debug=True)

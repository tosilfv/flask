# Go to address http://127.0.0.1:5000/ to see the Flask app in action.

from flask import Flask

app = Flask(__name__)

print(app)
print(__name__)

@app.route('/')
def homepage():
    return 'Home Page'

@app.route('/test')
def test():
    return 'test'

if __name__ == '__main__':
    app.run()

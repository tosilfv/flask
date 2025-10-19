# Go to address http://127.0.0.1:5000/ to see the Flask app in action.

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/test')
def test():
    return 'test'

if __name__ == '__main__':
    app.run(debug=True)
 
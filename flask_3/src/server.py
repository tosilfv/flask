import random, datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.datetime.now().year
    return render_template('index.html', rand_num = random_number, \
                           cur_y=current_year)

if __name__ == '__main__':
    app.run(debug=True)

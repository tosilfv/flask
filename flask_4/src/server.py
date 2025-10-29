from flask import Flask, render_template

app = Flask(__name__)
items = [
            {
                "title": "title_one",
                "author": "author_one"
            },
            {
                "title": "title_two",
                "author": "author_two"
            },
            {
                "title": "title_three",
                "author": "author_three"
            }
        ]

@app.route('/')
def home():
    return render_template('index.html', list_items=items, person_name="")

@app.route('/person/<name>')
def one_person(name):
    return render_template('index.html', person_name=name)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, url_for

app = Flask(__name__)

@app.route('/greeting/<name>')
def give_greeting(name):
    return 'Hello, {0}!'.format(name)


if __name__ == "__main__":
    app.run(debug=True)


#http://www.example.org/greeting/Mark
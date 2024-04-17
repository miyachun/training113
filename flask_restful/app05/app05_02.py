from flask import Flask, url_for

app = Flask(__name__)


def give_greeting(name):
    return 'Hello, {0}!'.format(name)

app.add_url_rule('/greeting/<name>', 'give_greeting', give_greeting)

if __name__ == "__main__":
    app.run(debug=True)


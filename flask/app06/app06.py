from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/")
def form():
    return render_template('index.html')


@app.route("/submit", methods=['POST'])
def submit():
    firstname = request.values['firstname']
    lastname = request.values['lastname']
    return render_template('submit.html',**locals())

if __name__ == '__main__':
   app.run(debug = True)
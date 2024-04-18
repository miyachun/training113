from flask import Flask, Blueprint
from admin import admin
from user import user

app = Flask(__name__)
app.register_blueprint(admin, url_prefix='/admin')
app.register_blueprint(user, url_prefix='/user')

if __name__ == "__main__":
    app.run(debug=True)

#http://www.example.org/admin/greeting
#http://www.example.org/user/greeting
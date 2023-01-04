from flask import Flask


app = Flask(__name__)

app.route('/')
def index1() :
    return 'git.'

from mod_admin import admin

app.register_blueprint(admin)
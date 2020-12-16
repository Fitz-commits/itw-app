from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from helper import links

app = Flask(__name__)
app.config['SECRET_KEY'] = '\xc0\x86x\xf6\x7f\xbac\xfa\xcc\x1a\x1c\xf7\xe2 IR\xf2^\xa3J\t`\x8a\xf8'

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', template_links=links)

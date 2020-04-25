from flask import Flask
from model.models import t_m_company
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/demo1')
def ddd():
    return 'Hello ddWorld!'
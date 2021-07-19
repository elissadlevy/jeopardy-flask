# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
import model
import modelQuestion


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    categoryList = model.categoryList
    return render_template("index.html",categoryList = categoryList)

@app.route('/questionview', methods = ['GET', 'POST'])
def questionview():
    catChoice = request.form['category']
    question = modelQuestion.getQuestion(catChoice)["question"]
    return render_template("questionview.html", question=question)

@app.route('/answerview', methods = ['GET', 'POST'])
def answerview():
    return render_template("answerview.html")
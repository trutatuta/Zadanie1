from flask import Flask, render_template, redirect, url_for, session
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired
import os


app = Flask(__name__)
app.config["SECRET_KEY"] = "super secrect key by bohdan hrybinchyk"

bootstrap = Bootstrap(app)


class NumberForm(FlaskForm):
    number = IntegerField("Which fibonacci number?", validators=[DataRequired()])
    submit = SubmitField("Submit")

def fib(n):
   if n <= 1:
       return (n)
   else:
       return (fib(n-1) + fib(n-2))


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("home.html")

@app.route('/calc', methods=['GET', 'POST'])
def fib_calc():
    form = NumberForm()
    if form.validate_on_submit():
        session["number"] = fib(form.number.data)
        return redirect(url_for("fib_calc"))
    return render_template("index.html", number=session.get("number"), form=form)



if __name__ == "__main__":
    app.run(debug=True)



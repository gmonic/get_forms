from flask import Flask, render_template, request
import requests
import tweepy, json
import pandas
from geopy.geocoders import Nominatim
from wtforms import Form, BooleanField, StringField, validators, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from flask_wtf.csrf import CSRFProtect

app = Flask("My_App")
csrf = CSRFProtect(app)




#create form 1
class Form1(FlaskForm):
    name = StringField('name')
    submit1 = SubmitField('submit')

#create form 2
class Form2(FlaskForm):
    age = StringField('age')
    submit2 = SubmitField('submit')

#create homepage
@app.route("/")
def my_form():
    form1 = Form1()
    form2 = Form2()
    return render_template('result.html', form1=form1, form2=form2)

#handle both forms
@app.route("/subscribe", methods=['POST'])
def register():
    form1 = Form1()
    form2 = Form2()
    if form1.submit1.data and form1.validate():
        user_name = form1.name.data
        return render_template('result.html', form1=form1, form2=form2, user_name=user_name)
    elif form2.submit2.data and form2.validate():
        user_age = form2.age.data
        return render_template('result.html', form1=form1, form2=form2, user_age=user_age)
    else:
        return render_template('result.html', form1=form1, form2=form2)

app.run(debug=True)

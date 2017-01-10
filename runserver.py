import os
import time
from datetime import timedelta

from flask import Flask, render_template, flash, request, redirect, session, abort
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

from amazonapi import Amazonapi
from ebay_api import EbayApi
from table_look_up import LookTables


# App config. 
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = os.urandom(12)




@app.route("/", methods=['POST','GET'])
def output():
    look_products = LookTables()
    amazon_products = look_products.look_table_amazon()
    ebay_products = look_products.look_table_ebay()
    return render_template('products.html',amazon = amazon_products, ebay = ebay_products)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
    #app.run(debug=True,host='127.0.0.1',port=5000)


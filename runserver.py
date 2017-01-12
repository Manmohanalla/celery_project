'''
Flask Rendering
'''
import os

from flask import Flask, render_template

from table_look_up import LookTables

'''
App config.
'''
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = os.urandom(12)


@app.route("/", methods=['POST', 'GET'])
def output():
    '''
    function to render the page from database
    '''
    look_products = LookTables()
    amazon_products = look_products.look_table_amazon()
    ebay_products = look_products.look_table_ebay()
    return render_template('products.html', amazon=amazon_products, ebay=ebay_products)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
    #app.run(debug=True,host='127.0.0.1',port=5000)

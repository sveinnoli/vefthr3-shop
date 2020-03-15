from flask import Flask, session, render_template, request
import os
app = Flask(__name__)

#Session key
app.config['SECRET_KEY'] = os.urandom(24).hex()

#products in shop 
#NOTE keep prices in int, figure out another time how to convert it from str to int
products = {"wares":[
            {"price":4000, "product":"shirt", "image":"/static/images/shirt1.jpg","id":os.urandom(10).hex()},
            {"price":3500, "product":"shoes", "image":"/static/images/shoes1.jpg","id":os.urandom(10).hex()},
            {"price":5000, "product":"pants", "image":"/static/images/pants1.jpg","id":os.urandom(10).hex()},
            {"price":7500, "product":"shoes", "image":"/static/images/shoes2.jpg","id":os.urandom(10).hex()}
            ]}


@app.route('/', methods=['GET','POST'])
def index():
    return render_template("shop.html", products=products, session=session)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
	app.run(debug=True)
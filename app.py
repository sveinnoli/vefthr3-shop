import os
from flask import Flask, session, render_template, request, redirect
app = Flask(__name__)

#Session key
app.config['SECRET_KEY'] = os.urandom(24).hex()

#NOTE keep prices in int, figure out another time how to convert it from str to int

#Add type for shoes and product for product name e.g: shirt, wizliz or something of the sort
products = {"wares":[
            {"price":4000, "product":"shirt", "image":"/static/images/shirt1.jpg","id":os.urandom(10).hex()},
            {"price":3500, "product":"shoes", "image":"/static/images/shoes1.jpg","id":os.urandom(10).hex()},
            {"price":5000, "product":"pants", "image":"/static/images/pants1.jpg","id":os.urandom(10).hex()},
            {"price":7500, "product":"shoes", "image":"/static/images/shoes2.jpg","id":os.urandom(10).hex()},
            ]}
#functions
def add_to_cart(product_id):
    for item in products["wares"]:
        for key, value in item.items():
            if key == "id" and value == product_id:
                #Bug in session caching dosen't allow you to append it, recreate session instance and append it back to session
                temp_session = session["wares"]
                temp_session.append(item)
                session["wares"] = temp_session

@app.route('/', methods=['GET','POST'])
def store():
    if "wares" not in session:
        session["wares"] = []
    if request.method == 'POST': #Catches submit form. 
        product_id = request.form['add_to_cart']
        add_to_cart(product_id)           
        return render_template("shop.html", products=products, session=session)
    else:
        return render_template("shop.html", products=products, session=session)

@app.route('/checkout', methods=['GET','POST'])
def checkout():
    return render_template("checkout.html", session=session)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
	app.run(debug=True)
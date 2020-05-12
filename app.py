import os
from flask import Flask, session, render_template, request, redirect, url_for
app = Flask(__name__)

#Session key
app.config['SECRET_KEY'] = os.urandom(24).hex()

#NOTE keep prices in int, figure out another time how to convert it from str to int

#Add type for shoes and product for product name e.g: shirt, wizliz or something of the sort
products = {"wares":[
    {os.urandom(10).hex():{"price":4000, "product":"shirt", "image":"/static/images/shirt1.jpg"}},
    {os.urandom(10).hex():{"price":3500, "product":"shoes", "image":"/static/images/shoes1.jpg"}},
    {os.urandom(10).hex():{"price":5000, "product":"pants", "image":"/static/images/pants1.jpg"}},
    {os.urandom(10).hex():{"price":7500, "product":"shoes", "image":"/static/images/shoes2.jpg"}},
]}

def add_to_cart(product_id):
    for item in products["wares"]:
        for key, value in item.items():
            if key == product_id:
                temp_session = session["wares"]
                temp_session.append(item)
                session["wares"] = temp_session

def update_cart():
    if len (session["wares"]) > 0:
        for x in range(len(session["wares"])):
            for key, value in session["wares"][x].items():
                session["wares"][x][key].update({"num":x})

# print("session_wares: {}\nitem: {}\nkey: {}\nvalue: {}\n".format(session["wares"], item, key, value))
def remove_from_cart(product_id, product_num):
    for item in session["wares"]:
        for key, value in item.items():
            if key == product_id and int(product_num) == int(value["num"]):
                session["wares"].pop(int(product_num))
                return session["wares"]

def sum_price():
    price = 0
    for item in session["wares"]:
        for key, value in item.items():
            price = price + value["price"]
    print(price)
    return price

@app.route('/', methods=['GET','POST'])
def store():
    session["purchase"] = False
    if "wares" not in session:
        session["wares"] = []
    if request.method == 'POST': #Catches submit form. 
        product_id = request.form['add_to_cart']
        add_to_cart(product_id)  
        update_cart()         
        return redirect(url_for("store"))
    else:
        return render_template("shop.html", products=products, session=session)


@app.route('/checkout', methods=['GET','POST'])
def checkout():
    if "wares" not in session:
        session["wares"] = []
    if request.method == 'POST' and 'remove' in request.form or "num" in request.form:
        product_id = request.form['remove']
        product_num = request.form['num']
        session["wares"] = remove_from_cart(product_id, product_num)
        update_cart()
        return redirect(url_for("checkout"))
    if request.method == 'POST' and "purchase" in request.form:
        session.pop("wares", None)
        session["wares"] = []
        session["purchase"] = True
        name = request.form["name"]
        email = request.form["email"]
        session["user_id"] = {"name":name, "email":email}
        return redirect(url_for("checkout"))
    return render_template("checkout.html", session=session, price=sum_price())


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
	app.run(debug=True)


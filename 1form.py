from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
	return render_template("form.html")

#import this code to app.py
@app.route('/info', methods=['GET','POST'])
def info():
    #add if statement to make sure Session ID is valid for product purchases.
    if request.method == 'POST': #Catches submit form. 
        nafn = request.form['name'] 
        netfang = request.form['email']
        print(nafn)
        print(netfang)
        return "Góðan dag og velkomin"
    else:
        return "<h1>Villa!</h1>"

if __name__ == "__main__":
	app.run(debug=True)
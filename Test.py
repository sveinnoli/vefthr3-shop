from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/info', methods=['GET','POST'])
def info():
    if request.method == 'POST':
        nafn = request.form['name']
        netfang = request.form['email']
        print(nafn)
        print(netfang)
        return "Góðan dag og velkomin"
    else:
        return "<h1>Má ekki !</h1>"

if __name__ == "__main__":
	app.run(debug=True)
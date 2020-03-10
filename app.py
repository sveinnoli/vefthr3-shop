from flask import Flask, session, render_template, request
import os
app = Flask(__name__)

#Session key
app.config['SECRET_KEY'] = os.urandom(24)
#Store cart seperately from session but append any data into session if they click purchase on a product

#Data -- Figure out how to use session to store data, 
session = {"wares":[{"price":"3500", "product":"shirt"}, {"price":"4000", "product":"shoes"}]}
text = ""
visited = False

def info():
    exit()

@app.route('/')
def index():
	return render_template("shop.html")

# Activates session
@app.route('/on')
def sessionon():
    if "hilmir" in session:
        text="Session already ON"
    else:
        session['hilmir'] = 'GALVEZ'
        session["testing"] = "working"
        print(session)
        text = "Session is now SET"
    return render_template("shop.html", text=text, session=session)

# Deletes session
@app.route('/off')
def sessionoff():
    if 'hilmir' in session:
        session.pop('hilmir', None)
        text="Session poped"
    else:
        text="Session was not set"
    return render_template("shop.html", text=text)

# Checks for session
@app.route('/check')
def checksession():
    if 'hilmir' in session:
        text="ON"
    else:
        text="OFF"
    return render_template("shop.html", text=text)


#Others
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
	app.run(debug=True)
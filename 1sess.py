# Verðum að importa session
from flask import Flask, session
app = Flask(__name__)

#Session key
app.config['SECRET_KEY'] = "temp"

@app.route('/')
def index():
	return '<h3><a href="/on">Set session</a></h3><h3><a href="/off">Delete session</a></h3><h3><a href="/check">Check session</a></h3>'

#session on
@app.route('/on')
def sessionon():
    session['hilmir'] = 'GALVEZ'
    return '<h3>Session ON</h3><h3><a href="/">Home</a></h3>'

# Deletes session
@app.route('/off')
def sessionoff():
    if 'hilmir' in session:
        print("before: ", session)
        session.pop('hilmir', None)
        print("after: ", session)
        return '<h3>Session poped</h3><h3><a href="/">Home</a></h3>'
    else:
        return '<h3>Session was not set</h3><h3><a href="/">Home</a></h3>'

# Checks for session
@app.route('/check')
def checksession():
    if 'hilmir' in session:
        print(session['hilmir']) # Debug, prentum gildi session í cmd
        return '<h3>ON</h3><h3><a href="/">Home</a></h3>'
    else:
        return '<h3>OFF</h3><h3><a href="/">Home</a></h3>'


if __name__ == "__main__":
	app.run(debug=True)
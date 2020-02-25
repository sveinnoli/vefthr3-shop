# Verðum að importa session
from flask import Flask, session
app = Flask(__name__)

# Þessi verður að vera inni til að session virki, best að fá random gildi...
app.config['SECRET_KEY'] = 'Leyno'

# Rót, hlekkir á mismunandi slóðir með mismunandi virkni session
@app.route('/')
def index():
	return '<h3><a href="/on">Set session</a></h3><h3><a href="/off">Delete session</a></h3><h3><a href="/check">Check session</a></h3>'

# Setjum session í gang, 'hilmir' og 'GALVEZ' eru bæði valkvæð gildi sem þú ákveður sjálf / ur
@app.route('/on')
def sessionon():
    session['hilmir'] = 'GALVEZ'
    return '<h3>Session ON</h3><h3><a href="/">Home</a></h3>'

# Eyðum session
@app.route('/off')
def sessionoff():
    if 'hilmir' in session:
        session.pop('hilmir', None)
        return '<h3>Session poped</h3><h3><a href="/">Home</a></h3>'
    else:
        return '<h3>Session was not set</h3><h3><a href="/">Home</a></h3>'

# Athugum hvort session 'hilmir' sé í gangi
@app.route('/check')
def checksession():
    if 'hilmir' in session:
        print(session['hilmir']) # Debug, prentum gildi session í cmd
        return '<h3>ON</h3><h3><a href="/">Home</a></h3>'
    else:
        return '<h3>OFF</h3><h3><a href="/">Home</a></h3>'


if __name__ == "__main__":
	app.run(debug=True)
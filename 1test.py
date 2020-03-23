import os

test_dict = {"wares":[{"product": "shoes", "price": "3500", "image": "~/{{usr}}/bin/img/s.jpg", "id": os.urandom(10).hex()},
            {"product": "jacket", "price": "5500", "image": "image", "id": os.urandom(10).hex()}]}

for item in test_dict["wares"]:
    for key, value in item.items():
        print(key, value)




#@app.route('/on')
#def sessionon():
#    if "testing" in session:
#        text="Session already ON"
#    else:
#        session['testing'] = 'working'
#        text = "Session is now SET"
#    return render_template("shop.html", text=text, session=session)
#
## Deletes session
#@app.route('/off')
#def sessionoff():
#    if "wares" in session:
#        session.clear()
#        text="Session cleared"
#    else:
#        text="Session was not set"
#    return render_template("shop.html", text=text)
#
## Checks for session
#@app.route('/check')
#def checksession():
#    if 'wares' in session:
#        text = session
#    else:
#        text="OFF"
#    return render_template("shop.html", text=text)
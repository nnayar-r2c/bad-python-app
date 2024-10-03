from flask import Flask

# Creating App

app = Flask(__name__)

@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
    resp = flask.make_response(render_template("index.html", input="View function called"))
    resp.set_cookie('userID', user,  secure=False)
    return resp

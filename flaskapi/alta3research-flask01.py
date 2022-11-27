from flask import Flask
from flask import redirect
from flask import jsonify
from flask import url_for
from flask import request
import requests
from flask import render_template

app = Flask(__name__)

url="https://www.boredapi.com/api/activity"
@app.route('/api')
def api():
    req = requests.get(url)
    reqres = req.json()
    return reqres
@app.route('/user/<name>')
def user(name):
    return render_template("user.html", name=name)
@app.route('/')
def start():
    return render_template("index.html") # look for templates/postmaker.html
# This is where postmaker.html POSTs data to
# A user could also browser (GET) to this location
@app.route("/login", methods = ["POST", "GET"])
def login():
    # POST would likely come from a user interacting with postmaker.html
    if request.method == "POST":
        if request.form.get("nm"): # if nm was assigned via the POST
            user = request.form.get("nm") # grab the value of nm from the POST
        else: # if a user sent a post without nm then assign value defaultuser
            user = "defaultuser"
    # GET would likely come from a user interacting with a browser
    elif request.method == "GET":
        if request.args.get("nm"): # if nm was assigned as a parameter=value
            user = request.args.get("nm") # pull nm from localhost:5060/login?nm=larry
        else: # if nm was not passed...
            user = "defaultuser" # ...then user is just defaultuser
    return redirect(url_for("user", name = user)) # pass back to /success with val for name



if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application
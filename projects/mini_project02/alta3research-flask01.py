from flask import Flask
from flask import redirect
from flask import jsonify
from flask import url_for
from flask import request
import requests
from flask import render_template

app = Flask(__name__)

url="https://www.boredapi.com/api/activity?participants=4"
url2= "https://www.boredapi.com/api/activity?participants=1"
@app.route('/api', methods = ["POST", "GET"])
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

    

@app.route("/activity", methods = ["POST", "GET"])
def activity():
    selected = request.form["participants"]
    req2 = requests.get(url2)
    if request.method =="POST":
        if request.form.get("participants"):
            response = req2.json()["activity"]
    return render_template("activity.html", selected=selected, response=response)    
    

@app.route("/groupactivity", methods = ["POST", "GET"])
def groupactivity():
    selected = request.form["participants2"]
    req = requests.get(url)
    reqres = req.json()
    if request.method =="POST":
        if request.form.get("participants2"):
            response = reqres["activity"]
    return render_template("activity.html", selected=selected, response=response)   
   



if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application
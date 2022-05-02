from unittest import result
from flask import Flask, render_template,request
import requests
app = Flask(__name__)
secretkey = "fbf2c29ad43f404ca0e110825220205"
TEMPLATES_AUTO_RELOAD = True

@app.route("/")
def main():
    return render_template("Home.html")

def kelvintocelcius(degree):
    C = degree - 273.15
    return int(C)

@app.route("/",methods=['GET','POST'])
def templatedisplay():    
    if request.method == "POST":
        city = request.form['city']
    else:
        city = "Bengaluru"
    result = requests.get(f"https://api.weatherapi.com/v1/current.json?key={secretkey}&q={city}&aqi=yes").json()

    return render_template("Home.html",result=result)

if __name__=="__main__":
    app.run(debug=True)
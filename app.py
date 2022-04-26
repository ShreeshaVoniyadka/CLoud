import os
from flask import Flask, abort, render_template,request
import requests
app = Flask(__name__)
secretkey = "5657ec52b9ce3c0254b375c7ac428f8b"
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
    try:
        location = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={secretkey}").json()
    except:
        return abort("Enter valid city")
    loca = {}
    for d in location:
       loca.update(d) 
    lat = loca['lat']
    lon = loca['lon']
    try:
        result = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={secretkey}").json()
    except:
        return abort("Enter valid city")
    incelcius = kelvintocelcius(result['main']['temp'])
    result = {
        "temp": str(incelcius) + 'Degree',
        "pressure": str(result['main']['pressure']),
        "humidity": str(result['main']['humidity']),
    }

    return render_template("Home.html",result=result)

if __name__=="__main__":
    app.run(debug=True)
# importing library
from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# load the model
# load the model
model = joblib.load("model/diabetic_80.pkl")

result = model.predict([[2,128,90,45,238,39.9,0.804,28]])[0]

print(result)

@app.route("/")
def home():
    return render_template('home1.html')

@app.route("/data", methods=["post"])
def data():
    preg = int(request.form.get("preg"))
    plas = int(request.form.get("plas"))
    pres = int(request.form.get("pres"))
    skin = int(request.form.get("skin"))
    test = int(request.form.get("test"))
    mass = int(request.form.get("mass"))
    pedi = int(request.form.get("pedi"))
    age = int(request.form.get ("age"))

    result = model.predict([[preg, plas, pres, skin, test, mass, pedi, age]])

    if result[0] == 1:
        data = "Person is diabetic"
    
    else:
        data = "Person is not diabetic"
    
    print(data)

    return "data received"


app.run()    # should be always at the end

# For csv files

@app.route("/csv_data", methods=["post"])
def data1():
    # load the csv
    result = model.predict([[preg, plas, pres, skin, test, mass, pedi, age]])

    if result[0] == 1:
        data1 = "Person is diabetic"
    
    else:
        data1 = "Person is not diabetic"
    
    print(data1)

    return "data received"
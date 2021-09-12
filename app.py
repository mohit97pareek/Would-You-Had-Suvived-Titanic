from flask import Flask,render_template,request
from model import machineModel

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/test")
def test():
    return render_template("second page.html")




@app.route("/first",methods = ['GET','POST'])
def First():
    if(request.method == 'POST'):

        surfix = request.form.get('surfix')
        name = request.form.get('name')
        last_name = request.form.get('last_name')
        gender = request.form.get('gender')
        age = request.form.get('age')
        pclass = request.form.get('pclass')

        weight = request.form.get('weight')
        height = request.form.get('height')
        address = request.form.get('address')

        city = request.form.get('city')
        state = request.form.get('state')
        pincode = request.form.get('pincode')
        SibSp = request.form.get('SibSp')
        Parch = request.form.get('Parch')

        fare = request.form.get('fare')
        cabin = request.form.get('cabin')
        Embarked = request.form.get('Embarked')

        machineModelObj = machineModel(pclass, age, SibSp, Parch, fare)
        result = machineModelObj.model()
        if(result == 1):
            output = "Congrulations, you will survive the Crash";
        else:
            output = "Sorry Mate, You should avoid sea travel";



        return render_template("second page.html",name = output)

app.run(debug=True)

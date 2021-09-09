import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import numpy as np

from RandomForestModel import *


def variabletodataframe(Pclass, Age, SibSp, Parch, Fare):
    predictInput = pd.DataFrame([[Pclass, Age, SibSp, Parch, Fare]],
                                columns=['Pclass', 'Age', 'SibSp', 'Parch', 'Fare'])
    return predictInput


def dataValidation(inputdata):
    bins = [0, 5, 17, 25, 50, 80]
    labels = ['Infant', 'Kid', 'Young', 'Adult', 'Old']
    inputdata['Age'] = inputdata['Age'].astype(np.float64)
    inputdata['Age'] = pd.cut(inputdata['Age'], bins=bins, labels=labels)
    print(inputdata)
    return inputdata


class machineModel():

    def __init__(self, pClass, age, sibSp, parCh, fare):
        self.pClass = pClass
        self.age = age
        self.sibSp = sibSp
        self.parCh = parCh
        self.fare = fare

    def model(self):
        test = variabletodataframe(self.pClass, self.age, self.sibSp, self.parCh, self.fare)
        inputdata = dataValidation(test)
        randomForestObj = RandomForests()
        model = randomForestObj.RandomForestfunction()
        return model.predict(test)

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

class RandomForests:

    def RandomForestfunction(self):
        train_data=pd.read_csv('train.csv')
        train_output = train_data.pop('Survived')

        numeric_variables = list(train_data.dtypes[train_data.dtypes != "object"].index)
        numeric_variables.pop(0);
        train_data["Age"].fillna(train_data.Age.mean(), inplace=True)

        model = RandomForestClassifier(n_estimators=100)
        model.fit(train_data[numeric_variables], train_output)

        return model

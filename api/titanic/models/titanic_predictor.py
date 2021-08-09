import numpy as np
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


titanic_raw = pd.read_csv("../data/titanic.csv")
df = titanic_raw.copy()

x_features = ['PassengerId', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
              'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
y_feature = 'Survived'

df_prep = df.copy()
encoder = {}
for feature in x_features:
    encoder[feature] = dict(df_prep[[feature, "Survived"]].groupby(feature).mean()["Survived"])
    encoder[feature]["other"] = df_prep["Survived"].astype("int").mean()

encoder
for feature in encoder.keys():
    df_prep[feature] = df_prep[feature].fillna(df_prep[feature].mode()[0])
    df_prep[feature] = df_prep[feature].map(encoder[feature])

x_train, x_test, y_train, y_test = train_test_split(df_prep[x_features], df_prep[y_feature])

model = RandomForestClassifier()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
acc = accuracy_score(y_pred, y_test)

joblib.dump(model, "titanic_predictor_v1.joblib")

class TitanicPredictorV1:
    def __init__(self):
        self.predictor = joblib.load("titanic_predictor_v1.joblib")

    def predict(self, titanic_data: list) -> str:
        flower_data_array = np.array(titanic_data).reshape(1, -1)
        prediction = self.predictor.predict(flower_data_array)
        return prediction[0]

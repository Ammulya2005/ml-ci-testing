import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier

def test_model_training():
    df = pd.read_csv("data/data.csv")

    le = LabelEncoder()
    df["payment_mode"] = le.fit_transform(df["payment_mode"])

    X = df[["amount"]]
    y = df["payment_mode"]

    model = DecisionTreeClassifier()
    model.fit(X, y)

    predictions = model.predict(X)

    assert len(predictions) == len(df)
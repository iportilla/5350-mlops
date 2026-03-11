import joblib
import pandas as pd

clf = joblib.load("trained_model.pkl")
X = pd.DataFrame([{"length": 10, "punct": 1}])
print(type(clf))
print(clf.predict(X))

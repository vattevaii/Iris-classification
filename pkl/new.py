import pandas as pd
import joblib

file = open("iris_pkl.pkl","rb")
model2 = joblib.load(file)
print(model2.predict([[6,2.9,5,1.5],[1.2,2.4,2.5,3]]))
file.close()
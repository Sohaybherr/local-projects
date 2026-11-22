import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline  
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score ,classification_report
from sklearn.preprocessing import StandardScaler



df=pd.read_csv("weatherAUS.csv")
df = df.dropna(thresh=len(df)*0.7, axis=1)     # نحيد الأعمدة اللي فيها بزاف NaN
df = df.fillna(df.median(numeric_only=True))   # نعوض NaN بالقيمة المتوسطة
df = df.dropna()   
le = LabelEncoder()
df['RainToday'] = le.fit_transform(df['RainToday'])
df['RainTomorrow'] = le.fit_transform(df['RainTomorrow'])

x = df[["Humidity3pm","Pressure9am","Temp3pm","WindGustSpeed","RainToday"]].values
y = df["RainTomorrow"].values
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42, stratify=y)
cmr=make_pipeline(
    StandardScaler(),
    LogisticRegression(max_iter=1000)
)
cmr.fit(X_train,y_train)
y_pred=cmr.predict(X_test)
print("accuracy on training set:",cmr.score(X_train,y_train))
print("Accuracy:",accuracy_score(y_test,y_pred))






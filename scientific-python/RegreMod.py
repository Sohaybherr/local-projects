import matplotlib.pyplot as plt
import pandas as pd

import numpy as np
from sklearn.linear_model import ElasticNetCV, LassoCV, LinearRegression, RidgeCV
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PolynomialFeatures


df=pd.read_csv("housing.csv").dropna()
df["rooms_per_household"] = df["total_rooms"] / df["households"]
df["bedrooms_per_room"] = df["total_bedrooms"] / df["total_rooms"]
df["sqrt_population"] = np.sqrt(df["population"])
df["log_median_income"] = np.log(df["median_income"])
df["sqrt_housing_median_age"] = np.sqrt(df["housing_median_age"])
df = pd.get_dummies(df, columns=["ocean_proximity"], drop_first=True)
x = df[["rooms_per_household", "bedrooms_per_room","population","median_income","sqrt_population","log_median_income","sqrt_housing_median_age"]+[col for col in df.columns if col.startswith("ocean_proximity_")]].values
y = df["median_house_value"].values
scaler= StandardScaler()
x=scaler.fit_transform(x)
alphas = np.logspace(-4, 4, 50)
poly_ridge = make_pipeline(
    PolynomialFeatures(degree=3, include_bias=False),
    StandardScaler(),
    ElasticNetCV(l1_ratio=0.3, alphas=np.logspace(-2, 4, 50), cv=5, max_iter=5000)
)


X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)



poly_ridge.fit(X_train, y_train)

y_pred_train = poly_ridge.predict(X_train)
y_pred_test = poly_ridge.predict(X_test)

print("Best alpha:", poly_ridge.named_steps['elasticnetcv'].alpha_)
print("R²train score:", r2_score(y_train, y_pred_train))
print("R² test score:", r2_score(y_test, y_pred_test))# Plot
plt.scatter(X_test[:, 0], y_test, color='lightblue', label="Data")
plt.plot(X_test[:, 0], y_pred_test, color='red', label="Regression line")
plt.xlabel("Rooms per household")
plt.ylabel("Median house value")
plt.title("Linear Regression: Housing dataset")
plt.legend()
plt.show()


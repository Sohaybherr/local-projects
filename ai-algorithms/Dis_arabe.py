import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree

from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score


# Charger le dataset Iris
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

df['target'] = iris.target

print(df.head())
print(df.info())
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
# Créer un modèle de classification
model = DecisionTreeClassifier()
# Entraîner le modèle
model.fit(X_train, y_train)
# Faire des prédictions

plt.figure(figsize=(12,8))

plot_tree(
    model,
    feature_names=iris.feature_names,
    class_names=iris.target_names,
    filled=True
)

plt.show()
y_pred = model.predict(X_test)
print(y_pred)
cm = confusion_matrix(y_test, y_pred)
print(cm)
acc = accuracy_score(y_test, y_pred)
print(acc)
recall = recall_score(
    y_test,
    y_pred,
    average='macro'
)

print(recall)
f1 = f1_score(
    y_test,
    y_pred,
    average='macro'
)

print(f1)
sepal_length = 2.5
petal_length = 0.2
new_flower = [[sepal_length, 3.0, petal_length, 0.1]]

prediction = model.predict(new_flower)

print(prediction)
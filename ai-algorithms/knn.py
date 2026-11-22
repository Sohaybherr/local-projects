import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score


df = pd.read_csv('iris.csv')
x = df.drop('species', axis=1)
y = df['species']
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)
Y_pred = model.predict(X_test)
print("Confusion Matrix:")
confusion_matrix_result = confusion_matrix(y_test, Y_pred)
print(confusion_matrix_result)
accuracy = accuracy_score(y_test, Y_pred)
print("Accuracy:", accuracy)
recall = recall_score(y_test, Y_pred, average='macro')
print("Recall:", recall)
f1 = f1_score(y_test, Y_pred, average='macro')
print("F1 Score:", f1)
new_data = [[5.1, 3.5, 1.4, 0.2]]
y_pred_new = model.predict(new_data)
print("Prediction for new data:", y_pred_new)
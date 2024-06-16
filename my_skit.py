from sklearn.datasets import load_iris
import pandas as pd
data = load_iris()
print(data)

titanic = pd.read_csv('titanic3.csv')
titanic.head(6)

male = titanic[titanic['sex'] == 'male']
male

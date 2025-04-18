import pandas as pd
from sklearn.preprocessing import OrdinalEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier
import pickle

oe = OrdinalEncoder()

df = pd.read_csv("./heart.csv")
print(df)
df['Sex'] = df['Sex'].map({'M': 1, 'F': 0})
df['ExerciseAngina'] = df['ExerciseAngina'].map({'Y': 1, 'N': 0})
df["ChestPainType"] = oe.fit_transform(df["ChestPainType"].values.reshape(-1, 1))
df["ST_Slope"] = oe.fit_transform(df["ST_Slope"].values.reshape(-1, 1))
df["RestingECG"] = oe.fit_transform(df["RestingECG"].values.reshape(-1, 1))
x = df[['Age', 'Sex', 'ChestPainType', 'RestingBP','Cholesterol','FastingBS','RestingECG','MaxHR','ExerciseAngina','Oldpeak','ST_Slope']] 
y = df['HeartDisease']
x_train, x_test, y_train, y_teste = train_test_split(x, y, test_size=0.3)

model = RandomForestClassifier()

model.fit(x_train, y_train)


with open('model_teste.pkl', 'wb') as f:
    pickle.dump(model, f)

# # Faz previsões com os dados de teste
y_pred = model.predict(x_test)

print(classification_report(y_teste, y_pred))

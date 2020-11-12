from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_diabetes
import pickle

X, y = load_diabetes(return_X_y=True)
regressor = LinearRegression()
print(regressor.fit(X,y))


model = pickle.dumps(regressor)
print(type(model)), print(type(regressor))

regressor_from_bytes = pickle.loads(model)
print(regressor_from_bytes)
print(type(regressor_from_bytes))

with open('model/myfile.pkl', 'wb') as output:
    pickle.dump(regressor, output)

with open('model/myfile.pkl', 'rb') as pkl_file:
    regressor_from_file = pickle.load(pkl_file)

print(regressor.predict(X))

print(all(regressor.predict(X) == regressor_from_bytes.predict(X)))

print(all(regressor.predict(X) == regressor_from_file.predict(X)))

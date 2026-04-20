import pandas as pd
import numpy as np

class Perceptron:

    def __init__(self, learning_rate=0.01, epochs=100):
        self.lr = learning_rate
        self.epochs = epochs
        self.weights = None
        self.bias = None

    def fit(self, x, y):
        n_samples, n_features = x.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        for _ in range(self.epochs):
            for idx, x_i in enumerate(x):
                linear_output = np.dot(x_i, self.weights) + self.bias
                y_predicted = 1 if linear_output >= 0 else 0

                update = self.lr * (y[idx] - y_predicted)
                self.weights += update * x_i
                self.bias += update
    
    def predict (self, x):
        linear_output = np.dot(x, self.weights) + self.bias
        y_predicted = np.where(linear_output >= 0, 1, 0)
        return y_predicted


df = pd.read_csv('Iris.csv')

df['Species'] = df['Species'].apply(lambda x: 1 if x == 'Iris-versicolor' else 0)

x = df.drop(['Id', 'Species'], axis=1).values
y = df['Species'].values

np.random.seed(42)
indices = np.arange(x.shape[0])
np.random.shuffle(indices)

train_size = int(0.7*len(x))
train_idx, test_idx = indices[:train_size], indices[train_size:]

x_train, x_test = x[train_idx], x[test_idx]
y_train, y_test = y[train_idx], y[test_idx]

model = Perceptron(learning_rate=0.1, epochs=50)
model.fit(x_train, y_train)

predictions = model.predict(x_test)

accuracy = np.mean(predictions == y_test)
print(f"Model Accuracy : {accuracy*100:.2f}%")

print("\nSample Predictions (1=Setosa, 0=Other):")
print("Actual: ", y_test[:10])
print("Predicted:", predictions[:10])
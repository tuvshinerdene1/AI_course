import numpy as np
import pandas as pd


class ClassicMultiPerceptron:
    def __init__(self, input_size, num_classes, epochs=100) -> None:
        self.epochs = epochs
        self.W = np.zeros((num_classes, input_size))
        self.b = np.zeros(num_classes)

    def fit(self, X, y):
        for epoch in range(self.epochs):
            made_update = False
            for idx, x_i in enumerate(X):
                scores = np.dot(self.W, x_i) + self.b

                y_pred = np.argmax(scores)
                y_true = y[idx]

                if y_pred != y_true:
                    self.W[y_pred] -= x_i
                    self.b[y_pred] -= 1

                    self.W[y_true] += x_i
                    self.b[y_true] += 1

                    made_update = True
            if not made_update:
                print(f"Converged early at epoch {epoch}")
                break

    def predict(self, X):
        scores = np.dot(X, self.W.T) + self.b
        return np.argmax(scores, axis=1)


df = pd.read_csv("Iris.csv")

X = df.drop(["Id", "Species"], axis=1).values

labels, y_names = pd.factorize(df["Species"])
y = labels


np.random.seed(52)
indices = np.arange(X.shape[0])
np.random.shuffle(indices)

train_size = int(0.7 * len(X))
X_train, X_test = X[indices[:train_size]], X[indices[train_size:]]
y_train, y_test = y[indices[:train_size]], y[indices[train_size:]]


model = ClassicMultiPerceptron(input_size=4, num_classes=3, epochs=50)
model.fit(X_train, y_train)


predictions = model.predict(X_test)
accuracy = np.mean(predictions == y_test)

print(f"\nFinal Test Accuracy: {accuracy * 100:.2f}%")
print("\nSample Comparisons:")
for i in range(10):
    if y_names[y_test[i]] == y_names[predictions[i]]:
        print(
            f"Correct prediction Actual: {y_names[y_test[i]]} | Predicted: {y_names[predictions[i]]}"
        )
    else:
        print(
            f"Incorrect prediction Actual: {y_names[y_test[i]]} | Predicted: {y_names[predictions[i]]}"
        )

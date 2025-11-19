import csv
import math
import random
import pickle

class SpamKNN:
    def __init__(self, k=5):
        self.k = k
        self.train_set = []

    def fit(self, X, y):
        """
        Fit the model using training data.
        X: list of features [length, punct]
        y: list of labels (0 or 1)
        """
        self.train_set = []
        for i in range(len(X)):
            row = list(X[i]) + [y[i]]
            self.train_set.append(row)

    def predict(self, X):
        """
        Predict labels for new data.
        X: list of features [length, punct]
        """
        predictions = []
        for row in X:
            output = self._predict_single(row)
            predictions.append(output)
        return predictions

    def _predict_single(self, test_row):
        neighbors = self._get_neighbors(test_row)
        output_values = [row[-1] for row in neighbors]
        prediction = max(set(output_values), key=output_values.count)
        return prediction

    def _get_neighbors(self, test_row):
        distances = []
        for train_row in self.train_set:
            dist = self._euclidean_distance(test_row, train_row)
            distances.append((train_row, dist))
        distances.sort(key=lambda tup: tup[1])
        neighbors = []
        for i in range(self.k):
            neighbors.append(distances[i][0])
        return neighbors

    def _euclidean_distance(self, row1, row2):
        distance = 0.0
        # row1 is test_row (features only), row2 is train_row (features + label)
        # We only compare features, which are at indices 0 and 1
        for i in range(len(row1)): 
            distance += (row1[i] - row2[i])**2
        return math.sqrt(distance)

    def save(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self, f)
    
    @staticmethod
    def load(filename):
        with open(filename, 'rb') as f:
            return pickle.load(f)

def load_dataset(filename):
    dataset = []
    try:
        with open(filename, 'r') as csvfile:
            lines = csv.reader(csvfile)
            next(lines) # Skip header
            for row in lines:
                if len(row) < 3:
                    continue
                # row: label, length, punct
                label = 1 if row[0] == 'spam' else 0
                try:
                    length = float(row[1])
                    punct = float(row[2])
                    dataset.append([length, punct, label])
                except ValueError:
                    continue
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
        return None
    return dataset

def split_dataset(dataset, split_ratio=0.8):
    train_size = int(len(dataset) * split_ratio)
    train_set = []
    test_set = list(dataset)
    while len(train_set) < train_size:
        index = random.randrange(len(test_set))
        train_set.append(test_set.pop(index))
    return train_set, test_set

def accuracy_metric(actual, predicted):
    correct = 0
    for i in range(len(actual)):
        if actual[i] == predicted[i]:
            correct += 1
    return correct / float(len(actual)) * 100.0

def main():
    filename = 'smsspamcollection-1k.csv'
    dataset = load_dataset(filename)
    if dataset is None:
        return

    random.seed(42)
    train_data, test_data = split_dataset(dataset)
    print(f'Split {len(dataset)} rows into train={len(train_data)} and test={len(test_data)}')

    # Prepare data for class
    X_train = [row[:-1] for row in train_data]
    y_train = [row[-1] for row in train_data]
    X_test = [row[:-1] for row in test_data]
    y_test = [row[-1] for row in test_data]

    # Train
    model = SpamKNN(k=5)
    model.fit(X_train, y_train)

    # Predict
    predictions = model.predict(X_test)

    # Evaluate
    accuracy = accuracy_metric(y_test, predictions)
    print(f'Spam Classifier Accuracy: {accuracy:.3f}%')

    # Save model
    model_filename = 'spam_model.pkl'
    model.save(model_filename)
    print(f"Model saved to {model_filename}")

if __name__ == "__main__":
    main()

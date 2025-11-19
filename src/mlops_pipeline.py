import os
import csv
import datetime
import shutil
import sys

# Ensure we can import the class from the current directory
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from spam_classifier import SpamKNN, load_dataset, split_dataset, accuracy_metric

def load_and_combine_data(original_file, new_file):
    print(f"Loading original data from {original_file}...")
    data1 = load_dataset(original_file)
    if data1 is None:
        print("Failed to load original data.")
        return None

    print(f"Loading new data from {new_file}...")
    data2 = load_dataset(new_file)
    if data2 is None:
        print("Failed to load new data.")
        return None
    
    print(f"Original size: {len(data1)}, New data size: {len(data2)}")
    combined_data = data1 + data2
    print(f"Combined dataset size: {len(combined_data)}")
    return combined_data

def train_and_evaluate(dataset):
    # Split data
    train_data, test_data = split_dataset(dataset, split_ratio=0.8)
    
    # Prepare features and labels
    X_train = [row[:-1] for row in train_data]
    y_train = [row[-1] for row in train_data]
    X_test = [row[:-1] for row in test_data]
    y_test = [row[-1] for row in test_data]

    # Train
    print("Training model...")
    model = SpamKNN(k=5)
    model.fit(X_train, y_train)

    # Evaluate
    print("Evaluating model...")
    predictions = model.predict(X_test)
    accuracy = accuracy_metric(y_test, predictions)
    print(f"Model Accuracy: {accuracy:.2f}%")
    
    return model, accuracy

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    original_data_path = os.path.join(script_dir, 'smsspamcollection-1k.csv')
    new_data_path = os.path.join(script_dir, 'synthetic_sms_numeric.csv')
    current_model_path = os.path.join(script_dir, 'spam_model.pkl')
    
    # 1. Data Ingestion
    dataset = load_and_combine_data(original_data_path, new_data_path)
    if dataset is None:
        sys.exit(1)

    # 2. Retraining & Evaluation
    model, accuracy = train_and_evaluate(dataset)

    # 3. Versioning
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    versioned_model_name = f"spam_model_{timestamp}.pkl"
    versioned_model_path = os.path.join(script_dir, versioned_model_name)
    
    print(f"Saving versioned model to {versioned_model_name}...")
    model.save(versioned_model_path)

    # 4. Promotion
    THRESHOLD = 85.0
    if accuracy >= THRESHOLD:
        print(f"Accuracy ({accuracy:.2f}%) meets threshold ({THRESHOLD}%). Promoting model...")
        shutil.copy(versioned_model_path, current_model_path)
        print(f"Model promoted to {current_model_path}")
    else:
        print(f"Accuracy ({accuracy:.2f}%) does NOT meet threshold ({THRESHOLD}%). Model not promoted.")

if __name__ == "__main__":
    main()

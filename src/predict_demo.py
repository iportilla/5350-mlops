import pickle
import sys
import os

# Ensure we can import the class from the current directory
sys.path.append(os.getcwd())

try:
    from spam_classifier import SpamKNN
except ImportError:
    # Fallback if running from a different directory context, though Cwd should handle it
    print("Error: Could not import SpamKNN. Make sure you are in the correct directory.")
    sys.exit(1)

def load_model():
    try:
        with open('spam_model.pkl', 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        print("Error: spam_model.pkl not found. Run spam_classifier.py first.")
        sys.exit(1)

def main():
    model = load_model()
    
    # Sample data points (Length, Punctuation)
    # Based on inspection of smsspamcollection-1k.csv
    examples = [
        (47, 0),    # Short, no punctuation (Likely Ham)
        (111, 9),   # Medium, some punctuation (Likely Ham)
        (155, 6),   # Long, moderate punctuation (Likely Spam)
        (149, 11),  # Long, high punctuation (Likely Spam)
        (20, 1),    # Very short (Likely Ham)
        (158, 8)    # Long, high punctuation (Likely Spam)
    ]

    print(f"{'Length':<10} {'Punct':<10} {'Prediction':<10}")
    print("-" * 30)

    for length, punct in examples:
        # Predict expects a list of lists
        prediction = model.predict([[length, punct]])[0]
        label = "Spam" if prediction == 1 else "Ham"
        print(f"{length:<10} {punct:<10} {label:<10}")

if __name__ == "__main__":
    main()

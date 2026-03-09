"""
Model training script with version support.

Usage:
    python train_model.py           # Train with default (v2/4k) dataset
    python train_model.py v1        # Train v1 with 1k dataset
    python train_model.py v2        # Train v2 with 4k dataset
    python train_model.py all       # Train both versions
"""

import sys
import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split


VERSIONS = {
    "v1": {
        "data_file": "smsspamcollection-1k.csv",
        "model_file": "trained_model_v1.pkl",
        "description": "Model v1 - trained on 1k dataset"
    },
    "v2": {
        "data_file": "smsspamcollection-4k.csv",
        "model_file": "trained_model_v2.pkl",
        "description": "Model v2 - trained on 4k dataset"
    },
    "v3": {
        "data_file": "smsspamcollection-balanced.csv",
        "model_file": "trained_model_v3.pkl",
        "description": "Model v3 - trained on balanced synthetic dataset"
    }
}

DEFAULT_VERSION = "v2"


def train_model(version: str) -> None:
    """Train a model for the specified version."""
    if version not in VERSIONS:
        print(f"Error: Unknown version '{version}'. Available: {list(VERSIONS.keys())}")
        sys.exit(1)
    
    config = VERSIONS[version]
    print(f"\n{'='*50}")
    print(f"Training {config['description']}")
    print(f"Dataset: {config['data_file']}")
    print(f"{'='*50}\n")
    
    data = pd.read_csv(config["data_file"])
    
    X = data[["length", "punct"]]
    y = data["label"]
    
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.25,
        random_state=42,
        stratify=y,
    )
    
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    
    predictions = model.predict(X_test)
    
    print(f"Accuracy: {accuracy_score(y_test, predictions):.2f}\n")
    print(classification_report(y_test, predictions))
    
    joblib.dump(model, config["model_file"])
    print(f"Model saved to {config['model_file']}")
    
    # Also save as default model name for backward compatibility
    joblib.dump(model, "trained_model.pkl")
    print(f"Also saved as trained_model.pkl (default)")


def main() -> None:
    if len(sys.argv) < 2:
        # Default behavior: train default version
        train_model(DEFAULT_VERSION)
    elif sys.argv[1] == "all":
        # Train all versions
        for version in VERSIONS:
            train_model(version)
    else:
        # Train specific version
        train_model(sys.argv[1])


if __name__ == "__main__":
    main()

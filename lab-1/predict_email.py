import sys
import joblib
import pandas as pd
from utils import extract_features


MODEL_FILE = "trained_model.pkl"


def main() -> None:
    if len(sys.argv) < 2:
        print('Usage: python predict_email.py "Your email text here"')
        sys.exit(1)

    email_text = sys.argv[1]
    features = extract_features(email_text)

    model = joblib.load(MODEL_FILE)
    feature_frame = pd.DataFrame([features])
    prediction = model.predict(feature_frame)[0]

    print(f"Email text: {email_text}")
    print(f"Extracted features: {features}")
    print(f"Prediction: {prediction}")


if __name__ == "__main__":
    main()

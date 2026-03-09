import os
import string
import joblib
import pandas as pd
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load model at startup
MODEL_PATH = os.environ.get("MODEL_PATH", "trained_model.pkl")
model = None


def load_model():
    global model
    if model is None:
        model = joblib.load(MODEL_PATH)
    return model


def extract_features(text: str) -> dict:
    """Extract features from text."""
    length = len(text)
    punct = sum(1 for ch in text if ch in string.punctuation)
    return {"length": length, "punct": punct}


@app.route("/classify", methods=["POST"])
def classify():
    """
    Classify a message as spam or ham.
    
    Request body: {"message": "Your text here"}
    Response: {"message": "...", "features": {...}, "prediction": "spam"|"ham"}
    """
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "Invalid JSON in request body"}), 400
    
    message = data.get("message", "")
    if not message:
        return jsonify({"error": "Missing 'message' field in request body"}), 400

    features = extract_features(message)
    clf = load_model()
    
    feature_frame = pd.DataFrame([features])
    prediction = clf.predict(feature_frame)[0]

    return jsonify({
        "message": message,
        "features": features,
        "prediction": prediction
    })


@app.route("/health", methods=["GET"])
def health():
    """Health check endpoint."""
    return jsonify({"status": "healthy"})


@app.route("/", methods=["GET"])
def index():
    """Root endpoint with API info."""
    return jsonify({
        "service": "Spam Classifier API",
        "version": "1.0.0",
        "endpoints": {
            "POST /classify": "Classify a message as spam or ham",
            "GET /health": "Health check endpoint"
        }
    })


if __name__ == "__main__":
    # Pre-load model
    load_model()
    
    port = int(os.environ.get("PORT", 8080))
    debug = os.environ.get("DEBUG", "false").lower() == "true"
    
    app.run(host="0.0.0.0", port=port, debug=debug)

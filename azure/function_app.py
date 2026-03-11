import azure.functions as func
import json
import joblib
import os
import string

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

# Load model at cold start
MODEL_PATH = os.path.join(os.path.dirname(__file__), "trained_model.pkl")
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


@app.route(route="classify", methods=["POST"])
def classify_spam(req: func.HttpRequest) -> func.HttpResponse:
    """
    Classify a message as spam or ham.
    
    Request body: {"message": "Your text here"}
    Response: {"message": "...", "features": {...}, "prediction": "spam"|"ham"}
    """
    try:
        req_body = req.get_json()
    except ValueError:
        return func.HttpResponse(
            json.dumps({"error": "Invalid JSON in request body"}),
            status_code=400,
            mimetype="application/json"
        )

    message = req_body.get("message", "")
    if not message:
        return func.HttpResponse(
            json.dumps({"error": "Missing 'message' field in request body"}),
            status_code=400,
            mimetype="application/json"
        )

    # Extract features and predict
    features = extract_features(message)
    clf = load_model()
    
    import pandas as pd
    feature_frame = pd.DataFrame([features])
    prediction = clf.predict(feature_frame)[0]

    result = {
        "message": message,
        "features": features,
        "prediction": prediction
    }

    return func.HttpResponse(
        json.dumps(result),
        status_code=200,
        mimetype="application/json"
    )


@app.route(route="health", methods=["GET"])
def health_check(req: func.HttpRequest) -> func.HttpResponse:
    """Health check endpoint."""
    return func.HttpResponse(
        json.dumps({"status": "healthy"}),
        status_code=200,
        mimetype="application/json"
    )

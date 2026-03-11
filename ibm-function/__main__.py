import os
import string

def response(status_code, body):
    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": body
    }

try:
    import joblib
    import pandas as pd
    IMPORT_ERROR = None
except Exception as e:
    joblib = None
    pd = None
    IMPORT_ERROR = str(e)

MODEL_PATH = os.path.join(os.path.dirname(__file__), "trained_model.pkl")
model = None

def load_model():
    global model
    if model is None:
        if IMPORT_ERROR:
            raise RuntimeError(f"Import error: {IMPORT_ERROR}")
        if not os.path.exists(MODEL_PATH):
            raise FileNotFoundError(f"Model file not found: {MODEL_PATH}")
        model = joblib.load(MODEL_PATH)
    return model

def extract_features(text: str) -> dict:
    return {
        "length": len(text),
        "punct": sum(1 for ch in text if ch in string.punctuation),
    }

def main(args):
    try:
        if args.get("health"):
            return response(200, {
                "status": "healthy",
                "model_path": MODEL_PATH,
                "model_exists": os.path.exists(MODEL_PATH),
                "import_error": IMPORT_ERROR,
                "cwd": os.getcwd(),
                "files": sorted(os.listdir(os.path.dirname(__file__)))
            })

        message = args.get("message", "")
        if not isinstance(message, str) or not message.strip():
            return response(400, {"error": "Missing or empty 'message' field in request"})

        features = extract_features(message.strip())
        clf = load_model()
        df = pd.DataFrame([features])
        prediction = clf.predict(df)[0]

        return response(200, {
            "message": message.strip(),
            "features": features,
            "prediction": str(prediction),
            "model_type": str(type(clf)),
        })

    except Exception as e:
        return response(500, {
            "error": str(e),
            "model_path": MODEL_PATH,
            "model_exists": os.path.exists(MODEL_PATH),
            "import_error": IMPORT_ERROR
        })
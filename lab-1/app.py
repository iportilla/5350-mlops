import streamlit as st
import joblib
import pandas as pd
from utils import extract_features


MODEL_FILE = "trained_model.pkl"


st.title("📧 Spam Email Classifier")
st.write("Enter an email or SMS message to check if it's spam or not.")

email_text = st.text_area("Message text:", height=150, placeholder="Type or paste your message here...")

if st.button("Classify", type="primary"):
    if not email_text.strip():
        st.warning("Please enter some text to classify.")
    else:
        try:
            model = joblib.load(MODEL_FILE)
            features = extract_features(email_text)
            feature_frame = pd.DataFrame([features])
            prediction = model.predict(feature_frame)[0]

            st.subheader("Results")
            col1, col2 = st.columns(2)
            
            with col1:
                st.metric("Length", features["length"])
            with col2:
                st.metric("Punctuation Count", features["punct"])

            if prediction == "spam":
                st.error("🚫 This message is **SPAM**")
            else:
                st.success("✅ This message is **HAM** (not spam)")

        except FileNotFoundError:
            st.error(f"Model file '{MODEL_FILE}' not found. Please run train_model.py first.")

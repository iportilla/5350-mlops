import streamlit as st
import pickle
import os
# Import the class definition so pickle can load the object
try:
    from spam_classifier import SpamKNN
except ImportError:
    st.error("Could not import SpamKNN class. Make sure spam_classifier.py is in the same directory.")

def load_model():
    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(script_dir, 'spam_model.pkl')
    
    if not os.path.exists(model_path):
        return None
    with open(model_path, 'rb') as f:
        return pickle.load(f)

def main():
    st.title("SMS Spam Classifier")
    st.write("Enter the message details below to check if it's Spam or Ham.")

    # Sidebar for inputs
    st.sidebar.header("Message Features")
    
    # Reasonable ranges based on the dataset (viewed earlier)
    # Length seems to go up to ~900, punct up to ~30
    length = st.sidebar.slider("Message Length", min_value=0, max_value=500, value=50)
    punct = st.sidebar.slider("Punctuation Count", min_value=0, max_value=50, value=2)

    st.write(f"**Analyzing message with:**")
    st.write(f"- Length: {length}")
    st.write(f"- Punctuation: {punct}")

    if st.button("Classify"):
        model = load_model()
        if model is None:
            st.error("Model file 'spam_model.pkl' not found. Please run 'spam_classifier.py' first.")
        else:
            # Predict expects a list of lists (features)
            prediction = model.predict([[length, punct]])
            result = "Spam" if prediction[0] == 1 else "Ham"
            
            if result == "Spam":
                st.error(f"Prediction: {result}")
            else:
                st.success(f"Prediction: {result}")

if __name__ == "__main__":
    main()

# SMS Spam Classifier

A simple machine learning application to classify SMS messages as 'Ham' (legitimate) or 'Spam' based on message length and punctuation count.

## Features

- **K-Nearest Neighbors (KNN) Classifier**: Custom implementation using standard Python libraries.
- **Streamlit UI**: Interactive web interface for easy testing.
- **Dockerized**: Ready for deployment with Docker.
- **Model Persistence**: Saves and loads the trained model using `pickle`.

## Project Structure

```
.
├── Dockerfile              # Docker configuration
├── requirements.txt        # Python dependencies
└── src/
    ├── app.py              # Streamlit application
    ├── spam_classifier.py  # Classifier logic and training script
    ├── spam_model.pkl      # Trained model (generated after training)
    ├── predict_demo.py     # CLI demo script
    └── smsspamcollection-1k.csv # Dataset
```

## Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/iportilla/5350-mlops.git
    cd spam
    ```

2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### 1. Train the Model
Before running the app, you need to train the model. This will generate `src/spam_model.pkl`.

```bash
python3 src/spam_classifier.py
```

### 2. Run the Streamlit App
Launch the web interface:

```bash
streamlit run src/app.py
```
Access the app at `http://localhost:8501`.

### 3. Run CLI Demo
To see predictions in the terminal:

```bash
python3 src/predict_demo.py
```

## Docker Deployment

Build and run the application using Docker.

1.  **Build the image**:
    ```bash
    docker build -t spam-classifier .
    ```

2.  **Run the container**:
    ```bash
    docker run -p 8501:8501 spam-classifier
    ```

3.  **Access the App**:
    Open your browser and navigate to `http://localhost:8501`.

## Model Details

The classifier uses a **K-Nearest Neighbors (KNN)** algorithm with `k=5`. It uses two features:
- **Length**: The number of characters in the message.
- **Punctuation**: The count of punctuation characters in the message.

The dataset used is a subset of the SMS Spam Collection.

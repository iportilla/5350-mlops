# MLOps Teaching Repository: Spam Classifier

Welcome to this educational repository designed to teach **MLOps (Machine Learning Operations)** concepts through a practical example.

This project evolves from a simple Python script into a production-ready, containerized application with an automated retraining pipeline.

## Documentation Guide

Explore the following documents to understand different aspects of the project:

### 1. [Project Details](PROJECT_DETAILS.md)
*   **What it is**: The technical documentation for the Spam Classifier application.
*   **Contents**: Installation, Usage, Docker deployment, and Model details.
*   **Target Audience**: Developers wanting to run the app.

```
/Users/fiery/Downloads/spam/
├── Dockerfile
├── requirements.txt
├── README.md               # Cover Page
├── PROJECT_DETAILS.md      # Technical Documentation
├── MLOPS_README.md         # MLOps Best Practices
├── TEACHING_PROMPTS.md     # Session Prompts
└── src/
    ├── app.py
    ├── spam_classifier.py
    ├── spam_model.pkl
    ├── mlops_pipeline.py
    ├── smsspamcollection-1k.csv
    ├── synthetic_sms_numeric.csv
    └── predict_demo.py
```

### 2. [MLOps Best Practices](MLOPS_README.md)
*   **What it is**: A deep dive into the operational side of Machine Learning.
*   **Contents**: Pipeline architecture, Quality Gates, Deployment Strategies (Canary, Shadow), and advanced concepts (Drift Detection, Feature Stores).
*   **Target Audience**: MLOps Engineers and Students learning about production ML.

### 3. [Teaching Prompts](TEACHING_PROMPTS.md)
*   **What it is**: A "behind-the-scenes" look at how this project was built using AI.
*   **Contents**: The exact sequence of prompts used to generate the code, demonstrating the role of AI Agents in modern software engineering.
*   **Target Audience**: Instructors and Students interested in AI-assisted development.

---

## Quick Start

To run the application immediately using Docker:

```bash
docker build -t spam-classifier .
docker run -p 8501:8501 spam-classifier
```

Then open [http://localhost:8501](http://localhost:8501).

# MLOps Teaching Repository: Spam Classifier

Welcome to this educational repository designed to teach **MLOps (Machine Learning Operations)** concepts through a practical example.

This project evolves from a simple Python script into a production-ready, containerized application with an automated retraining pipeline.

## Start here: the labs

| Lab | What you do | Start with |
|---|---|---|
| [lab-1](lab-1/README.md) | Train spam models v1, v2 and v3 and discover why accuracy can mislead | [lab-1/README.md](lab-1/README.md) |
| [lab-mlops-101](lab-mlops-101/README.md) | The MLOps loop: model cards, a retraining pipeline with a quality gate, rollback, safe rollouts and drift. Command line or Jupyter notebooks | [lab-mlops-101/README.md](lab-mlops-101/README.md) |

The lab-mlops-101 notebooks are the quickest way in: `train_model.ipynb`, then `mlops_basics.ipynb` (new to data science) or `mlops_pipeline.ipynb` (full version). Each has a Starter section with TODOs and a Solution section.

## Repository layout

| Folder | What is in it |
|---|---|
| [src/](src/) | The original spam classifier app: KNN model, Streamlit UI and `mlops_pipeline.py` |
| [lab-1/](lab-1/README.md) | Lab 1: training and the accuracy trap |
| [lab-mlops-101/](lab-mlops-101/README.md) | MLOps 101 lab: scripts, notebooks, instructor guide and solutions |
| [docker/](docker/README.md) | Running the model in Docker, on a cloud VM and on Kubernetes |
| [ibm-function/](ibm-function/README.md) | The model as a serverless API on IBM Code Engine |
| [azure/](azure/README.md) | The model as a serverless API on Azure Functions |
| [summary/](summary/README.md) | How the class steps map to the MLOps maturity model |
| [docs/](docs/README.md) | Slides (PDF) |

## Documentation Guide

Explore the following documents to understand different aspects of the project:

### 1. [Project Details](PROJECT_DETAILS.md)
*   **What it is**: The technical documentation for the Spam Classifier application.
*   **Contents**: Installation, Usage, Docker deployment, and Model details.
*   **Target Audience**: Developers wanting to run the app.

```
5350-mlops/
├── Dockerfile              # builds the src/ Streamlit app
├── requirements.txt
├── README.md               # this page
├── PROJECT_DETAILS.md      # technical documentation for the src/ app
├── MLOPS_README.md         # MLOps best practices
├── TEACHING_PROMPTS.md     # the prompts used to build src/
└── src/
    ├── app.py
    ├── spam_classifier.py
    ├── spam_model.pkl
    ├── mlops_pipeline.py
    ├── predict_demo.py
    └── *.csv               # datasets
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

To run the `src/` application immediately using Docker:

```bash
docker build -t spam-classifier .
docker run -p 8501:8501 spam-classifier
```

Then open [http://localhost:8501](http://localhost:8501).

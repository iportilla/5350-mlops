# MLOps Teaching Guide: Session Prompts

This document contains the sequence of prompts used to build the Spam Classifier project, evolving from a simple script to a Dockerized MLOps pipeline. Use this to demonstrate the iterative nature of software engineering and MLOps.

## Phase 1: The MVP (Minimum Viable Product)

**Prompt 1:**
> "write a python script to create a classifier for ham/spam predictions with the smsspam csv file in this folder"

*   **Goal**: Basic implementation.
*   **Outcome**: A simple Python script using K-Nearest Neighbors (due to library constraints) to classify messages based on length and punctuation.

**Prompt 2:**
> "next save the model for testing via streamlit UI"

*   **Goal**: Model Persistence & Serving.
*   **Outcome**: Refactoring code into a class, saving the model with `pickle`, and creating a `Streamlit` app for user interaction.

**Prompt 3:**
> "run it and show me predictions"

*   **Goal**: Verification.
*   **Outcome**: A demo script (`predict_demo.py`) to validate the model works as expected without needing the full UI environment.

## Phase 2: Containerization

**Prompt 4:**
> "perfect,next let's create a deployment with docker, create Dockerfile and folder structure"

*   **Goal**: Reproducibility & Deployment.
*   **Outcome**: Reorganizing into a `src` directory, creating a `Dockerfile` and `requirements.txt`.

**Prompt 5:**
> "test again, docker daemon running"

*   **Goal**: Build Verification.
*   **Outcome**: Building and running the Docker container.

**Prompt 6:**
> "error - Model file 'spam_model.pkl' not found. Please run 'spam_classifier.py' first."

*   **Goal**: Debugging.
*   **Outcome**: Fixing file path issues. The app was looking for the model in the current directory, but inside Docker, paths must be relative to the script location.

**Prompt 7:**
> "perfect, write a readme file for a github deployment"

*   **Goal**: Documentation.
*   **Outcome**: A comprehensive `README.md` for the repository.

## Phase 3: MLOps & Automation

**Prompt 8:**
> "demonstrate MLOps techniques, I just received a new synthetic sms file, placed it in src folder"

*   **Goal**: Automation & Continuous Training.
*   **Outcome**: An `mlops_pipeline.py` script that ingests new data, retrains the model, and versions it.

**Prompt 9:**
> "what would you recommend to deploy a new model to production?"

*   **Goal**: Strategy.
*   **Outcome**: Discussion of deployment strategies (Shadow, Canary, Blue/Green) and the importance of Quality Gates (the pipeline rejected the new model because accuracy dropped).

**Prompt 10:**
> "Create a new readme for all these mlops best practices"

*   **Goal**: Knowledge Sharing.
*   **Outcome**: `MLOPS_README.md` detailing the pipeline architecture and deployment strategies.

**Prompt 11:**
> "anything else I should know about mlops?"

*   **Goal**: Advanced Concepts.
*   **Outcome**: Expanding documentation to include Monitoring (Drift), Data Versioning, Feature Stores, and Explainability.

## Teaching Point: AI Agents & Tool Use in MLOps

This session itself is a lesson in modern MLOps workflows using AI Agents.

1.  **Rapid Scaffolding**: The agent quickly generated boilerplate (Dockerfiles, pipeline scripts), allowing the engineer to focus on high-level strategy (e.g., "add a quality gate").
2.  **Iterative Verification**: The agent didn't just write code; it *ran* the code (using tools) to verify builds and catch errors (like the Docker path issue) before the human intervened. This acts as a "Pre-CI" check.
3.  **Context Awareness**: The agent understood the project structure (`src` folder move) and adapted subsequent commands (Docker paths) accordingly.
4.  **Human-in-the-Loop**: The human provided the *intent* ("deploy", "fix error", "teach me"), while the agent handled the *implementation*. This mirrors the shift in MLOps from "writing every line of code" to "orchestrating systems."

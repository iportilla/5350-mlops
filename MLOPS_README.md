# MLOps Best Practices & Pipeline Documentation

This document outlines the MLOps architecture implemented in this project and recommends strategies for production deployment.

## 1. The Automated Pipeline (`src/mlops_pipeline.py`)

We have implemented a robust pipeline to handle model retraining and lifecycle management.

### Workflow Steps
1.  **Data Ingestion**:
    *   Combines the original dataset (`smsspamcollection-1k.csv`) with new incoming data (e.g., `synthetic_sms_numeric.csv`).
    *   *Best Practice*: In production, this would pull from a Feature Store or Data Lake.

2.  **Retraining**:
    *   Trains a new K-Nearest Neighbors model on the combined dataset.
    *   *Best Practice*: Use hyperparameter tuning (e.g., Grid Search) during this phase to optimize performance.

3.  **Evaluation & Quality Gate**:
    *   Calculates accuracy on a held-out test set.
    *   **The Gate**: The model is ONLY promoted if accuracy exceeds a strict threshold (currently **85%**).
    *   *Benefit*: Prevents performance regression caused by noisy data or concept drift.

4.  **Versioning**:
    *   Every training run saves a model artifact with a timestamp (e.g., `spam_model_20251119_063257.pkl`).
    *   *Benefit*: Allows for easy rollback to previous versions if issues arise.

5.  **Promotion**:
    *   If the Quality Gate is passed, the new model overwrites the production model (`spam_model.pkl`).

## 2. Deployment Strategies

When deploying a new model version to production, avoid a "Big Bang" replacement. Use one of these safer strategies:

### Shadow Deployment (Recommended)
*   **How**: Deploy the new model alongside the current one. Route traffic to both, but only return the **current** model's response to the user.
*   **Why**: Allows you to verify the new model's predictions against real-world traffic without risking user experience.

### Canary Deployment
*   **How**: Route a small percentage (e.g., 5-10%) of traffic to the new model.
*   **Why**: Limits the blast radius of any potential issues. If metrics remain stable, gradually increase traffic to 100%.

### Blue/Green Deployment
*   **How**: Maintain two identical environments. "Blue" is live. Deploy the new version to "Green". Switch the router to point to Green.
*   **Why**: Instant rollback capability by switching the router back to Blue.

## 3. CI/CD Integration

To fully operationalize this workflow:

*   **Triggering**: Run the pipeline automatically when:
    *   New data arrives in the S3 bucket/data warehouse.
    *   Code changes are merged to the `main` branch.
*   **Containerization**: If a model is promoted, the CI system should:
    1.  Rebuild the Docker image.
    2.  Run integration tests.
    3.  Push the new image to the Container Registry.
    4.  Trigger a deployment (Shadow/Canary) to the Kubernetes cluster.

## 4. Advanced MLOps Concepts (Future Roadmap)

Beyond the basics, a mature MLOps platform includes:

### Monitoring & Observability
*   **Drift Detection**: Continuously monitor input data for "Data Drift" (e.g., spam messages becoming shorter) and model output for "Concept Drift" (e.g., accuracy dropping over time).
*   **Alerting**: Set up alerts (e.g., PagerDuty, Slack) when drift exceeds a threshold to trigger automatic retraining.

### Data Versioning
*   **Tools**: Use tools like **DVC (Data Version Control)** or **Delta Lake**.
*   **Why**: Code versioning (Git) is not enough. You need to know exactly which *dataset version* produced a specific *model version* to ensure reproducibility.

### Feature Store
*   **Concept**: A centralized repository for storing, documenting, and sharing features.
*   **Why**: Ensures consistency between training (batch) and serving (real-time). If you calculate "average message length" one way in training, the Feature Store ensures the exact same logic is used in the app.

### Model Explainability
*   **Tools**: SHAP, LIME.
*   **Why**: "Black box" models can be risky. Explainability tools help you understand *why* a model classified a message as spam (e.g., "because it contained 15 punctuation marks").

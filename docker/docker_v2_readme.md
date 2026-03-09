# Lab 1 v2 --- MLOps Spam Classification Challenge

## Overview

In this lab you will deploy and evaluate multiple machine learning
models that classify emails as **spam** or **ham** using simple text
features.

You will: - Connect to a shared Linux server - Launch a Streamlit ML
application - Evaluate model performance - Investigate **dataset
imbalance** - Generate a **balanced dataset** - Train a new model and
compare results

This lab demonstrates a core real‑world ML lesson:

> **Accuracy alone can be misleading when datasets are imbalanced.**

------------------------------------------------------------------------

# System Architecture

``` mermaid
flowchart LR
A[Student Laptop] -->|SSH| B[Course Server]
B --> C[GitHub Repo]
C --> D[Lab1 Code]
D --> E[Streamlit ML App]
E --> F[Model Training]
F --> G[Results Dashboard]
```

------------------------------------------------------------------------

# Step 1 --- Connect to the Server

Open a terminal and run:

``` bash
ssh ubuntu@54.214.192.144
```

------------------------------------------------------------------------

# Step 2 --- Create Your Workspace

Replace `[YOUR_NAME]` with your name.

``` bash
mkdir [YOUR_NAME]
cd [YOUR_NAME]
```

Example:

``` bash
mkdir maria
cd maria
```

------------------------------------------------------------------------

# Step 3 --- Clone the Repository

``` bash
git clone https://github.com/iportilla/5350-mlops.git
```

------------------------------------------------------------------------

# Step 4 --- Navigate to the Lab

``` bash
cd 5350-mlops/docker
```

------------------------------------------------------------------------

# Step 5 --- Start the Streamlit App

Each student should use a **different port number**.

``` bash
make run PORT=850X
```

Examples:

``` bash
make run PORT=8501
make run PORT=8502
make run PORT=8503
```

Open the application in your browser:

    http://54.214.192.144:8501

------------------------------------------------------------------------

Test with



```code
curl -X POST http://54.214.192.144:8501/classify \
-H "Content-Type: application/json" \
-d '{"message": "Congratulations! You won a free iPhone. Click here now!"}'
```







# Step 6 --- Evaluate Model v1

Observe the following metrics:

-   Accuracy
-   Precision
-   Recall
-   Confusion Matrix

You may notice something unusual:

The model reports **high accuracy but fails to detect spam messages.**

------------------------------------------------------------------------

# Why Does This Happen?

The dataset is **imbalanced**.

``` mermaid
pie
title Dataset Distribution
"ham" : 88
"spam" : 12
```

A model can achieve **88% accuracy by predicting HAM every time.**

------------------------------------------------------------------------

# Step 7 --- Generate Balanced Data

Create a balanced synthetic dataset:

``` bash
python generate_balanced_data.py
```

This creates:

    smsspamcollection-balanced.csv

Balanced distribution:

-   1000 ham
-   1000 spam

------------------------------------------------------------------------

# Step 8 --- Train Model v3

``` bash
python train_model.py v3
```

The new model should detect spam much more accurately.

------------------------------------------------------------------------

# Expected Results

  Metric            Imbalanced Model   Balanced Model
----------------- ------------------ ----------------
  Accuracy          \~84%              \~99%
  Spam Recall       0%                 \~98%
  False Negatives   Very High          Very Low

------------------------------------------------------------------------

# Improved Decision Boundary

``` mermaid
flowchart LR
Data --> FeatureExtraction
FeatureExtraction --> BalancedTraining
BalancedTraining --> BetterDecisionBoundary
BetterDecisionBoundary --> AccuratePredictions
```

------------------------------------------------------------------------

# Discussion Questions

1.  Why can accuracy be misleading in imbalanced datasets?
2.  What real‑world systems might have similar problems?
3.  What alternatives exist besides synthetic data balancing?
4.  When would you use **class weighting** instead?

------------------------------------------------------------------------

# Bonus Exploration

Try experimenting with:

-   Logistic Regression
-   Decision Trees
-   Random Forest

Compare:

-   Precision
-   Recall
-   F1 Score

------------------------------------------------------------------------

# Key Takeaway

Real ML systems must consider:

-   Data distribution
-   Evaluation metrics
-   Model bias

Understanding **dataset imbalance** is a critical skill in **MLOps and
production AI systems**.

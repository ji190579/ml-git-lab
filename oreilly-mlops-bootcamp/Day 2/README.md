
#  Day 2: Applied MLOps 

Welcome to **Day 2** of the MLOps Bootcamp! Today’s focus is on **Applied MLOps** — deploying, scaling, and managing ML models in production environments using modern infrastructure tools like Kubernetes, HPA, and CI/CD pipelines.

---

##  Repository Structure Overview

### 1. `lesson-2-kubernetes-basics/` – Kubernetes Basics

Deploy a simple ML inference API using **Kubernetes Deployments** and **Services**. Learn the basics of running containerized ML apps in a cluster.

🔗 See [`lesson-2-kubernetes-basics/README.md`](lesson-2-kubernetes-basics/README.md) for setup and usage.

---

### 2. `lesson-5-kubernetes-hpa/` – Horizontal Pod Autoscaling

Set up **HPA (Horizontal Pod Autoscaling)** to automatically scale your service based on CPU usage. Simulate load and watch Kubernetes scale your pods dynamically.

🔗 See [`lesson-5-kubernetes-hpa/README.md`](lesson-5-kubernetes-hpa/README.md) for step-by-step scaling instructions.

---

### 3. `lesson-7-ab-testing/` – A/B Testing 

Deploy two ML models (Logistic Regression and Random Forest) to predict diabetes risk using **FastAPI**, and simulate **A/B testing** .

🔗 See [`lesson-7-ab-testing/README.md`](lesson-7-ab-testing/README.md) for deployment patterns and traffic control.

---

### 4. `lesson-10-mlops-practices/` –  Integrating End-to-End MLOps

Deploy a full MLOps workflow with:

* **MLflow** for model tracking and versioning
* **Flask API** for real-time inference
* **Prometheus & Grafana** for monitoring
* **Kubernetes** for scalable deployment

This project demonstrates how to manage, serve, monitor, and scale ML models in production.

🔗 See [`lesson-10-mlops-practices/README.md`](lesson-10-mlops-practices/README.md)  lesson-10-mlops-practices/README.md for end-to-end MLOps.

---

##  Prerequisites

Before starting, make sure you have the following installed:

* Docker
* Kubectl
* Python 3.11 (required for MLflow compatibility)
* Postman (for testing APIs)
* MLflow

### Environment Setup

For the best experience, we recommend setting up a conda environment with Python 3.11:

```bash
# Create new environment with Python 3.11
conda create -n mlops-py311 python=3.11

# Activate the environment
conda activate mlops-py311

# Verify Python version
python --version
```

**Note**: Python 3.12+ may cause compatibility issues with MLflow. If you encounter `AttributeError: 'EntryPoints' object has no attribute 'get'`, please use Python 3.11.

---

##  Contributing

Feel free to fork this repo, enhance the exercises, and submit a pull request. For bugs or feature requests, please open an issue.



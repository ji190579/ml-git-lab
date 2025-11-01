# Day 1: MLOps / LLMOps Foundation – Bootcamp

Welcome to **Day 1** of the MLOps/LLMOps Bootcamp! This repository contains a set of **hands-on exercises** that introduce core concepts and tools for machine learning operations. You'll work with tools like **Git**, **MLflow**, **Docker**, and **CI/CD pipelines**, building real workflows from development to deployment.

---

## 🎯 Learning Objectives

By the end of Day 1, you will be able to:
- **Version control** ML code using Git
- **Track experiments** and model performance with MLflow
- **Containerize** ML applications using Docker
- **Build complete ML pipelines** with preprocessing, training, and deployment
- **Automate CI/CD** workflows using GitHub Actions
- **Deploy ML models** as production-ready APIs

---

## 📁 Repository Structure Overview

### 1. `lesson-2-git/` – Version Control with Git
**Objective**: Learn Git fundamentals for ML project management

- Implement a **Random Forest model** on the **Iris dataset**
- Learn **Git commands** for version control
- Track code changes and collaborate effectively

🔗 See [lesson-2-git/README.md](lesson-2-git/README.md) for details and instructions.

---

### 2. `lesson-3-mlflow/` – Experiment Tracking with MLflow
**Objective**: Master experiment tracking and model management

- Track **Logistic Regression model** for **air quality classification**
- Use **MLflow Tracking UI** for experiment visualization
- Log parameters, metrics, and model versions
- Compare different model runs

🔗 See [lesson-3-mlflow/README.md](lesson-3-mlflow/README.md) for details and setup.

---

### 3. `lesson-4-docker/` – Model Deployment with Docker
**Objective**: Containerize ML applications for consistent deployment

- Build and deploy an **Age Detection model** using **Flask**
- Containerize the application using **Docker**
- Learn to run ML models as APIs in isolated environments
- Understand containerization benefits

🔗 See [lesson-4-docker/README.md](lesson-4-docker/README.md) for Docker usage and running the app.

---

### 4. `lesson-5-ml-pipeline/` – ML Pipeline with MLflow & Flask
**Objective**: Build end-to-end ML pipelines

- Implement a complete **machine learning pipeline** for income classification
- **Data preprocessing pipeline** with feature engineering
- **Model training** with experiment tracking via MLflow
- **Model deployment** using Flask & Docker
- **Production-ready** ML application

🔗 See [lesson-5-ml-pipeline/README.md](lesson-5-ml-pipeline/README.md) for step-by-step usage.

---

### 5. `lesson-6-ci-cd/` – CI/CD with GitHub Actions
**Objective**: Automate ML workflows with CI/CD

- Extend the ML pipeline by integrating **CI/CD** using **GitHub Actions**
- **Automate testing** of ML models and data
- **Automate building** and deployment of Docker containers
- **Continuous integration** for ML projects
- **Production deployment** best practices

🔗 See [lesson-6-ci-cd/README.md](lesson-6-ci-cd/README.md) for automation setup and workflow explanation.

---

## 🛠️ Prerequisites

Ensure the following tools are installed before starting the exercises:

### **Core Tools**
- **Python 3.9+** - Primary programming language
- **Git** - Version control system
- **Docker** - Containerization platform

### **Python Packages**
- **MLflow** - Experiment tracking and model management
- **Flask** - Web framework for API development
- **scikit-learn** - Machine learning library
- **pandas** - Data manipulation
- **pytest** - Testing framework

### **Optional Tools**
- **Jupyter Notebook** - Interactive development
- **Postman** - API testing
- **GitHub CLI** - GitHub integration

---

## 🚀 Getting Started

1. **Clone the repository**:
   ```bash
   git clone https://github.com/AmmarMohanna/oreilly-mlops-bootcamp.git
   cd oreilly-mlops-bootcamp/Day1
   ```

2. **Install dependencies** for each lesson:
   ```bash
   cd lesson-X-name
   pip install -r requirements.txt
   ```

3. **Follow the lesson README** for specific instructions

4. **Complete exercises** in order for best learning experience

---

## 📊 Learning Path

```
lesson-2-git/     → Git fundamentals
       ↓
lesson-3-mlflow/  → Experiment tracking
       ↓
lesson-4-docker/  → Containerization
       ↓
lesson-5-ml-pipeline/ → End-to-end ML pipeline
       ↓
lesson-6-ci-cd/   → Automation & CI/CD
```

---

## 🔧 Troubleshooting

### Common Issues
- **Port conflicts**: Some lessons use port 5000 (macOS AirPlay conflict) - use port 8000 instead
- **MLflow UI issues**: Use `mlflow ui --port 5001` to avoid conflicts
- **Docker permission errors**: Ensure Docker is running and you have proper permissions
- **GitHub Actions**: Check the Actions tab for workflow status and logs

### Getting Help
- Check individual lesson README files for specific troubleshooting
- Review error messages in terminal output
- Ensure all prerequisites are properly installed

---

## Contributing

Feel free to fork the repo, improve the content, and submit a pull request. For suggestions or issues, open a GitHub Issue.


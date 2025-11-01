# Lesson 5: End-to-End ML Pipeline – Adult Income Classification

This lesson demonstrates how to build, train, track, and deploy a full machine learning pipeline for the **Adult Income Classification** problem using real census data.

---

##  Objective

Classify individuals into one of two income categories:
- **Group 1**: Income ≤ 50K  
- **Group 2**: Income > 50K  

The model uses 1994 U.S. Census data from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/adult).

---

##  Dataset Overview

The dataset contains demographic and employment-related features:
- **Numerical**: age, fnlwgt, education-num, capital-gain, capital-loss, hours-per-week
- **Categorical**: workclass, education, marital-status, occupation, relationship, race, sex, native-country
- **Target**: income (`<=50K`, `>50K`)

---

##  Pipeline Overview

### 1. Data Ingestion
- Load data from `adult.data`
- Perform exploratory data analysis

### 2. Data Preprocessing
- Clean missing and inconsistent entries
- Encode target (`<=50K`: 0, `>50K`: 1)
- Transform features:
  - Scale numeric features (StandardScaler)
  - Encode categorical features (OneHotEncoder)
- Apply SMOTE for class balancing

### 3. Model Training & Tracking
- Train a `RandomForestClassifier` using the transformed dataset
- Use **MLflow** to:
  - Track experiment metadata (parameters, metrics)
  - Save models and pipelines for reproducibility

### 4. Deployment
- Save model and preprocessing pipeline using `joblib`
- Create a **Flask API** (`app.py`) for real-time inference
- Containerize the app using **Docker**
- Test the deployed API with **Postman**

---

##  Project Structure

- `data/`: Input dataset (`adult.data`)
- `data_pipeline/`: Scripts for EDA and preprocessing
- `train.py`: Trains model and logs to MLflow
- `app.py`: Flask API for inference
- `Dockerfile`: Containerizes the API
- `requirements.txt`: Required packages

##  How to Use
1. **Clone the repo:**
   ```bash
   git clone https://github.com/AmmarMohanna/oreilly-mlops-bootcamp.git
   cd oreilly-mlops-bootcamp/Day1/lesson-5-ml-pipeline

2. **Install Required Libraries:**
    ```bash
    pip install -r requirements.txt

3. **Run preprocessing & training:**
   ```bash
   python train.py
   
 Don't forget to replace the run ID with the one from your own run in the app.py 
 
4. **Start Flask app locally:**
    ```bash
    python app.py
    
5. **OR build with Docker:**
    ```bash
    docker build -t income-classifier .
    docker run -p 8000:8000 income-classifier

Use API at http://localhost:8000

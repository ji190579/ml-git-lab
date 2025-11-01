
# lesson-7-ab-testing

## A/B Testing Simulator for Diabetes Prediction using FastAPI

This lesson walks through building an A/B testing simulator for two machine learning models deployed using **FastAPI**, allowing you to test and compare their performance in predicting diabetes risk.

---

## Objectives

* Train two models (Logistic Regression & Random Forest) for diabetes prediction
* Deploy both models behind a FastAPI `/predict` endpoint
* Simulate a 50/50 traffic split for A/B testing
* Log predictions and analyze model performance metrics

---

## Prerequisites

* Python 3.x
* Basic knowledge of machine learning
* Familiarity with FastAPI

---

## Project Structure

* `training.py`: Train and save both models
* `app.py`: FastAPI app to serve predictions and route traffic
* `simulator.py`: Simulates multiple client requests
* `performance.py`: Fetches logs and evaluates accuracy
* `requirements.txt`: Dependencies
* `diabetes_data.csv`: Dataset used to train the models

---

## How to use

1. **Clone the repo:**

   ```bash
   git clone https://github.com/AmmarMohanna/oreilly-mlops-bootcamp.git
   cd oreilly-mlops-bootcamp/Day2/lesson-7-ab-testing
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Train and save the models:**

   ```bash
   python training.py
   ```

   This will save models and preprocessors under the `models/` folder.

4. **Run the FastAPI app:**

   ```bash
   uvicorn app:app --reload
   ```

5. **Test the API:**
   Send a POST request to:

   ```
   http://localhost:8000/predict
   ```

   With sample JSON:

   ```json
   {
     "features": {
       "age": 50,
       "gender": "Male",
       "smoking_history": "never",
       "hypertension": 0,
       "heart_disease": 0,
       "bmi": 25.0,
       "HbA1c_level": 6.0,
       "blood_glucose_level": 140
     },
     "true_label": 1
   }
   ```

6. **Simulate 100+ requests:**

   ```bash
   python simulator.py
   ```

7. **Evaluate model performance:**

   ```bash
   python performance.py
   ```



import requests
import random
import json

url = "http://localhost:8000/predict"

# Define possible categories
genders = ["Male", "Female"]
smoking_histories = ["never", "former", "current", "not current", "ever", "unknown"]

results = []

# Simulate 100 requests
for i in range(100):
    sample = {
        "features": {
            "age": random.randint(20, 80),
            "bmi": round(random.uniform(18, 40), 1),
            "HbA1c_level": round(random.uniform(4.0, 10.0), 1),
            "blood_glucose_level": random.randint(70, 200),
            "gender": random.choice(genders),
            "smoking_history": random.choice(smoking_histories),
            "hypertension": random.choice([0, 1]),
            "heart_disease": random.choice([0, 1])
        },
        "true_label": random.choice([0, 1])  # randomly assign true labels
    }

    response = requests.post(url, json=sample)
    if response.status_code == 200:
        results.append(response.json())
    else:
        print(f"Request {i} failed: {response.text}")

print("Done sending requests!")

from fastapi import FastAPI, Request
import pickle
import numpy as np
import uvicorn

# Load models and scaler
with open("models/model_a.pkl", "rb") as f:
    model_a = pickle.load(f)

with open("models/model_b.pkl", "rb") as f:
    model_b = pickle.load(f)

with open("models/scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# Load dataset to identify columns
numerical_features = ['age', 'bmi', 'HbA1c_level', 'blood_glucose_level']
categorical_features = ['gender', 'smoking_history']
other_features = ['hypertension', 'heart_disease']

# Load encoders for categorical features
encoders = {}
for feature in categorical_features:
    with open(f"models/encoder_{feature}.pkl", "rb") as f:
        encoders[feature] = pickle.load(f)

# Initialize FastAPI app
app = FastAPI()

# Store logs in memory
logs = []

# Counter to alternate models A/B
counter = 0

@app.post("/predict")
async def predict(request: Request):
    global counter
    counter += 1
    # Alternating between model A and B
    assigned_model = "A" if counter % 2 == 0 else "B"

    data = await request.json()
    feature_dict = data.get("features") 

    # Prepare numerical data
    numerical_data = []
    for col in numerical_features:
        numerical_data.append(float(feature_dict[col]))
    numerical_data = np.array(numerical_data).reshape(1, -1)

    # Scale numerical features
    numerical_data_scaled = scaler.transform(numerical_data)

    # Prepare categorical data (apply label encoding)
    categorical_data = []
    for col in categorical_features:
        le = encoders[col]
        try:
            encoded_val = le.transform([feature_dict[col]])[0]
        except ValueError:
            return {"error": f"Invalid category '{feature_dict[col]}' for feature '{col}'. Expected one of {list(le.classes_)}"}
        categorical_data.append(encoded_val)
    categorical_data = np.array(categorical_data).reshape(1, -1)

    # Prepare other features (as numerical, no encoding)
    other_data = []
    for col in other_features:
        other_data.append(float(feature_dict[col]))
    other_data = np.array(other_data).reshape(1, -1)

    # Combine scaled numerical and encoded categorical features
    processed_features = np.hstack((numerical_data_scaled, categorical_data, other_data))

    # Get prediction from the selected model
    if assigned_model == "A":
        prediction = int(model_a.predict(processed_features)[0])
    else:
        prediction = int(model_b.predict(processed_features)[0])

    # Log result
    log_entry = {
        "input": feature_dict,
        "model": assigned_model,
        "prediction": prediction,
        "true_label": data.get("true_label")
    }
    logs.append(log_entry)

    return {"model": assigned_model, "prediction": prediction}

@app.get("/logs")
def get_logs():
    return logs

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

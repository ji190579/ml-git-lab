from flask import Flask, request, jsonify
import mlflow.sklearn
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from imblearn.over_sampling import SMOTE
import joblib
import os

app = Flask(__name__)

# Get the current directory and construct dynamic paths
current_dir = os.path.dirname(os.path.abspath(__file__))

# Load the latest model from MLflow
try:
    # Get the experiment by name
    experiment = mlflow.get_experiment_by_name("Income_Classification")
    if experiment is None:
        raise Exception("No experiment found with name 'Income_Classification'")
    
    # Get the latest run from the experiment
    runs = mlflow.search_runs(experiment_ids=[experiment.experiment_id], order_by=["start_time DESC"], max_results=1)
    if runs.empty:
        raise Exception("No runs found in the experiment")
    
    latest_run = runs.iloc[0]
    run_id = latest_run.run_id
    
    # Load the model from the latest run
    model_uri = f"runs:/{run_id}/model"
    model = mlflow.sklearn.load_model(model_uri)
    print(f"Loaded model from run: {run_id}")
    
except Exception as e:
    print(f"Error loading MLflow model: {e}")
    print("Falling back to local model file...")
    # Fallback to local model file
    model_path = os.path.join(current_dir, "model", "rf_model.pkl")
    if os.path.exists(model_path):
        model = joblib.load(model_path)
        print("Loaded local model file")
    else:
        raise Exception("No model found locally or in MLflow")

# Load preprocessor
preprocessor_path = os.path.join(current_dir, "model", "preprocessor.pkl")
if os.path.exists(preprocessor_path):
    preprocessor = joblib.load(preprocessor_path)
else:
    raise Exception("Preprocessor file not found. Please run training first.")
 
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Check if the input is in JSON format
        data = request.get_json()

        if not data:
            return jsonify({"error": "No input data provided or invalid format"}), 400

        # Convert the data to a pandas DataFrame
        data = pd.DataFrame([data])

        # Apply preprocessing to input data
        processed_data = preprocessor.transform(data)
        
        # Make the prediction
        prediction = model.predict(processed_data)

        # Map prediction back to label
        label_map = {0: "<=50K", 1: ">50K"}
        predicted_label = label_map[int(prediction[0])]

        # Return the prediction
        return jsonify({"prediction": predicted_label})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

import pandas as pd
import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib
import os

from data_pipeline.preprocessing import load_and_preprocess_data  

def train():
    X_train, X_test, y_train, y_test, preprocessor = load_and_preprocess_data()

    # Set MLflow tracking URI to local directory for CI environment
    mlflow.set_tracking_uri("file:./mlruns")
    mlflow.set_experiment("Income_Classification")
    with mlflow.start_run():

        clf = RandomForestClassifier(n_estimators=100, random_state=42)
        clf.fit(X_train, y_train)

        y_pred = clf.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        report = classification_report(y_test, y_pred, output_dict=True)

        mlflow.log_param("model_type", "RandomForest")
        mlflow.log_metric("accuracy", acc)

        for label, scores in report.items():
            if isinstance(scores, dict):  
                mlflow.log_metric(f"{label}_precision", scores["precision"])
                mlflow.log_metric(f"{label}_recall", scores["recall"])

        # Create model directory if it doesn't exist
        os.makedirs("model", exist_ok=True)
        
        # Save model and preprocessor
        joblib.dump(clf, "model/rf_model.pkl")
        joblib.dump(preprocessor, "model/preprocessor.pkl")
        
        # Try to log model to MLflow, but don't fail if it doesn't work
        try:
            mlflow.sklearn.log_model(clf, "model")
        except Exception as e:
            print(f"Warning: Could not log model to MLflow: {e}")
            print("Model saved locally only.")

if __name__ == "__main__":
    train()

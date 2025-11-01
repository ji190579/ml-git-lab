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
        model_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "model")
        os.makedirs(model_dir, exist_ok=True)
        
        # Save model and preprocessor with dynamic paths
        model_path = os.path.join(model_dir, "rf_model.pkl")
        preprocessor_path = os.path.join(model_dir, "preprocessor.pkl")
        
        joblib.dump(clf, model_path)
        joblib.dump(preprocessor, preprocessor_path)
        mlflow.sklearn.log_model(clf, "model")

if __name__ == "__main__":
    train()

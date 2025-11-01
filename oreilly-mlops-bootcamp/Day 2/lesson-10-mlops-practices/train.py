import pandas as pd
import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib
import os
from data_pipeline.preprocessing import load_and_preprocess_data  


# Ensure the directory exists
os.makedirs(os.path.dirname('model/'), exist_ok=True)

def train():
    X_train, X_test, y_train, y_test, preprocessor = load_and_preprocess_data()
    mlflow.set_tracking_uri("http://localhost:5001")
    mlflow.set_experiment("Income_Classification_Randomforest")
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

        # Save model and preprocessor
        joblib.dump(clf, "model/rf_model.pkl")
        joblib.dump(preprocessor, "model/preprocessor.pkl")
        mlflow.sklearn.log_model(
            clf,
            artifact_path="model",
            registered_model_name="IncomeClassifier"
        )


if __name__ == "__main__":
    train()

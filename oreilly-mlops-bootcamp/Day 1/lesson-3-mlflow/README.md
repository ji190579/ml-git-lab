# MLflow Experiment Tracking - Air Quality Classification

This lesson demonstrates MLflow experiment tracking using a Jupyter notebook for air quality classification.

## Objectives

By the end of this hands-on session, you will be able to:
- Set up a machine learning environment with MLflow
- Preprocess and prepare a dataset for classification
- Train and evaluate a logistic regression model
- Track experiments and model performance using MLflow Tracking
- Compare different model runs and load a saved model for inference

## Prerequisites

- Python 3.7+
- Any IDE (e.g., VS Code)
- Jupyter Notebook installed

## Project Structure

```
air_quality_mlflow/
│
├── air_quality.csv
├── requirements.txt
└── mlflow-Experiment Tracking.ipynb
```

- **air_quality.csv**: The dataset file containing air quality information
- **requirements.txt**: A list of all the Python libraries required to run the notebook
- **mlflow-Experiment Tracking.ipynb**: The Jupyter notebook where all hands-on steps are executed

## Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Start Jupyter Notebook
```bash
jupyter notebook
```

### 3. Open the Notebook
Open `mlflow- Experiment Tracking.ipynb` in your browser.

### 4. Fix the Connection Issue (IMPORTANT)
Before running the notebook cells, add this code in a new cell at the beginning:

```python
import mlflow
mlflow.set_tracking_uri("file:./mlruns")
```

### 5. Run All Cells
Execute all cells in the notebook. The experiment will be logged locally in the `mlruns` folder.

## Detailed Steps

### 1. Set Up Environment
- Download or clone the project repository
- Navigate to the project directory in your terminal or command prompt
- Install dependencies: `pip install -r requirements.txt`

### 2. Open the Jupyter Notebook
Open `mlflow-Experiment Tracking.ipynb` and follow along with these main sections:

#### Prepare the Data
- Load `air_quality.csv`
- Remove the target column (Air_Quality_Category) from the feature set
- Encode the target labels using LabelEncoder
- Standardize the feature data using StandardScaler

#### Split and Train the Model
- Split the dataset into training and testing sets (80/20)
- Define logistic regression parameters (solver, max_iter)
- Train the model on the training set

#### Experiment Tracking with MLflow
- Initialize MLflow
- Start a run and log:
  - Tags (e.g., experiment name, model type)
  - Parameters (e.g., solver type)
  - Metrics (accuracy, precision, recall, F1-score)
  - The trained model using `mlflow.sklearn.log_model()`

#### Load a Trained Model
- Use a run_id from a previous MLflow run
- Load the model using `mlflow.sklearn.load_model()`
- Use it to make predictions

### 3. View in MLflow UI
Launch the MLflow UI in a new terminal window:
```bash
mlflow ui --port 5001
```

Open your browser and go to: http://localhost:5001

In the UI:
- Click on your experiment: Air Quality Classification
- View all runs and logged details
- View the model artifacts

### 4. Tweak Parameters and Compare Runs
- Modify the solver parameter in the notebook: Change from "lbfgs" to "sag" in the logistic regression initialization
- Re-run the experiment cell to trigger a new MLflow run
- Go to the MLflow UI:
  - Click on both runs (hold Ctrl or Shift to multi-select)
  - Click on Compare
  - Use a scatter plot:
    - Set X-axis to `params.solver`
    - Set Y-axis to `metrics.accuracy`

## View Your Experiments

After running the notebook, you can view your experiments:

```python
import mlflow
import pandas as pd

# View all experiments
experiments = mlflow.search_experiments()
for exp in experiments:
    print(f"Experiment: {exp.name}")
    
    # View runs in this experiment
    runs = mlflow.search_runs(experiment_ids=[exp.experiment_id])
    for idx, run in runs.iterrows():
        print(f"  Run ID: {run['run_id']}")
        print(f"  Accuracy: {run.get('metrics.accuracy', 'N/A')}")
```

## Files
- `mlflow- Experiment Tracking.ipynb`: Main notebook
- `air_quality.csv`: Dataset
- `requirements.txt`: Dependencies

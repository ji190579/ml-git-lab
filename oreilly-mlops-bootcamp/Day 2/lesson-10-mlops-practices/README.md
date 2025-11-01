
# lesson-10-mlops-practices

## End-to-End MLOps: Model Registry, Monitoring & Kubernetes Deployment

This project demonstrates a full MLOps pipeline using the UCI Adult Income dataset. It integrates **MLflow**, **Flask**, **Prometheus**, **Grafana**, and **Kubernetes** to create a scalable and monitorable ML deployment.

---

## Objectives

* Train and version models using **MLflow**
* Serve predictions using a **Flask API**
* Monitor performance with **Prometheus** and **Grafana**
* Deploy everything with **Kubernetes**

---

## Prerequisites

* Python 3.11 (required for MLflow compatibility)
* Docker + Docker Hub account
* A Kubernetes cluster (e.g., Docker Desktop with K8s enabled)
* `kubectl` configured
* MLflow installed
* Prometheus & Grafana Docker images

---

##  Project Structure 


* **`app.py`** – Serves predictions + metrics
* **`dockerfile`** – Container build instructions
* **`requirements.txt`** – Required Python packages
* **`data/`** – Raw + new datasets
* **`data_pipeline/`** – Data cleaning + encoding
* **`train.py`** – Model training + logging
* **`test/`** – Unit + API testing
* **`k8s-deployment.yaml`** – Flask deployment + service
* **`monitoring-deployment.yaml`** – Monitoring stack deployment

---

## How to Use

1. **Set Up Conda Environment (Recommended)**

    Create and activate a conda environment with Python 3.11:

    ```bash
    # Create new environment with Python 3.11
    conda create -n mlops-py311 python=3.11
    
    # Activate the environment
    conda activate mlops-py311
    
    # Verify Python version
    python --version
    ```

2. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

3. **Train & Register Your Model (MLflow)**

    Start the MLflow UI:

    ```bash
    mlflow ui --port 5001
    ```

    Visit `http://localhost:5001`.

    Train and register a model:

    ```bash
    python train.py
    ```

4. **Build and Push Docker Image**

    ```bash
    docker login
    docker build -t yourdockerhub/income-flask-app:latest .
    docker push yourdockerhub/income-flask-app:latest
    ```


5. **Kubernetes Deployment**

    Deploy Flask app, Prometheus, and Grafana:

    ```bash
    kubectl apply -f monitoring-deployment.yaml
    kubectl apply -f k8s-deployment.yaml
    ```
6. **Test the API**

| Service    | URL                                              |
| ---------- | ------------------------------------------------ |
| Flask API  | [http://localhost:30800/predict](http://localhost:30800/predict) |
| Prometheus | [http://localhost:30909](http://localhost:30909) |
| Grafana    | [http://localhost:30009](http://localhost:30009) |


7. **Monitoring**

* Login: `admin / admin`
* Add Data Source:

  * Type: **Prometheus**
  * URL: `http://prometheus-service:9090`
* Create Dashboards:

  * `predict_requests_total`
  * `predict_exceptions_total`
  * `predict_request_latency_seconds`

8. **Delete Deployments**

* kubectl delete -f k8s-deployment.yaml
* kubectl delete -f monitoring-deployment.yaml

---

## Troubleshooting

### MLflow Compatibility Issues

If you encounter `AttributeError: 'EntryPoints' object has no attribute 'get'`:

1. **Ensure you're using Python 3.11**:
   ```bash
   python --version
   ```

2. **If using Python 3.12+, create a conda environment with Python 3.11**:
   ```bash
   conda create -n mlops-py311 python=3.11
   conda activate mlops-py311
   pip install -r requirements.txt
   ```

3. **Alternative: Use MLflow server instead of UI**:
   ```bash
   python -m mlflow server --port 5001 --host 0.0.0.0
   ```

### Port Conflicts

* **Port 5000**: Often reserved on macOS for AirPlay Receiver
* **Solution**: Use port 5001 as shown in the instructions above


## Summary

You’ve built an end-to-end MLOps pipeline that includes:

* **Model training + versioning** with MLflow
* **Prediction serving** with Flask
* **Real-time monitoring** with Prometheus
* **Live dashboards** with Grafana
* **Production-grade deployment** via Kubernetes



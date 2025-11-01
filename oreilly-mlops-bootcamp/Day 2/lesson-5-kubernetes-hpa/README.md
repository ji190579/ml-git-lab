# Lesson 5: Kubernetes HPA

## Autoscaling the Age Detection API using Kubernetes Horizontal Pod Autoscaler (HPA)

This lesson shows how to set up Horizontal Pod Autoscaling (HPA) for the age-detect API to automatically scale the number of pods based on CPU usage.

## Objectives

- Configure HPA to auto-scale between 1 and 10 replicas
- Track CPU usage using metrics-server
- Simulate load to trigger auto-scaling behavior

## Prerequisites

- A Kubernetes cluster (e.g., Docker Desktop, Minikube)
- kubectl configured to access the cluster
- Working deployment from previous lesson (age-detect API)

## Project Structure

| File | Purpose |
|------|---------|
| `k8s-deployment.yml` | Defines the age-detect service and deployment |
| `hpa.yml` | HPA configuration for CPU-based scaling |

## How to Use

### 1. Navigate to the lesson folder:

```bash
cd oreilly-mlops-bootcamp/Day2/lesson-5-kubernetes-hpa
```

### 2. Apply the age-detect deployment and service:

```bash
kubectl apply -f k8s-deployment.yml
```

### 3. Install metrics-server:

```bash
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
```

Then patch it for local clusters:

```bash
kubectl patch deployment metrics-server -n kube-system \
  --type='json' \
  -p='[
    {"op": "add", "path": "/spec/template/spec/containers/0/args/-", "value": "--kubelet-insecure-tls"},
    {"op": "add", "path": "/spec/template/spec/containers/0/args/-", "value": "--kubelet-preferred-address-types=InternalIP,Hostname,InternalDNS,ExternalDNS,ExternalIP"}
  ]'

kubectl delete pod -n kube-system -l k8s-app=metrics-server
```

### 4. Confirm metrics-server is working:

```bash
kubectl get --raw "/apis/metrics.k8s.io/v1beta1/nodes"
```

You should get a JSON response with node metrics.

### 5. Apply the HPA:

```bash
kubectl apply -f hpa.yml
```

### 6. Check HPA status:

```bash
kubectl get hpa
kubectl describe hpa age-detect-hpa
```

### 7. Simulate load to trigger autoscaling:

```bash
kubectl run loadgen --restart=Never --image=busybox:1.28 -- \
  /bin/sh -c "while true; do wget -q -O- http://age-detect:5000/detect_age; done"
```

### 8. Monitor autoscaling:

```bash
kubectl get hpa -w
```

And in another terminal:

```bash
kubectl get pods -w
```

## Clean Up

```bash
kubectl delete -f hpa.yml
kubectl delete -f k8s-deployment.yml
kubectl delete pod loadgen --ignore-not-found
```


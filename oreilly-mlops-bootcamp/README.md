# 🚀 MLOps Bootcamp: From Foundation to Production

A comprehensive, hands-on MLOps bootcamp that takes you from basic concepts to production-ready machine learning deployments. This repository contains **10+ practical lessons** covering the entire MLOps lifecycle using real-world tools and datasets.

![MLOps Pipeline](https://img.shields.io/badge/MLOps-Pipeline-blue)
![Python](https://img.shields.io/badge/Python-3.11+-green)
![Docker](https://img.shields.io/badge/Docker-Containerized-orange)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Orchestration-purple)
![MLflow](https://img.shields.io/badge/MLflow-Experiment%20Tracking-red)

---

## 🎯 What You'll Learn

This bootcamp covers the complete MLOps journey:

### **Day 1: MLOps Foundation** 
- **Version Control** with Git for ML projects
- **Experiment Tracking** with MLflow
- **Containerization** with Docker
- **ML Pipelines** with preprocessing, training, and deployment
- **CI/CD Automation** with GitHub Actions

### **Day 2: Applied MLOps**
- **Kubernetes Deployment** for scalable ML services
- **Horizontal Pod Autoscaling** (HPA) for dynamic scaling
- **A/B Testing** for model comparison and traffic control
- **End-to-End MLOps** with monitoring and observability

---

## 📚 Repository Structure

```
oreilly-mlops-bootcamp/
├── Day 1/                          # Foundation concepts
│   ├── lesson-2-git/              # Version control with Git
│   ├── lesson-3-mlflow/           # Experiment tracking
│   ├── lesson-4-docker/           # Containerization
│   ├── lesson-5-ml-pipeline/      # End-to-end ML pipeline
│   └── lesson-6-ci-cd/            # CI/CD automation
│
└── Day 2/                          # Production deployment
    ├── lesson-2-kubernetes-basics/ # Kubernetes fundamentals
    ├── lesson-5-kubernetes-hpa/    # Auto-scaling
    ├── lesson-7-ab-testing/        # A/B testing
    └── lesson-10-mlops-practices/  # Complete MLOps workflow
```

---

## 🛠️ Prerequisites

### **Core Requirements**
- **Python 3.11** (required for MLflow compatibility)
- **Git** - Version control system
- **Docker** - Containerization platform
- **Kubectl** - Kubernetes command-line tool
- **Kubernetes cluster** (Docker Desktop with K8s enabled)

### **Python Packages**
- **MLflow** - Experiment tracking and model management
- **Flask/FastAPI** - Web frameworks for API development
- **scikit-learn** - Machine learning library
- **pandas** - Data manipulation
- **pytest** - Testing framework
- **prometheus-client** - Monitoring metrics

### **Optional Tools**
- **Jupyter Notebook** - Interactive development
- **Postman** - API testing
- **GitHub CLI** - GitHub integration

---

## 🚀 Quick Start

### 1. **Environment Setup**

```bash
# Clone the repository
git clone https://github.com/AmmarMohanna/oreilly-mlops-bootcamp.git
cd oreilly-mlops-bootcamp

# Create conda environment with Python 3.11
conda create -n mlops-py311 python=3.11
conda activate mlops-py311

# Verify Python version
python --version  # Should show Python 3.11.x
```

### 2. **Install Dependencies**

```bash
# For each lesson, install requirements
cd Day\ 1/lesson-2-git/
pip install -r requirements.txt

# Repeat for other lessons as needed
```

### 3. **Start Learning**

Begin with Day 1 lessons in order:
1. **Git fundamentals** → `Day 1/lesson-2-git/`
2. **MLflow tracking** → `Day 1/lesson-3-mlflow/`
3. **Docker containerization** → `Day 1/lesson-4-docker/`
4. **ML pipelines** → `Day 1/lesson-5-ml-pipeline/`
5. **CI/CD automation** → `Day 1/lesson-6-ci-cd/`

Then progress to Day 2 for production deployment:
6. **Kubernetes basics** → `Day 2/lesson-2-kubernetes-basics/`
7. **Auto-scaling** → `Day 2/lesson-5-kubernetes-hpa/`
8. **A/B testing** → `Day 2/lesson-7-ab-testing/`
9. **Complete MLOps** → `Day 2/lesson-10-mlops-practices/`

---

## 📖 Detailed Lesson Overview

### **Day 1: Foundation**

| Lesson | Focus | Tools | Dataset |
|--------|-------|-------|---------|
| **Git** | Version control | Git, GitHub | Iris dataset |
| **MLflow** | Experiment tracking | MLflow UI | Air quality data |
| **Docker** | Containerization | Docker, Flask | Age detection model |
| **ML Pipeline** | End-to-end workflow | MLflow, Flask, Docker | Adult income data |
| **CI/CD** | Automation | GitHub Actions | Adult income data |

### **Day 2: Production**

| Lesson | Focus | Tools | Dataset |
|--------|-------|-------|---------|
| **Kubernetes** | Container orchestration | K8s, Docker | Age detection model |
| **HPA** | Auto-scaling | K8s HPA, Prometheus | Age detection model |
| **A/B Testing** | Model comparison | FastAPI, K8s | Diabetes prediction |
| **Complete MLOps** | Full workflow | MLflow, Flask, K8s, Prometheus, Grafana | Adult income data |

---

## 🎓 Learning Path

```
Day 1: Foundation
├── Git Version Control
├── MLflow Experiment Tracking
├── Docker Containerization
├── ML Pipeline Development
└── CI/CD Automation
         ↓
Day 2: Production
├── Kubernetes Deployment
├── Auto-scaling (HPA)
├── A/B Testing
└── Complete MLOps Workflow
```

---

## 🔧 Troubleshooting

### **Common Issues**

#### **MLflow Compatibility**
```bash
# Error: AttributeError: 'EntryPoints' object has no attribute 'get'
# Solution: Use Python 3.11
conda create -n mlops-py311 python=3.11
conda activate mlops-py311
```

#### **Port Conflicts**
```bash
# macOS AirPlay uses port 5000
# Solution: Use alternative ports
mlflow ui --port 5001
python -m mlflow server --port 5001 --host 0.0.0.0
```

#### **Docker Issues**
```bash
# Ensure Docker is running
docker --version
docker ps
```

#### **Kubernetes Issues**
```bash
# Check cluster status
kubectl cluster-info
kubectl get nodes
```

### **Getting Help**
- Check individual lesson README files for specific troubleshooting
- Review error messages in terminal output
- Ensure all prerequisites are properly installed
- Verify Python version is 3.11 for MLflow compatibility

---

## 🏗️ Architecture Overview

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Development   │    │   Experiment    │    │   Deployment    │
│                 │    │   Tracking      │    │                 │
│  • Git         │───▶│  • MLflow       │───▶│  • Docker       │
│  • Local Dev   │    │  • Model Reg    │    │  • Kubernetes   │
│  • Testing     │    │  • Metrics      │    │  • Monitoring   │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   CI/CD Pipeline│    │   Model Serving │    │   Observability │
│                 │    │                 │    │                 │
│  • GitHub       │    │  • Flask API    │    │  • Prometheus   │
│  • Actions      │    │  • FastAPI      │    │  • Grafana      │
│  • Automation   │    │  • A/B Testing  │    │  • HPA          │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### **Areas for Improvement**
- Additional datasets and use cases
- More advanced Kubernetes configurations
- Additional monitoring and observability tools
- Performance optimization techniques
- Security best practices

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **O'Reilly Media** for the educational framework
- **MLflow** team for the excellent experiment tracking tool
- **Kubernetes** community for container orchestration
- **Open source contributors** who made these tools possible

---

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/AmmarMohanna/oreilly-mlops-bootcamp/issues)
- **Discussions**: [GitHub Discussions](https://github.com/AmmarMohanna/oreilly-mlops-bootcamp/discussions)
- **Documentation**: Check individual lesson README files

---

**Ready to start your MLOps journey?** 🚀

Begin with [Day 1: MLOps Foundation](Day%201/README.md) and work your way through to [Day 2: Applied MLOps](Day%202/README.md) for a complete production-ready MLOps experience! 
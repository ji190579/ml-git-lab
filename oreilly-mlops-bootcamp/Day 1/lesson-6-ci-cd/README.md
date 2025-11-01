
# Lesson 6: CI/CD Pipeline with GitHub Actions

This lesson extends the ML pipeline by automating build, test, and deploy using **CI/CD** via **GitHub Actions**.

##  Objective
Integrate a CI/CD pipeline that:
- Runs tests automatically
- Builds Docker image
- Tests the Flask API in a container
- Provides reliable model training and deployment

##  Files
- All files from `lesson-5-ml-pipeline`
- `.github/workflows/day1_lesson6_ci_cd.yml`: CI/CD workflow for GitHub Actions
- `test/`: Unit test scripts for data and model validation
- `model/`: Directory for trained models (created automatically)

## Jobs Defined
1. **Test (CI)**
    * Checkout code
    * Set up Python 3.9
    * Install dependencies from requirements.txt
    * Train the model using train.py
    * Run unit tests using pytest

2. **Deploy (CD)**: 
    * Triggered only if tests pass
    * Set up Python environment
    * Install dependencies
    * Train model for deployment
    * Build Docker image for Flask app
    * Run the app in a Docker container
    * Send a test request to verify the app is live

##  Key Features
- **Automatic model training** in CI/CD environment
- **Local model storage** for reliable deployment
- **Error handling** for MLflow and model loading
- **Path-based triggers** - only runs when lesson files change
- **Comprehensive testing** of data and model performance

##  How to Use
1. Clone the repo:
   ```bash
   git clone https://github.com/AmmarMohanna/oreilly-mlops-bootcamp.git
   cd oreilly-mlops-bootcamp/Day1/lesson-6-ci-cd
   ```

2. Train the model locally (optional):
   ```bash
   python train.py
   ```

3. Push code to **GitHub**:
   ```bash
   git add .
   git commit -m "Your commit message"
   git push origin main
   ```

4. GitHub Actions will automatically:
   - Run tests on each push to main
   - Train models in CI environment
   - Build and test the Docker image
   - Verify the Flask API is working

##  Troubleshooting
- **Model files missing**: Run `python train.py` locally first
- **MLflow errors**: The app uses local model files as fallback
- **Port conflicts**: App runs on port 8000 (changed from 5000 for macOS compatibility)
- **Dependencies**: All required packages are in requirements.txt


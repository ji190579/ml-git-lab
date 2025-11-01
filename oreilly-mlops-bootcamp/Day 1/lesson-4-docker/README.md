# Hands-On: Deploying an Age Detection Model Using Docker

## Objectives
Welcome to the world of Docker! In this lab, we'll containerize an age detection model that predicts the age bin from an image. You'll learn how to turn your app into a deployable, accessible solution while exploring the fundamentals of Docker.

By the end of this hands-on, you'll be able to:
- Create a Dockerfile for the model.
- Build and run a Docker container.
- Interact with the app using Postman.

## Prerequisites
- Install Docker from [this link](https://docs.docker.com/get-docker/).
- Install Postman from [this link](https://www.postman.com/downloads/).
- Familiarity with Python, Flask, and Docker basics.

## Project Structure
```
age_detection/
|-- app.py       
|-- requirements.txt           
|-- model/   
|   |-- age_net.caffemodel 
|   |-- deploy_age.prototxt    
|-- images/  
```

### app.py
The Flask application script. It:
- Loads the pre-trained model.
- Defines endpoints to process an image and return the predicted age bin.
- Example Endpoint: `/detect_age` accepts an image file and returns the age bin.

### requirements.txt
Contains the dependencies needed to run the application, such as Flask and OpenCV.

### model/
- **age_net.caffemodel**: The pre-trained Caffe model for age prediction. A Caffe model refers to a deep learning model developed using the Caffe framework, which is an open-source deep learning library designed for speed and modularity.
- **deploy_age.prototxt**: Describes the network architecture for age detection including the layers, their types (e.g., convolution, pooling, fully connected), and their parameters (e.g., kernel size, stride, activation functions).

The age detection model is sourced from the following repository:
[Age and Gender Classification GitHub Repo](https://github.com/GilLevi/AgeGenderDeepLearning)

### images/
A folder with example images to test the app.

## Steps

### 1. Create a Dockerfile
The Dockerfile is the starting point for building and running a containerized application. It defines the steps required to create an image that will set up your environment, install dependencies, and execute your app. Here's how to write one for your age detection application.

The Dockerfile will ensure:
- Your application runs in a consistent environment.
- All dependencies are installed automatically.
- The app is ready to process images and predict age bins.

### 2. Build and Run the Docker Image

**Build the Image**: Run the following command in your terminal to build the Docker image:
```bash
docker build -t age_detect .
```

Once you build your Docker image, it will appear in the Docker Desktop application or be listed when you check available images via the command line:
```bash
docker images
```

**Run the Container**: Start a container from the built image:
```bash
docker run -p 8000:8000 age_detect
```

### 3. Test the App
Open Postman and send a POST request to:
`http://localhost:8000/detect_age`

Attach an image file under the form-data body with the key `image`.

The app should return the predicted age bin in JSON format, e.g.:
```json
{"age_interval": "25-32"}
```

### 4. Docker Commands for Managing the App

**Check Running Containers**:
```bash
docker ps
```

**Stop the Container**:
```bash
docker stop <container-id>
```

**Remove the Container**:
```bash
docker rm <container-id>
```

**Remove the Image**:
```bash
docker rmi age_detect
```

## Conclusion
Congratulations! You have successfully containerized and deployed an age detection model using Docker. You learned how to build a Dockerfile, create a containerized app, interact with it using Postman, and manage Docker images and containers.


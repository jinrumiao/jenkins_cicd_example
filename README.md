# Build CI/CD Workflow using Jenkins and ArgoCD ♾️

## 🌱Intro
The CI/CD pipeline is an automated software process that encompasses building, testing, and deploying applications. Whenever developers push code changes to a GitHub repository, the CI/CD pipeline is triggered. Once the first two stages of the process are successfully completed, the new code is deployed to the production environment.

In this project, Jenkins handles the building and testing phases by defining a Jenkins pipeline. When developers push their API services to the repository, Jenkins initiates the creation of a new Docker image and tests the functionality of the API within a Docker container. Subsequently, Jenkins pushes the new Docker image to Docker Hub with a new image tag and simultaneously updates the image tag within the YAML file located in the manifest repository. Upon the update of the YAML file, ArgoCD automatically pulls the specified image tag as indicated in the file. Finally, ArgoCD deploys the latest API service to the Kubernetes cluster.

![Imgur](https://imgur.com/hOZSMeg.png)

## ⚙️Libraries


## 🦿Features


## ⚗️Process


## 📚Learnings


## 🛠️Improvement
☑️*

## 🏃‍♂️Running the Project


## 🎞️Video

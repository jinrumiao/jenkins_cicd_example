# Build CI/CD Workflow using Jenkins and ArgoCD ♾️

## 🌱Intro
The CI/CD pipeline is an automated software process that encompasses building, testing, and deploying applications. Whenever developers push code changes to a GitHub repository, the CI/CD pipeline is triggered. Once the first two stages of the process are successfully completed, the new code is deployed to the production environment.

This project demonstrates a simple example of CI/CD (Continuous Integration/Continuous Deployment) using Jenkins and ArgoCD stack. Jenkins handles the building and testing phases by defining a Jenkins pipeline. When developers push their API services to the repository, Jenkins initiates the creation of a new Docker image and tests the functionality of the API within a Docker container. Subsequently, Jenkins pushes the new Docker image to Docker Hub with a new image tag and simultaneously updates the image tag within the YAML file located in the manifest repository. Upon the update of the YAML file, ArgoCD automatically pulls the specified image tag as indicated in the file. Finally, ArgoCD deploys the latest API service to the Kubernetes cluster.

![Imgur](https://imgur.com/hOZSMeg.png)

## ⚙️Techstack
### Jenkins
![Imgur](https://imgur.com/65h0xJX.png)
Jenkins is an open-source automation server used for continuous integration (CI) and continuous deployment (CD). It automates the process of building, testing, and deploying software projects. Jenkins provides a flexible and extensible platform that supports various development tools and technology stacks through plugins.
### ArgoCD
![Imgur](https://imgur.com/S33YR0D.png)
ArgoCD is an open-source tool for continuous delivery, particularly designed for Kubernetes. It automates the deployment of applications and ensures that the application's state matches the desired state. ArgoCD utilizes application definitions stored in Git repositories and monitors their changes to automatically synchronize the deployment status of applications when needed.

## 🏃‍♂️Running the Project
### Prerequisites
- Docker installation
- Git installation
- Kind, kubectl installation
- Github, Docker Hub account

## ✨️Demo
- Jenkins Server
    ![Imgur](https://imgur.com/E87yKz2.png)
- ArgoCD UI Server
    ![Imgur](https://imgur.com/cG4Qy1S.png)
- FastAPI Service
    ![Imgur](https://imgur.com/TGkYAO3.png)

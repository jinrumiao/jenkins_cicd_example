pipeline {
    agent any

    environment {
        IMAGE_TAG = "${BUILD_NUMBER}"
        REGISTRY = "miaojinru/cicd-e2e-example:$IMAGE_TAG"
    }

    triggers {
        pollSCM "H/3 * * * *"
      }

    stages {
        stage('Check Build Number') {
            steps {
                sh 'echo $REGISTRY'
            }
        }
        stage('Show Docker Image') {
            steps {
                echo 'Show Docker Image.'
                sh 'docker images python'
            }
        }
        stage('Build Docker Image and Test') {
            steps {
                script{
                    sh '''
                    echo 'Build Docker Image.'
                    docker build -t $REGISTRY .
                    '''

                    sh '''
                    echo 'Test api in Docker Container.'
                    docker run -d -it --rm --name api_cicd_example $REGISTRY pytest
                    docker logs -f api_cicd_example
                    '''
                }
            }
        }
        stage('Push Docker Image') {
            withDockerRegistry([ credentialsId: "DOCKER_HUB", url: "" ]) {
                sh 'docker push $REGISTRY'
            }
        }
    }
}
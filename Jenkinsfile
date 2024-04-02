pipeline {
    agent any
    triggers {
        pollSCM "H/3 * * * *"
      }
    stages {
        stage('Show Docker Image') {
            steps {
                echo 'Show Docker Image.'
                sh 'docker images python'
            }
        }
        stage('Build Docker Image') {
            steps {
                script{
                    sh '''
                    echo 'Build Docker Image.'
                    docker build -t miaojinru/cicd-e2e-exampl:1 .
                    '''
                }
            }
        }
        stage('Test api') {
            steps {
                script{
                    sh '''
                    echo 'Test api in Docker Container.'
                    docker exec -it miaojinru/cicd-e2e-exampl:1 python3 api_test.py
                    '''
                }
            }
        }
    }
}
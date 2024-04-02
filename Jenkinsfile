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
                    docker run -d --rm --name api_cicd_example miaojinru/cicd-e2e-exampl:1
                    docker exec -it api_cicd_example python3 api_test.py
                    '''
                }
            }
        }
    }
}
pipeline {
    agent any

    environment {
        IMAGE_TAG = "${BUILD_NUMBER}"
        REGISTRY = "miaojinru/cicd-e2e-exampl:$IMAGE_TAG"
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
                    '''

                    customImage = docker.build("$REGISTRY")

                    sh '''
                    echo 'Test api in Docker Container.'
                    '''

                    customImage.inside {
                        sh 'ls'
                        sh 'pytest'
                    }
                }
            }
        }
//         stage('Test api') {
//             steps {
//                 script{
//                     sh '''
//                     echo 'Test api in Docker Container.'
//                     docker run -d --rm --name api_cicd_example miaojinru/cicd-e2e-exampl:1
//                     docker exec -it api_cicd_example python3 api_test.py
//                     '''
//                 }
//             }
//         }
    }
}
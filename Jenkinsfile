pipeline {
    agent {
        node {
            label 'docker-agent-python'
            }
      }
    triggers {
        pollSCM "H/3 * * * *"
      }
    stages {
        stage('Build') {
            steps {
                echo "Building.."
                sh '''
                echo "doing build stuff.."
                ls -ltr
                python3 --version
                pip install --upgrade pip
                pip install --no-cache-dir -r requirements.txt
                '''
                /* pip install --no-cache-dir -r requirements.txt */
            }
        }
        stage('Test') {
            steps {
                echo "Testing.."
                sh '''
                echo "doing test stuff.."
                python3 -m pytest
                '''
                /* python3 greeting.py */
            }
        }
        stage('Build Docker'){
            /* This builds the actual image; synonymous to
             * docker build on the command line */

            app = docker.build("miaojinru/cicd-e2e-exampl:1")
//             steps{
//                 script{
//                     sh '''
//                     echo 'Build Docker Image'
//                     docker build -t miaojinru/cicd-e2e-exampl:1 .
//                     '''
//                 }
//             }
        }
        /* stage('Deliver') {
            steps {
                echo 'Deliver....'
                sh '''
                echo "doing delivery stuff.."
                python3 api_example.py
                cat http://localhost:8000/
                '''
            }
        } */
    }
}
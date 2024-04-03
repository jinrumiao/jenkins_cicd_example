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
            steps {
                script{
                    withDockerRegistry([ credentialsId: "DOCKER_HUB", url: "" ]) {
                    sh 'docker push $REGISTRY'
                    }
                }
            }
        }
        stage('Checkout K8S manifest') {
            steps {
                git(
                    url: "https://github.com/jinrumiao/jenkins_cicd_manifest.git",
                    branch: "master",
                    changelog: true,
                    poll: true
                )
            }
        }
        stage('Update K8S manifest and push to github') {
            steps {
                script{
                    withCredentials([ gitUsernamePassword(credentialsId: "github_jenkins_cicd_manifest", gitToolName: "Default") ]) {
                    sh '''
                        ls -lh
                        cat deploy.yaml
                        sed -i 's/miaojinru\\/cicd-e2e-example:[0-9]\\+/$REGISTRY/g' deploy.yaml
                        cat deploy.yaml

                    '''
//                     git add deploy.yaml
//                         git commit -m 'Updated the deploy.yaml | By Jenkins Pipeline'
//                         git remote -v
//                         git push https://github.com/jinrumiao/jenkins_cicd_manifest.git HEAD:master
                    }
                }
            }
        }
    }
}
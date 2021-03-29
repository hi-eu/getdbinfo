pipeline {
    environment {
    registry = '406858794777.dkr.ecr.ap-southeast-1.amazonaws.com/backend_prod_dbinfo'
    registryCredential = 'aws'
    dockerImage = ''
  }
    agent {
        label 'docker'
    }
    stages {
        stage('Building image') {
            steps{
                script {
                    dockerImage = docker.build registry + ":$BUILD_NUMBER"
                }
            }
        }
        stage('Deploy image') {
            steps{
                script{
                    docker.withRegistry("https://" + registry, "ecr:ap-southeast-1:" + registryCredential) {
                    dockerImage.push()
                    }
                }
            }
        }
    }
}


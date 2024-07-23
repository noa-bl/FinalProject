pipeline {
    agent {
        kubernetes {
            label 'jenkins-slave'
            yamlFile 'runner.yaml'
            defaultContainer 'builder'
        }
    }
    stages {
        stage('Run Pipeline') {
            steps {
                script {
                    echo 'Kubernetes connection is working!'
                }
            }
        }
    }
}

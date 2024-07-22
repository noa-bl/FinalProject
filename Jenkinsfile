pipeline {
    agent {
        kubernetes {
            yamlFile 'charts/final-chart/jenkins-chart/runner.yaml'
            defaultContainer 'builder'
        }
    }

    stages {
        stage("Checkout code") {
            steps {
                checkout scm
            }
        }

        stage("Echo Test") {
            steps {
                container('builder') {
                    sh 'echo "This is a test for the Jenkins pipeline with Kubernetes agent."'
                }
            }
        }
    }
}

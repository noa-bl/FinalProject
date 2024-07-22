pipeline {
    agent {
        kubernetes {
            yamlFile 'charts/final-chart/jenkins-chart/runner.yaml'
            defaultContainer 'builder'
        }
    }
    stages {
        stage("Test") {
            steps {
                echo 'Testing Jenkinsfile with Kubernetes agent'
            }
        }
    }
}

pipeline {
    agent {
        kubernetes {
            label 'jenkins-slave'
            yamlFile 'finalproject-charts/charts/jenkins-chart/runner.yaml'
            defaultContainer 'builder'
            namespace 'default' // Specify the namespace for the runner
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

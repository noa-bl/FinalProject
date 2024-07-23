pipeline {
    agent any
    stages {
        stage('Clone Charts Repository') {
            steps {
                script {
                    // Clone the finalproject-charts repository
                    git url: 'https://github.com/noa-bl/finalproject-charts.git', branch: 'main'
                }
            }
        }
        stage('Run Pipeline') {
            agent {
                kubernetes {
                    yamlFile 'charts/jenkins-chart/runner.yaml' // Path relative to where it will be cloned
                    defaultContainer 'builder'
                }
            }
            steps {
                script {
                    echo 'Kubernetes connection is working!'
                }
            }
        }
    }
}

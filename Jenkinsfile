pipeline {
    agent any
    stages {
        stage('Clone Charts Repository') {
            steps {
                script {
                    // Clone the finalproject-charts repository into a specific directory
                    dir('finalproject-charts') {
                        git url: 'https://github.com/noa-bl/finalproject-charts.git', branch: 'main'
                    }
                    // List the contents to ensure the correct path
                    sh 'ls -la finalproject-charts/charts/jenkins-chart'
                }
            }
        }
        stage('Run Pipeline') {
            agent {
                kubernetes {
                    // Specify the full path where runner.yaml will be located after cloning
                    yamlFile 'finalproject-charts/charts/jenkins-chart/runner.yaml'
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

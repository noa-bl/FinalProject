pipeline {
    agent {
        kubernetes {
            // Directly reference the local path where runner.yaml is located
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

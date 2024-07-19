pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', url: 'https://github.com/noa-bl/FinalProject'
            }
        }
        stage('Build') {
            steps {
                sh 'echo Hello Jenkins!'
            }
        }
    }
}
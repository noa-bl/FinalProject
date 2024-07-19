pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', url: 'git@github.com:noa-bl/FinalProject.git'
            }
        }
        stage('Build') {
            steps {
                sh 'echo Hello Jenkins!!'
            }
        }
    }
}

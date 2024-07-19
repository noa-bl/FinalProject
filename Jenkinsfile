pipeline {
    agent any
    stages {
        stage('Clean Workspace') {
            steps {
                deleteDir()
            }
        }
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', 
                          branches: [[name: 'refs/heads/master']], 
                          userRemoteConfigs: [[url: 'https://github.com/noa-bl/FinalProject']]
                ])
            }
        }
        stage('Build') {
            steps {
                sh 'echo Hello Jenkins!'
            }
        }
    }
}
 

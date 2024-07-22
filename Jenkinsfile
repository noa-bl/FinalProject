pipeline {
    agent any
    triggers {
        githubPush()
    }
    stages {
        stage('Test') {
            steps {
                echo 'last test for triggers'
            }
        }
    }
}
pipeline {
    agent any
    triggers {
        githubPush()
    }
    stages {
        stage("Checkout code") {
            steps {
                checkout scm
            }
        }
        stage("for test") {
            steps {
                echo 'one'
            }
        }
    }
}
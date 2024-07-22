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
        stage("Test") {
            steps {
                echo 'ok?'
            }
        }
    }
}
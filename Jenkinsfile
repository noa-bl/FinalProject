pipeline {
    agent {
        kubernetes {
            yaml """
apiVersion: v1
kind: Pod
metadata:
  labels:
    jenkins: slave
spec:
  containers:
  - name: jnlp
    image: jenkins/inbound-agent:latest
    args: ['\$(JENKINS_SECRET)', '\$(JENKINS_NAME)']
  - name: builder
    image: maven:3.6.3-jdk-8
    command:
    - cat
    tty: true
"""
        }
    }
    triggers {
        githubPush()
    }
    stages {
        stage('Checkout code') {
            steps {
                checkout scm
            }
        }
        stage('Test') {
            steps {
                echo 'This is a test stage using Kubernetes agent'
            }
        }
    }
}

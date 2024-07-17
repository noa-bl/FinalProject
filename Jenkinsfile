pipeline {
    agent {
        kubernetes {
            label 'jenkins-agent'
            defaultContainer 'jnlp'
            yaml """
            apiVersion: v1
            kind: Pod
            metadata:
              labels:
                app: jenkins-agent
            spec:
              containers:
              - name: jnlp
                image: jenkins/inbound-agent:4.10-3
                args: ['\$(JENKINS_SECRET)', '\$(JENKINS_NAME)']
              - name: docker
                image: docker:latest
                command:
                - cat
                tty: true
                volumeMounts:
                - name: docker-sock
                  mountPath: /var/run/docker.sock
              volumes:
              - name: docker-sock
                hostPath:
                  path: /var/run/docker.sock
            """
        }
    }

    stages {
        stage('Build Docker Image') {
            steps {
                container('docker') {
                    script {
                        sh 'docker build -t myapp:${GIT_COMMIT} .'
                    }
                }
            }
        }
        stage('Run Unit Tests') {
            steps {
                container('docker') {
                    script {
                        sh 'pytest'
                    }
                }
            }
        }
        stage('Build HELM Package') {
            steps {
                container('docker') {
                    script {
                        sh 'helm package ./helm-chart'
                    }
                }
            }
        }
        stage('Merge to Master') {
            when {
                branch 'feature/*'
            }
            steps {
                container('docker') {
                    script {
                        if (currentBuild.result == 'SUCCESS') {
                            sh 'git checkout master'
                            sh 'git merge ${BRANCH_NAME}'
                            sh 'git push origin master'
                        } else {
                            error("Tests failed. Not merging to master.")
                        }
                    }
                }
            }
        }
        stage('Push Docker Image') {
            when {
                branch 'master'
            }
            steps {
                container('docker') {
                    script {
                        sh 'docker login -u your-dockerhub-username -p your-dockerhub-password'
                        sh 'docker push myapp:${GIT_COMMIT}'
                    }
                }
            }
        }
    }
    post {
        failure {
            script {
                emailext (
                    subject: "Pipeline Failed: ${currentBuild.fullDisplayName}",
                    body: "Pipeline ${currentBuild.fullDisplayName} failed. Check Jenkins for details.",
                    to: 'noablfdev@gmail.com'
                )
            }
        }
        always {
            script {
                emailext (
                    subject: "Pipeline Completed: ${currentBuild.fullDisplayName}",
                    body: "Pipeline ${currentBuild.fullDisplayName} completed. Check Jenkins for details.",
                    to: 'noablfdev@gmail.com'
                )
            }
        }
    }
}

pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image
                    sh 'docker build -t myapp:${GIT_COMMIT} .'
                }
            }
        }
        stage('Run Unit Tests') {
            steps {
                script {
                    // Run unit tests
                    sh 'pytest'
                }
            }
        }
        stage('Build HELM Package') {
            steps {
                script {
                    // Package HELM chart
                    sh 'helm package ./helm-chart'
                }
            }
        }
        stage('Merge to Master') {
            when {
                branch 'feature/*'
            }
            steps {
                script {
                    // Merge feature branch to master
                    sh 'git checkout master'
                    sh 'git merge ${BRANCH_NAME}'
                    sh 'git push origin master'
                }
            }
        }
    }
    post {
        failure {
            script {
                // Send email notification on failure
                emailext (
                    subject: "Pipeline Failed: ${currentBuild.fullDisplayName}",
                    body: "Pipeline ${currentBuild.fullDisplayName} failed. Check Jenkins for details.",
                    to: 'noablfdev@gmail.com'
                )
            }
        }
        always {
            script {
                // Notify project managers and developers of each run
                emailext (
                    subject: "Pipeline Completed: ${currentBuild.fullDisplayName}",
                    body: "Pipeline ${currentBuild.fullDisplayName} completed. Check Jenkins for details.",
                    to: 'noablfdev@gmail.com'
                )
            }
        }
    }
}

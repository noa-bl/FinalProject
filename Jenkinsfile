pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'noabl/flask-app'
        DOCKERHUB_URL = 'https://registry.hub.docker.com'
        GITHUB_API_URL = 'https://api.github.com'
        GITHUB_REPO = 'noa-bl/FinalProject'
        HELM_CHART_REPO = "noa-bl/FinalProject"
        HELM_CHART_PATH = 'charts/final-chart'
    }
    stages {
        stage("Checkout code") {
            steps {
                checkout scm
            }
        }

        stage("Build Docker image") {
            steps {
                script {
                    dockerImage = docker.build("noabl/flask-app:latest", "--no-cache .")
                }
            }
        }

        stage("Run Unit Tests") {
            steps {
                script {
                    sh 'pytest --cov'
                }
            }
        }

        stage('Push Docker image') {
            when {
                branch 'main'
            }
            steps {
                script {
                    docker.withRegistry(DOCKERHUB_URL, 'docker-cred') {
                        dockerImage.push("${env.BRANCH_NAME}-${env.BUILD_NUMBER}")
                        dockerImage.push('latest')
                    }
                }
            }
        }

        stage('Package Helm Chart') {
            when {
                branch 'main'
            }
            steps {
                script {
                    sh """
                    helm package ${HELM_CHART_PATH} -d .
                    helm repo index . --url https://your_github_username.github.io/helm-charts
                    mv *.tgz docs/
                    mv index.yaml docs/
                    git add docs/
                    git commit -m "Add Helm chart version ${env.BUILD_NUMBER}"
                    git push origin main
                    """
                }
            }
        }

        stage('Email Notification') {
            steps {
                script {
                    emailext (
                        subject: "Build ${currentBuild.fullDisplayName}",
                        body: "Build ${currentBuild.fullDisplayName} completed with status ${currentBuild.currentResult}",
                        to: "your_email@example.com",
                        attachLog: true
                    )
                }
            }
        }

        stage('Create Merge Request') {
            when {
                not {
                    branch 'main'
                }
            }
            steps {
                withCredentials([usernamePassword(credentialsId: 'gh-user-cred', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                    script {
                        def branchName = env.BRANCH_NAME
                        def pullRequestTitle = "Merge ${branchName} into main"
                        def pullRequestBody = "Automatically generated merge request for branch ${branchName} from Jenkins"

                        sh """
                            curl -X POST -u ${PASSWORD}:x-oauth-basic \
                            -d '{ "title": "${pullRequestTitle}", "body": "${pullRequestBody}", "head": "${branchName}", "base": "main" }' \
                            ${GITHUB_API_URL}/repos/${GITHUB_REPO}/pulls
                        """
                    }
                }
            }
        }
    }
}
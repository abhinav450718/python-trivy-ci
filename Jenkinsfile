pipeline {
    agent any

    environment {
        VENV = "venv"
    }

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                python3 -m venv $VENV
                . $VENV/bin/activate
                pip install --upgrade pip
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                . $VENV/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Dependency Scan - Trivy') {
            steps {
                sh '''
                trivy fs --severity HIGH,CRITICAL --exit-code 1 .
                '''
            }
        }

        stage('Static Code Scan - Bandit') {
            steps {
                sh '''
                . $VENV/bin/activate
                bandit -r app/
                '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh '''
                . $VENV/bin/activate
                pytest
                '''
            }
        }

    }

    post {

        success {
            echo "Pipeline executed successfully"
        }

        failure {
            echo "Security vulnerabilities or tests failed"
        }
    }
}

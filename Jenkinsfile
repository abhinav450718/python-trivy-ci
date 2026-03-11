pipeline {
    agent any

    environment {
        VENV = "venv"
    }

    stages {

        stage('Checkout Code') {
            steps {
                echo "Cloning repository..."
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                echo "Creating Python virtual environment"
                sh '''
                python3 -m venv $VENV
                . $VENV/bin/activate
                pip install --upgrade pip
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                echo "Installing Python dependencies"
                sh '''
                . $VENV/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Dependency Scan - Trivy') {
            steps {
                echo "Running Trivy vulnerability scan"
                sh '''
                trivy fs --scanners vuln --severity HIGH,CRITICAL .
                '''
            }
        }

        stage('Static Code Scan - Bandit') {
            steps {
                echo "Running Bandit security scan"
                sh '''
                . $VENV/bin/activate
                bandit -r app/
                '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                echo "Running pytest"
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
            echo "Pipeline failed"
        }
        always {
            echo "Pipeline execution finished"
        }
    }
}

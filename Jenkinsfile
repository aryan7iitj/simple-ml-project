pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                script {
                    echo 'Checking out the repository...'
                    
                }
            }
        }
        stage('Install dependencies') {
            steps {
                script {
                    echo 'Installing dependencies...'
                   
                }
            }
        }
        stage('Run tests') {
            steps {
                script {
                    echo 'Running tests...'
                    
                }
            }
        }
        stage('Train model') {
            steps {
                script {
                    echo 'Training model...'
                    
                }
            }
        }
        stage('Deploy model') {
            steps {
                script {
                    echo 'Deploying model...'
        
                }
            }
        }
    }
    post {
        always {
            script {
                echo 'Cleaning workspace...'
                junit '**/test-*.xml'
                cleanWs()
            }
        }
    }
    options {
        timeout(time: 30, unit: 'SECONDS')  // Set a timeout for the entire pipeline
    }
}

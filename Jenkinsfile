pipeline {
    agent {
        docker { image 'python:3' }
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    echo 'Checking out the repository...'
                    git branch: 'master', url: 'https://github.com/aryan7iitj/simple-ml-project'
                }
            }
        }
        stage('Train model') {
            steps {
                script {
                    echo 'Training model...'
                    bat 'python model/train.py'
                }
            }
        }
        stage('Run tests') {
            steps {
                script {
                    echo 'Running tests...'
                    bat 'python -m unittest discover -s tests'
                }
            }
        }
        stage('Deploy model') {
            steps {
                script {
                    echo 'Deploying model...'
                    def modelFile = 'model/linear_regression_model.pkl'
                    archiveArtifacts artifacts: modelFile
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
        timeout(time: 30, unit: 'MINUTES')  // Set a timeout for the entire pipeline
    }
}

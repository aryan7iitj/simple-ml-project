pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', url: 'https://github.com/aryan7iitj/simple-ml-project'
            }
        }
        stage('Install dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run tests') {
            steps {
                sh 'python -m unittest discover -s tests'
            }
        }
        stage('Train model') {
            steps {
                sh 'python model/train.py'
            }
        }
        stage('Deploy model') {
            steps {
                script {
                    def modelFile = 'model/linear_regression_model.pkl'
                    archiveArtifacts artifacts: modelFile
                }
            }
        }
    }
    post {
        always {
            junit '**/test-*.xml'
            cleanWs()
        }
    }
}

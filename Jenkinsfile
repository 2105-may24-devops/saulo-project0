pipeline {
    agent any 
    stages {
        stage('build') {
            steps {
                sh 'echo hello world'
            }
        }
    }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
    }
}

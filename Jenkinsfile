pipeline {
    agent any 
    stages {
        stage('build') {
            steps {
                sh '''
                git clone https://github.com/2105-may24-devops/saulo-project0.git
                python3 -m pip install --upgrade pip
                python3 -m pip install --upgrade venv
                python3 -m venv venv
                . venv/bin/activate
                venv/bin/pytho3n -m pip install -r requirements.txt
                bash ./test_script.sh
                '''
            }
        }
        stage('build2') {
            steps {
                sh 'python3 --version'
                sh 'echo hello world'
            }
        }
    }
}

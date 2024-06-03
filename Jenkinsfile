pipeline {
    agent any
    stages {
        stage(Hello) {
            steps{
                echo "Hello World"
                sh '''
                 apt update
                 apt install python3
                 python3 --version
                 apt install python3-pip

                '''
            }
        }
    }
}
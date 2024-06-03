pipeline {
    agent any
    stages {
        stage(Hello) {
            steps{
                echo "Hello World"
                sh '''
                 sudo apt update
                 sudo apt install python3
                 python3 --version
                 sudo apt install python3-pip

                '''
            }
        }
    }
}
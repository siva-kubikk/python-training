pipeline {
    agent any
    stages {
        stage(Hello) {
            steps{
                echo "Hello World - Step 1.\n"
                echo "Step 2.\n"
                echo "Step 3.\n"
            }
        }
        stage(Stage2) {
            steps{
                sh '''
                echo "Cat issue file"
                cat /etc/issues
                '''
            }
        }
    }

    post {
        always {
            echo "Inside the POST - ALWAYS section"
        }
        success {
            echo "Inside the POST - SUCCESS section"
        }
        failure {
            echo "Inside the POST - FAILURE section"
        }
    }
}


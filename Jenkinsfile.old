pipeline {
    agent any

    parameters {
        string (name: 'NAME', defaultValue: 'World', description: 'The name to say hello to.')
    }

    environment {
        ENVIRONMENT = "Prod"
    }


    stages {
        stage(Hello) {
            steps{
                echo "Hello ${params.NAME}. You are in ${env.ENVIRONMENT} environment."
            }
        }
        stage(Stage2) {
            steps{
                sh '''
                echo "Cat issue file"
                cat /etc/issue
                '''
            }
        }

        stage(Parallel){
            parallel{
                stage(Stage3) {
                    steps{
                        echo "Stage 3 parallel"
                    }
                }
                stage(Stage4) {
                    steps{
                        echo "Stage 4 parallel"
                    }
                }

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


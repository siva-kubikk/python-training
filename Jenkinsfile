pipeline {
    agent any

    parameters {
        string(name: 'GREETING', defaultValue: 'Hello', description: 'Greeting to use')
        booleanParam(name: 'DEBUG_MODE', defaultValue: false, description: 'Enable debug mode')
        choice(name: 'ENVIRONMENT', choices: ['dev', 'qa', 'prod'], description: 'Deployment environment')
        password(name: 'DB_PASSWORD', defaultValue: 'password', description: 'Database password')
        file(name: 'CONFIG_FILE', description: 'Upload your configuration file')
    }


    environment{
        LOCATION = "Prod"
    }
    stages{
        stage('Hello'){
            steps{
                echo "Hello ${params.NAME}. You are in ${env.LOCATION}"
            }
        }
        stage('Display Parameters') {
            steps {
                script {
                    echo "Greeting: ${params.GREETING}"
                    echo "Debug Mode: ${params.DEBUG_MODE}"
                    echo "Environment: ${params.ENVIRONMENT}"
                    echo "DB Password: ${params.DB_PASSWORD}"
                    echo "Config File: ${params.CONFIG_FILE}"
                }
            }
        }

        stage("Parallel"){
            parallel{
                stage('p1'){
                    steps{
                        echo 'Parallel step 1'
                        sh '''
                        uptime
                        date
                        '''
                    }
                }
                stage('p2'){
                    steps{
                        echo 'Parallel step 2'
                        sh '''
                        cat /etc/issue
                        '''
                    }
                }
            }
        }
    }

    post{
    always{
        echo "Inside ALWAYS"
    }
    success{
        echo "Inside SUCCESS"
    }
    failure{
        echo "Inside FAILURE"
    }
}

}
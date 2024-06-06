pipeline {
    agent any

    parameters{
        string(name: 'NAME', defaultValue: "World", description: "Input Name")
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
}
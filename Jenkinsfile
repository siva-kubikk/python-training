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
    }
}
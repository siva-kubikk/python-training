pipeline {
    agent any

    parameters{
        string(name: NAME, defaultValue: "World", description: "Input Name")
    }
    stages{
        stage('Hello'){
            steps{
                echo "Hello {{NAME}}"
            }
        }
    }
}
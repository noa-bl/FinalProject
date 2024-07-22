pipeline {
    agent any 
    //{
 //       kubernetes {
   //         yamlFile 'jenkins/runner.yaml'
     //       defaultContainer 'builder'
       // }
    //}
    stages{
        stage("Checkout code") {
            steps {
                checkout scm
            }

        stage("Test"){
            steps{
                echo 'MAYBE last test for triggers'
                }
            }
        }
    }
}
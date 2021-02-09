pipeline {
    agent any
   
    environment {
        registry = "srinathgvelly/app_try"
        registryCredential = '1efeab5c-5037-46df-a88c-9c91774dd1c0'
        dockerImage = ''
    }
   
   
    stages {
        stage('Cloning Git') {
            steps {
                 checkout([$class: 'GitSCM', branches: [[name: '*/main']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: '8f73025a-b8ff-4efc-9a29-30214cf378cc', url: 'https://github.com/srinathgvelly/jenkins_demo.git']]])
        }
      }
        stage('Building image') {
           steps{
           script {
             docker.build registry + ":$BUILD_NUMBER"
           }
       }
    }
        stage('Upload Image to docker hub') {
          steps{    
            script {
            docker.withRegistry( '', registryCredential ) {
            dockerImage.push()
            }
        }
      }
    }
        stage('Docker Run') {
           steps{
             script {
             dockerImage.run("-p 8001:5000 --rm --name app_try")
            }
         }
      }
    }
 }

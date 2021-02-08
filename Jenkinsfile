pipeline {
    agent any
   
    environment {
        registry = "srinathgvelly/app_try"
        registryCredential = '06e5778e-fd93-4e80-840d-cc9b02f63ef0'
        dockerImage = ''
    }
   
   
    stages {
        stage('Cloning Git') {
            steps {
                 checkout([$class: 'GitSCM', branches: [[name: '*/main']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: 'e6bbe2af-357a-4a03-931b-08d77355f0c8', url: 'https://github.com/srinathgvelly/jenkins_demo.git']]])
            }
        }
        stage('Building image') {
           steps{
           script {
             docker.build registry + ":$BUILD_NUMBER"
           }
       }
     }
        stage('Upload Image') {
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

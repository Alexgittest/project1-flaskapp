
pipeline {
//    triggers {
//       GenericTrigger (causeString: 'Generic Cause', regexpFilterExpression: '', regexpFilterText: '', token: 'task4-hw47', tokenCredentialId: '')
//             }
    environment {
	  AWS_ACCESS_KEY_ID=credentials('AWS_ACCESS_KEY_ID_2')
	  AWS_SECRET_ACCESS_KEY=credentials('AWS_SECRET_ACCESS_KEY_2')
    GIT_REPO_FLASK_APP = "https://github.com/Alexgittest/project1-flaskapp.git"
    }
    tools { terraform 'terraform-14' }
    agent any
    stages {
        stage('Hello') {
            steps {
              git branch: 'main', url: "$GIT_REPO_FLASK_APP"
        }
        stage ('slack send message git checkout'){
			    steps {
				    slackSend channel: '#jenkins', message: 'Git flask app repository cloned successful'
			    }
		    }
        stage("Docker build"){
				  script {
					  docker.withRegistry('', 'dockerhub') {
						  def Myflaskapp = docker.build("alexandrkorol/flaskapp:latest")
						  Myflaskapp.push()
					  }
				  }
        }
        stage ('slack send message docker build'){
			    steps {
				    slackSend channel: '#jenkins', message: 'Docker image build completed and pushed to dockerhub'
			    }
		    }

  

        }
    }
}



 

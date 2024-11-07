pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE_OWNER = 'snicuz0588'
        DOCKER_IMAGE_TAG = 'latest'
        DOCKER_TOKEN = credentials('****토큰')
    }
    
    stages {
        stage('clone from SCM') {
            steps {
                sh '''
                rm -rf hello-msa
                git clone https://github.com/play10grounds/hello-msa.git
                '''
            }
        }
        
        stage('Docker login') {
            steps {
                script {
                    sh """
                    echo ${DOCKER_TOKEN} | docker login -u ${DOCKER_IMAGE_OWNER} --password-stdin
                    """
                }
            }
        }
        
        stage('Docker Image Building') {
            steps {
                sh '''
                cd hello-msa    
                docker build -t ${DOCKER_IMAGE_OWNER}/msa-frontend:${DOCKER_IMAGE_TAG} ./msa-frontend
                docker build -t ${DOCKER_IMAGE_OWNER}/msa-user-service:${DOCKER_IMAGE_TAG} ./msa-user-service
                docker build -t ${DOCKER_IMAGE_OWNER}/msa-product-service:${DOCKER_IMAGE_TAG} ./msa-product-service
                '''
            }
        }

        stage('Docker Push') {
            steps {
                sh '''
                docker push ${DOCKER_IMAGE_OWNER}/msa-frontend:${DOCKER_IMAGE_TAG}
                docker push ${DOCKER_IMAGE_OWNER}/msa-user-service:${DOCKER_IMAGE_TAG}
                docker push ${DOCKER_IMAGE_OWNER}/msa-product-service:${DOCKER_IMAGE_TAG}
                '''
            }
        }
        
        stage('Docker Logout') {
            steps {
                sh '''
                docker logout
                '''
            }
        }
    }
}

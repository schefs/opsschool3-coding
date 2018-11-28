pipeline {
    agent none
    stages {
        stage('Run Tests') {
            parallel {
                stage('Test On Windows') {
                    agent {
                        label "master"
                    }
                    steps {
                        echo "running windows tests"
                    }
                    post {
                        always {
                            echo "cleanning some leftovers"
                        }
                    }
                }
                stage('Test On Linux') {
                    agent {
                        label "master"
                    }
                    steps {
                        echo "running windows tests"
                    }
                    post {
                        always {
                            echo "cleanning some leftovers"
                        }
                    }
                }
            }
        }
        stage('Spinning up new ec2 salve...') {
            agent {
                label "ec2-dynamic"
            }
            steps{
                echo 'Slave is up and running !'
            }
        }
        stage('Running the real SH*T') {
            agent {
                label "ec2-dynamic"
            }
            steps('running the service') {
                sh 'pip3 install weather-api'
                sh "python3 ./home-assignments/session2/cli.py --city dublin --forecast TODAY+5 -f"
            }
        }
    }
}



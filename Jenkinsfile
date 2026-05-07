pipeline {
    agent any

    stages {

        stage('Activate Virtualenv') {
            steps {
                sh '''
                . networkvenv/bin/activate
                pip list
                '''
            }
        }

        stage('Configure VLAN') {
            steps {
                sh '''
                . networkvenv/bin/activate
                ansible-playbook -i ansible/inventory/hosts.ini ansible/playbooks/vlan_config.yml
                '''
            }
        }

        stage('Validate VLAN') {
            steps {
                sh '''
                . networkvenv/bin/activate
                pyats run job pyats/jobs/vlan_job.py
                '''
            }
        }

    }
}

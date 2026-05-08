pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git branch: 'main',
                url: 'https://github.com/harish559-lab/Network-Automation.git'
            }
        }

        stage('Create Virtual Environment') {
            steps {
                sh '''
                python3 -m venv networkvenv
                . networkvenv/bin/activate

                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        // =========================================================
        // VLAN AUTOMATION
        // =========================================================

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

        // =========================================================
        // HOSTNAME AUTOMATION
        // =========================================================

        stage('Configure Hostname') {
            steps {
                sh '''
                . networkvenv/bin/activate

                ansible-playbook -i ansible/inventory/hosts.ini ansible/playbooks/hostname_config.yml
                '''
            }
        }

        stage('Validate Hostname') {
            steps {
                sh '''
                . networkvenv/bin/activate

                pyats run job pyats/jobs/hostname_job.py
                '''
            }
        }

        // =========================================================
        // TELNET ENABLE TEST
        // =========================================================

        stage('Enable Telnet Server') {
            steps {
                sh '''
                . networkvenv/bin/activate

                ansible-playbook -i ansible/inventory/hosts.ini ansible/playbooks/telnet_enable.yml
                '''
            }
        }

        stage('Validate Telnet Enabled') {
            steps {
                sh '''
                . networkvenv/bin/activate

                pyats run job pyats/jobs/telnet_enable_job.py
                '''
            }
        }

        // =========================================================
        // TELNET DISABLE TEST
        // =========================================================

        stage('Disable Telnet Server') {
            steps {
                sh '''
                . networkvenv/bin/activate

                ansible-playbook -i ansible/inventory/hosts.ini ansible/playbooks/telnet_disable.yml
                '''
            }
        }

        stage('Validate Telnet Disabled') {
            steps {
                sh '''
                . networkvenv/bin/activate

                pyats run job pyats/jobs/telnet_disable_job.py
                '''
            }
        }
    }

    post {

        always {
            echo 'Pipeline execution completed.'
        }

        success {
            echo 'SUCCESS: All configurations and validations passed.'
        }

        failure {
            echo 'FAILURE: One or more stages failed.'
        }
    }
}

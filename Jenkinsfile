pipeline {
agent any


stages {

    stage('Clone Repository') {
        steps {
            git 'https://github.com/harish559-lab/Network-Automation.git'
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

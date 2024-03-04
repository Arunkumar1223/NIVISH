#!/bin/bash

#-T added
ssh devops_admin@nivishstaging <<EOF
/bin/bash /home/devops_admin/project/nivish-api/nivish/deployment/deploy_main.sh 
EOF

#!/bin/bash

read -p "Entrez le nom d'utilisateur : " SSHUSER
read -p "Entre l'adresse IP/hostname : " SSHHOST

ssh-keygen -f "/home/mateuw/.ssh/known_hosts" -R "${SSHHOST}"

ssh-copy-id -i ~/.ssh/id_rsa.pub ${SSHUSER}@${SSHHOST}

scp -r ~/Scripts ${SSHUSER}@${SSHHOST}:/home/${SSHUSER}  

ssh -t ${SSHUSER}@${SSHHOST} "sudo /home/${SSHUSER}/Scripts/zsh_install/zsh_install.sh"


ssh -t ${SSHUSER}@${SSHHOST} "sudo /home/${SSHUSER}/Scripts/docker_install.sh"


read -p "Entrez la nouvelle IP : " NEW_IP
read -p "Entre le nouveau nom d'hôte : " NEW_HOSTNAME
ssh -t ${SSHUSER}@${SSHHOST} "sudo 'sed -i s/192.168.20.18\/24/${NEW_IP}\/24/' /etc/netplan/00-installer-config.yaml"
ssh -t ${SSHUSER}@${SSHHOST} "sudo hostnamectl set-hostname ${NEW_HOSTNAME}"
ssh -t ${SSHUSER}@${SSHHOST} "sudo netplan apply"


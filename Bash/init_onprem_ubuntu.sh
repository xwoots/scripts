#!/bin/bash

# Add SSH Key to new host + change ip address & hostname + add host entry
# Works only for on-prem hosts with Ubuntu 18.04+

read -p "Entrez le nom d'utilisateur : " SSHUSER
read -p "Entre l'adresse IP/hostname : " SSHHOST

ssh-keygen -f "/home/mateuw/.ssh/known_hosts" -R "${SSHHOST}"

ssh-copy-id -i ~/.ssh/id_rsa.pub ${SSHUSER}@${SSHHOST}

read -p "Entrez la nouvelle IP : " NEW_IP
read -p "Entre le nouveau nom d'hôte : " NEW_HOSTNAME

ssh -t mateuw@${SSHHOST} "sudo sed -i 's/${SSHHOST}\/24/${NEW_IP}\/24/' /etc/netplan/00-installer-config.yaml \
	&& sudo hostnamectl set-hostname ${NEW_HOSTNAME} \
	&& sudo netplan apply"
	
echo ${NEW_IP} ${NEW_HOSTNAME} | sudo tee -a /etc/hosts



#!/bin/bash

read -p "Entrez l'adresse IP du template : " TEMPLATE_IP
read -p "Entrez l'adresse IP souhaitée : " NEW_IP
read -p "Entre le nouveau nom d'hôte : " NEW_HOSTNAME
ssh -t mateuw@${TEMPLATE_IP} "sudo sed -i 's/${TEMPLATE_IP}\/24/${NEW_IP}\/24/' /etc/netplan/00-installer-config.yaml"
ssh -t mateuw@${TEMPLATE_IP} "sudo hostnamectl set-hostname ${NEW_HOSTNAME}"
ssh -t mateuw@${TEMPLATE_IP} "sudo netplan apply"

#!/bin/bash

cat <<EOF
------------------------------------------------------------------------------------
                                HELLO WORLD !
                        Let's Build This K8s Cluster
------------------------------------------------------------------------------------
EOF

echo "Type your password for further further commands!"
sudo echo ""

# Retrieve servers infos
read -p 'Hostname: ' selected_hostname
read -p 'Controller IP: ' controller_ip
read -p 'Worker1 IP: ' worker1_ip
read -p 'Worker2 IP: ' worker2_ip

# Change current server Hostname 
sudo hostnamectl set-hostname $selected_hostname

# Populate Hosts file
sudo tee -a /etc/hosts <<EOF
$controller_ip  kctrl
$worker1_ip  kworker1
$worker2_ip  kworker2
EOF

# Load kernel modules and modify systems settings for containerd
cat << EOF | sudo tee /etc/modules-load.d/containerd.conf
overlay
br_netfilter
EOF

sudo modprobe overlay
sudo modprobe br_netfilter

cat <<EOF | sudo tee /etc/sysctl.d/kubernetes.conf
net.bridge.bridge-nf-call-iptables = 1
net.ipv4.ip_forward = 1
net.bridge.bridge-nf-call-ip6tables = 1
EOF

sudo sysctl --system

# Install and configure containerd
sudo apt-get update && sudo apt-get install -y containerd
sudo mkdir -p /etc/containerd
sudo containerd config default | sudo tee /etc/containerd/config.toml
sudo systemctl restart containerd

# Disable swap
sudo swapoff -a

# Install kubeadm, kubelet, and kubectl
sudo apt-get update && sudo apt-get install -y apt-transport-https curl
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -

cat << EOF | sudo tee /etc/apt/sources.list.d/kubernetes.list
deb https://apt.kubernetes.io/ kubernetes-xenial main
EOF

sudo apt-get update
sudo apt-get install -y kubelet=1.26.0-00 kubeadm=1.26.0-00 kubectl=1.26.0-00
sudo apt-mark hold kubelet kubeadm kubectl



hn=`hostname`
if [ $hn == 'kctrl' ]
then
    # Initialize the cluster and set up kubectl access
    sudo kubeadm init --pod-network-cidr 172.16.0.0/16
    
    mkdir -p $HOME/.kube
    sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
    sudo chown $(id -u):$(id -g) $HOME/.kube/config

    kubectl get nodes

    # Install the Calico network add-on.
    
    # kubectl apply -f https://raw.githubusercontent.com/projectcalico/calico/v3.26.1/manifests/calico.yaml -O

    kubectl create -f https://raw.githubusercontent.com/projectcalico/calico/v3.26.1/manifests/tigera-operator.yaml
    curl https://raw.githubusercontent.com/projectcalico/calico/v3.26.1/manifests/custom-resources.yaml -O
    kubectl create -f custom-resources.yaml
    sleep 40s
    kubectl get pods -n calico-system

    # Print the join command
    echo $'\nHere is the command for joining the cluser :'
    kubeadm token create --print-join-command
else
    echo $'\nPlease retrieve the join command from the Control-Plane Node'
    read -p "Join command: " join_command
    sudo_join_command="sudo $join_command"
    eval $sudo_join_command
fi

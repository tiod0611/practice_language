#!/usr/bin/env bash
# 위 텍스트는 스크립트 해석기로, 아 sh파일이 bash로 실행되어야 함을 나타냄

# init kubernetes
kubeadm init --token 123456.1234567890123456 --token-ttl 0 \
--pod-network-cidr=172.16.0.0/16 --apiserver-advertise-address=192.168.1.10

# config for master node only
mkdir -p $HOME/.kube
cp -i /etc/kubernetes/admin.conf $HOME/.kube/config # -i : 강제로 파일을 복사함(파일이 있어도 덮어쓰라는 말)
chown $(id -u):$(id -g) $HOME/.kube/config # 파일 소유자 변경. 파일의 소유자와 그룹을 현재 사용자로 변경


# config for kubernetes's network
kubectl apply -f \
https://raw.githubusercontent.com/sysnet4admin/IaC/master/manifests/172.16_net_calico.yaml


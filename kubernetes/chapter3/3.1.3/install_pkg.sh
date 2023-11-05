#!/usr/bin/env bash

# 시간 설정
yum -y install ntpdate
ntpdate -s ntp.postech.ac.kr && clock -w

# install packages
yum install epel-release -y # Red Hat 계열의 추가 소프트웨어 패키지 저장소
yum install vim-enhanced -y
yum install git -y

# install docker
yum install docker -y && systemctl enable --now docker # docker를 설치하고 재부팅 시에도 즉시 docker를 시작하도록 설정

# install kubernetes cluster
yum install kubectl-$1 kubelet-$1 kubeadm-$1 -y # Version 인자값을 받아서 kubectl과 kubelet, kubeadm을 설치
systemctl enable --now kubelet # 재부팅을 해도 kubelet을 항상 시작함

# git clone _Book_k8sInfra.git
if [ $2 = "Main"]; then # 해당 코드를 master node에서만 실행하기 위해 "Main" 인자를 받음.
    git clone https://github.com/sysnet4admin/_Book_k8sInfra.git
    mv /home/vagrant/_Book_k8sInfra $HOME # git에서 clone한 디렉토리를 HOME으로 이동
    find $HOME/_Book_k8sInfra/ -regex ".*\.\(sh\)" -exec chmod 700 {} \; # 해당 폴더의 sh파일을 찾아서 700 권한으로 변경. 700은 소유자에게 읽기, 쓰기, 실행을 부여하고 나머지 사용자에게는 권한을 주지 않음.
fi 


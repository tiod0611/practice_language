#!/usr/bin/env bash
# kuberadm으로 쿠버네티스를 설치하기 위한 사전 조건을 설정하는 sh 파일

# vim configuration
echo 'alias vi=vim' >> /etc/profile # alias vi=vim을 /etc/profile 에 내용 추가. vi를 입력하면 실제는 vim이 작동됨

# swapoff -a to disable swapping
swapoff -a # 모든 swap 공간을 비우고 스왑 공간을 사용하지 않음. 쿠버네티스는 설치전 swapoff를 반드시 해야함.

# sed to comment the swap partition in /etc/fstab
# sed(Stream Editor) : 텍스트 스트림에서 패턴 매칭 및 텍스트 변환을 수행함. /etc/fstab 내용을 수정
# -i.bak : -i 옵션은 'sed'를 사용해 파일을 직접 수정함. '.bak'은 수정하기 전 파일을 백업 파일로 보관한다는 의미
# -r 's/(.+ swap .+)/#\1/' : -r은 정규식을 사용. 하나씩 뜯어보자.
# s : sed에서 substitute를 의미함. 패턴에 매치되는 텍스트를 대체함.
# (.+ swap .+) : swap이라는 단어가 포함된 모든 라인을 탐색함
# #\1/ : 해당 라인의 첫번째 자리에 #를 넣음
# swap 관련 기능을 모두 주석 처리하는 명령어
sed -i.bak -r 's/(.+ swap .+)/#\1/' /etc/fstab # 시스템이 다시 시작되더라도 스왑되지 않도록 파일 자체를 변경

# kubernetes repo
gg_pkg="packages.cloud.google.com/yum/doc" # Due to shorten addr for key
cat <<EOF > /etc/yum.repos.d/kubernetes.repo # 아래 내용을 해당 파일에 작성, EOF가 나오면 작성 종료
[kubernetes]
name=Kubernetes
baseurl=https://packages.cloud.google.com/yum/repos/kubernetes-el7-x86_64
enabled=1
gpgcheck=0
gpgkey=https://${gg_pkg}/yum-key.gpg https://${gg_pkg}/rpm-package-key.gpg
EOF

# Set SELinux in permissive mode (effectively disabling it)
# setenforce는 리눅스의 보안 기능 중 하나인 SELinux의 상태를 변경하는 명령어다. 
# SELinux는 시스템의 파일, 프로세스, 포트 등에 대한 접근 권한을 제어한다.
# 0 인자는 SELinux 기능을 비활성화 하는 의미다.
setenforce 0 
# SELINUX 값을 enforcing에서 premissive로 변경
# $는 라인의 끝을 의미함. 즉 SELINUX=enforcing으로 딱 끝나는 라인을 의미.
sed -i 's/^SELINUX=enforcing$/SELINUX=permissive/' /etc/selinux/config 

# RHEL/CentOS 7 have reported traffic issues being routed incorrectly due to iptables bypassed
cat <<EOF > /etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
EOF

# modprobe는 리눅스에서 커널 모듈을 로드함.
modprobe br_netfilter # br_netfilter 모듈을 로드하여 network bridge관련 기능을 활성화함. 

# local small dns & vagrant cannot parse and delivery shell code.
echo "192.168.1.10 m-k8s" >> /etc/hosts # /etc/hosts 파일에 해당 내용을 추가

# $1의 인자를 받아서 반복문을 실행. /etc/hosts에 worker node의 ip 주소를 넣는다. 인자는 Vagrant 파일에서 N값으로 받음
for (( i=1; i<=$1; i++ )); do echo "192.168.56.10$i w$i-k8s" >> /etc/hosts; done


# config DNS
# 외부와 통신할 수 있게 DNS 서버를 지정
cat <<EOF > /etc/resolv.conf
nameserver 1.1.1.1 #cloudflare DNS
nameserver 8.8.8.8 #Google DNS
EOF


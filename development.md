# Stable Diffusion 개발 환경

## GPU를 가진 Cloud9 개발 환경  

[GPU를 사용할수 있는 Cloud9 설정](https://github.com/kyopark2014/stable-diffusion-model/blob/main/cloud9-gpu.md)에 따라 GPU를 가진 EC2를 Cloud9 개발 환경으로 준비합니다.

## GPU 설정

[NVIDIA GPU 설정](https://github.com/kyopark2014/stable-diffusion-model/blob/main/nvidia-gpu.md)에 따라 NVIDIA GPU를 쓸 수 있도록 개발 환경을 설정합니다. 

## Docker 설치

Docker 환경도 설치합니다.

```java
sudo apt-get update
sudo apt-get upgrade
```

```java
sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

```java
sudo apt-get install docker-ce docker-ce-cli containerd.io
```

## CPU 설정

속도는 느리지만 CPU로도 구현이 가능합니다. 

1) [Cloud9 Console](https://ap-northeast-2.console.aws.amazon.com/cloud9control/home?region=ap-northeast-2#/)에서 [Create environment]를 선택하여 Cloud9을 생성합니다. 

2) [Cloud9에서 EBS 크기 변경](https://github.com/kyopark2014/technical-summary/blob/main/resize.md)를 참조하여 아래처럼 크기를 변경합니다.

```java
wget https://raw.githubusercontent.com/kyopark2014/technical-summary/main/resize.sh
chmod a+rx resize.sh
./resize.sh 100
```

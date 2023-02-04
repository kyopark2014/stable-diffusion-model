# Stable Diffusion 개발 환경

## GPU를 가진 Cloud9 개발 환경  

[GPU를 사용할수 있는 Cloud9 설정](https://github.com/kyopark2014/stable-diffusion-model/blob/main/cloud9-gpu.md)에 따라 GPU를 가진 EC2를 Cloud9 개발 환경으로 준비합니다.

## GPU 설정

[NVIDIA GPU 설정](https://github.com/kyopark2014/stable-diffusion-model/blob/main/nvidia-gpu.md)에 따라 NVIDIA GPU를 쓸 수 있도록 개발 환경을 설정합니다. 

## Docker 설치

Docker 환경도 설치합니다.

```java
sudo apt-get update && upgrade
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
sudo apt-get update && upgrade
sudo apt-get install docker-ce docker-ce-cli containerd.io
```

# NVIDIA GPU 설정

[Verify You Have a CUDA-Capable GPU](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#verify-you-have-a-cuda-capable-gpu)에 따라 GPU를 확인하면 아래와 같습니다. 

```java
$ lspci | grep -i nvidia
00:1e.0 3D controller: NVIDIA Corporation GV100GL [Tesla V100 SXM2 16GB] (rev a1)
```

[Verify You Have a Supported Version of Linux](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#verify-you-have-a-supported-version-of-linux)에 따라 현재의 환경을 확인합니다.

```java
$ uname -m && cat /etc/*release
x86_64
DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=22.04
DISTRIB_CODENAME=jammy
DISTRIB_DESCRIPTION="Ubuntu 22.04.1 LTS"
PRETTY_NAME="Ubuntu 22.04.1 LTS"
NAME="Ubuntu"
VERSION_ID="22.04"
VERSION="22.04.1 LTS (Jammy Jellyfish)"
VERSION_CODENAME=jammy
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
UBUNTU_CODENAME=jammy
```

[CUDA Toolkit 12.0 Update 1 Downloads](https://developer.nvidia.com/cuda-downloads)에서 아래와 같이 선택하여 CUDA 설치를 준비합니다.

![image](https://user-images.githubusercontent.com/52392004/216669274-5bf5eac3-7980-4815-8fc5-00ea8bfab106.png)

선택된 명령어는 이용해 아래와 같이 CUDA를 설치합니다.

```java
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-ubuntu2204.pin
sudo mv cuda-ubuntu2204.pin /etc/apt/preferences.d/cuda-repository-pin-600
```

```java
wget https://developer.download.nvidia.com/compute/cuda/12.0.1/local_installers/cuda-repo-ubuntu2204-12-0-local_12.0.1-525.85.12-1_amd64.deb
sudo dpkg -i cuda-repo-ubuntu2204-12-0-local_12.0.1-525.85.12-1_amd64.deb
sudo cp /var/cuda-repo-ubuntu2204-12-0-local/cuda-*-keyring.gpg /usr/share/keyrings/
```

```java
sudo apt-get update
sudo apt-get -y install cuda
```

라이브러리를 설치합니다.

```java
pip install torch
```

정상적으로 설치되었는지 아래와 같이 확인합니다. 이때 True가 나와와 합니다. 

```java
$ python3 -c 'import torch; print(torch.cuda.is_available())'
True
```



## Troubleshooting

상기 GPU 테스트에서 False 인 경우에 아래를 추가적으로 수행합니다.

Nvidia cuda toolkit을 아래와 같이 설치합니다.

```java
sudo apt-get install nvidia-cuda-toolkit
```

아래와 같이 설치된 policy를 확인할 수 있습니다.

```java
apt-cache policy nvidia-cuda-toolkit
nvidia-cuda-toolkit:
  Installed: 11.5.1-1ubuntu1
  Candidate: 11.5.1-1ubuntu1
  Version table:
 *** 11.5.1-1ubuntu1 500
        500 http://ap-northeast-2.ec2.archive.ubuntu.com/ubuntu jammy/multiverse amd64 Packages
        100 /var/lib/dpkg/status
```        

[NVIDIA Driver Installation Quickstart Guide](https://docs.nvidia.com/datacenter/tesla/tesla-installation-notes/index.html#ubuntu-lts)을 따라 driver를 설치합니다. 

```java
sudo apt-get install linux-headers-$(uname -r)
distribution=$(. /etc/os-release;echo $ID$VERSION_ID | sed -e 's/\.//g')
wget https://developer.download.nvidia.com/compute/cuda/repos/$distribution/x86_64/cuda-keyring_1.0-1_all.deb
sudo dpkg -i cuda-keyring_1.0-1_all.deb
sudo apt-get update
sudo apt-get -y install cuda-drivers
```



# Stable Diffusion Model

## Cloud9

Cloud9 생성후 [Cloud9에서 EBS 크기 변경](https://github.com/kyopark2014/technical-summary/blob/main/resize.md)에 따라 EBS의 크기를 변경합니다. 

[Verify You Have a CUDA-Capable GPU](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#verify-you-have-a-cuda-capable-gpu)에 따라 GPU를 확인하면 아래와 같습니다. 

```java
$ lspci | grep -i nvidia
00:1e.0 3D controller: NVIDIA Corporation GV100GL [Tesla V100 SXM2 16GB] (rev a1)
```

[Verify You Have a Supported Version of Linux](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#verify-you-have-a-supported-version-of-linux)에 따라 지원여부를 확인하면 아래와 같습니다. 

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

[CUDA Toolkit 12.0 Update 1 Downloads](https://developer.nvidia.com/cuda-downloads)로 접속하여 아래와 같이 다운로드 및 설치를 합니다. 

![image](https://user-images.githubusercontent.com/52392004/216669274-5bf5eac3-7980-4815-8fc5-00ea8bfab106.png)

여기서 선택된 멸령어는 아래와 같습니다.

```java
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-ubuntu2204.pin
sudo mv cuda-ubuntu2204.pin /etc/apt/preferences.d/cuda-repository-pin-600
wget https://developer.download.nvidia.com/compute/cuda/12.0.1/local_installers/cuda-repo-ubuntu2204-12-0-local_12.0.1-525.85.12-1_amd64.deb
sudo dpkg -i cuda-repo-ubuntu2204-12-0-local_12.0.1-525.85.12-1_amd64.deb
sudo cp /var/cuda-repo-ubuntu2204-12-0-local/cuda-*-keyring.gpg /usr/share/keyrings/
sudo apt-get update
sudo apt-get -y install cuda
```

## 실행

필요한 라이브러리를 설치합니다. 

```java
pip install torch diffusers transformers
```

Stable Diffusion을 실행합니다. 

```java
cd text2image/ && python3 stable-diffusion.py
```

## Reference

[Deploy Stable Diffusion Models On Amazon SageMaker Endpoint](https://github.com/aws-samples/deploy-stable-diffusion-model-on-amazon-sagemaker-endpoint)

[Hugging Face - runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5)

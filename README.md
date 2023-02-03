# Stable Diffusion Model

Prompt Engineering으로도 불리는 Stable Diffusion은 텍스트 또는 이미지를 입력하면 인공지능(AI)가 Art Generator로서 그림을 그려줄 수 있습니다. 여기에서는 Hugging Face의 [stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5)을 Cloud9에서 구현하는것을 설명합니다. 


## Cloud9 준비 

[GPU를 사용할수 있는 Cloud9 설정](https://github.com/kyopark2014/stable-diffusion-model/blob/main/cloud9-gpu.md)에 따라 Cloud9 환경을 준비합니다.

## NVIDA GPU 설정

[NVIDA GPU 설정](https://github.com/kyopark2014/stable-diffusion-model/blob/main/nvidia-gpu.md)에 따라 GPU 환경을 설정합니다. 


## Stable Diffusion 실행

필요한 코드를 다운로드 합니다. 

```java
git clone https://github.com/kyopark2014/stable-diffusion-model
```

필요한 라이브러리를 설치합니다. 

```java
pip install torch diffusers transformers 
pip install accelerate
```

Stable Diffusion을 실행합니다. 

```java
cd text2image/ && python3 stable-diffusion.py
```

이때의 결과는 아래와 같습니다.

![astronaut_rides_horse](https://user-images.githubusercontent.com/52392004/216675578-137efd06-7c39-419d-a37b-ac3ca274f601.png)



## Reference

[Deploy Stable Diffusion Models On Amazon SageMaker Endpoint](https://github.com/aws-samples/deploy-stable-diffusion-model-on-amazon-sagemaker-endpoint)

[Hugging Face - runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5)

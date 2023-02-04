# Stable Diffusion Model

Prompt Engineering으로도 불리는 [Stable Diffusion](https://stability.ai/blog/stable-diffusion-public-release)은 텍스트 또는 이미지를 입력하면 인공지능(AI)이 Art Generator로서 그림을 그려줄 수 있습니다. 여기에서는 Hugging Face의 [stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5)을 이용하여 Stable Diffusion을 Cloud9을 이용하여 구현합니다. Hugging Face의 대부분의 모델들은 GPU를 사용하여 모델 학습(Training) 및 추론(Inference) 성능을 향상시킵니다. 따라서 개발자들이 GPU를 포함한 개발환경을 구성하여야 하는데, 성능좋은 GPU를 가진 고성능 컴퓨터를 구매하고 유지하는것은 많은 비용을 필요로 합니다. AWS의 개발환경인 Cloud9은 브라우저만으로 코드를 작성, 실행 및 디버깅할 수 있는 클라우드 기반 IDE(통합 개발 환경)로서 [AWS가 제공하는 GPU 인스턴스](https://docs.aws.amazon.com/ko_kr/dlami/latest/devguide/gpu.html)을 손쉽게 이용할 수 있습니다. 또한, 개발 프로젝트가 끝나거나, 일시적으로 사용하지 않을 경우에는 Cloud9 개발환경을 terminate나 Hibernate시켜서, 비용을 합리적으로 감소시킬 수 있습니다.


## GPU를 가진 Cloud9 개발 환경  

[GPU를 사용할수 있는 Cloud9 설정](https://github.com/kyopark2014/stable-diffusion-model/blob/main/cloud9-gpu.md)에 따라 GPU를 가진 EC2를 Cloud9 개발 환경으로 준비합니다.

## GPU 설정

[NVIDIA GPU 설정](https://github.com/kyopark2014/stable-diffusion-model/blob/main/nvidia-gpu.md)에 따라 NVIDIA GPU를 쓸 수 있도록 개발 환경을 설정합니다. 


## Stable Diffusion 실행

### Text2Image

Stable Diffusion을 실행할때 필요한 라이브러리를 설치합니다. 

```java
pip install --upgrade pip

python3 -m pip install huggingface-hub
python3 -m pip install diffusers
python3 -m pip install setuptools_rust
python3 -m pip install transformers
```

```java
pip install torch diffusers transformers 
pip install accelerate
```

[stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5)을 참조하여 [stable-diffusion.py](https://github.com/kyopark2014/stable-diffusion-model/blob/main/text2image/stable-diffusion.py)을 생성하거나 아래와 같이 다운로드합니다.

```java
git clone https://github.com/kyopark2014/stable-diffusion-model
```

[stable-diffusion.py](https://github.com/kyopark2014/stable-diffusion-model/blob/main/text2image/stable-diffusion.py)의 내용은 아래와 같습니다. 

```python
from diffusers import StableDiffusionPipeline
import torch

def main():
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print("device: "+ device)

    model_id = "runwayml/stable-diffusion-v1-5"
    pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
    pipe = pipe.to(device)

    prompt = "a photo of an astronaut riding a horse on mars"
    image = pipe(prompt).images[0]  
        
    image.save("astronaut_rides_horse.png")

if __name__ == '__main__':
    main()
```

Stable Diffusion을 실행합니다. 

```java
cd text2image/ && python3 stable-diffusion.py
```

이때의 결과는 아래와 같습니다.

![astronaut_rides_horse](https://user-images.githubusercontent.com/52392004/216675578-137efd06-7c39-419d-a37b-ac3ca274f601.png)

### Image2Image

아래의 원본이미지를 "A fantasy landscape, trending on artstation"로 변환한 결과는 아래와 같습니다.

- 원본 이미지
![sketch-mountains-input](https://user-images.githubusercontent.com/52392004/216759733-f9b362d0-7ed5-4b4f-8fe8-61f91af110aa.jpeg)

- 변환된 이미지
![fantasy_landscape](https://user-images.githubusercontent.com/52392004/216759738-05a00e84-ac2e-4af9-9352-56b57b9b8b81.png)


### In-painting

- 원본 이미지
![overture-creations-5sI6fQgYIuo](https://user-images.githubusercontent.com/52392004/216759803-cc1fc6d1-18ac-4410-bdd8-40cdd763c418.png)

- Mask 이미지
![overture-creations-5sI6fQgYIuo_mask](https://user-images.githubusercontent.com/52392004/216759809-027e9957-c3da-4772-b5d4-cf33e1fa3a40.png)

- 변환된 이미지
![in-painting](https://user-images.githubusercontent.com/52392004/216759815-206b48e5-b3ec-4e2f-aa07-4647e16aae87.png)



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
sudo apt-get install docker-ce docker-ce-cli containerd.io
```


## Reference

[Hugging Face - runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5)


[Text-to-Image generation with Stable Diffusion](https://github.com/huggingface/diffusers#text-to-image-generation-with-stable-diffusion)

[Image-to-Image text-guided generation with Stable Diffusion](https://github.com/huggingface/diffusers#image-to-image-text-guided-generation-with-stable-diffusion)

[In-painting using Stable Diffusion](https://github.com/huggingface/diffusers#in-painting-using-stable-diffusion)


[Stable Diffusion blog](https://huggingface.co/blog/stable_diffusion)

[Hugging Face - fffiloni/sd-img-variations](https://huggingface.co/spaces/fffiloni/sd-img-variations)

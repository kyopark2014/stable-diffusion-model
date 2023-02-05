# Stable Diffusion Model

Prompt Engineering으로도 불리는 [Stable Diffusion](https://stability.ai/blog/stable-diffusion-public-release)은 텍스트 또는 이미지를 입력하면 인공지능(AI)이 Art Generator로서 그림을 그려줄 수 있습니다. 여기에서는 Hugging Face의 [stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5)을 이용하여 Stable Diffusion을 Cloud9을 이용하여 구현합니다. Hugging Face의 대부분의 모델들은 GPU를 사용하여 모델 학습(Training) 및 추론(Inference) 성능을 향상시킵니다. 따라서 개발자들이 GPU를 포함한 개발환경을 구성하여야 하는데, 성능좋은 GPU를 가진 고성능 컴퓨터를 구매하고 유지하는것은 많은 비용을 필요로 합니다. AWS의 개발환경인 Cloud9은 브라우저만으로 코드를 작성, 실행 및 디버깅할 수 있는 클라우드 기반 IDE(통합 개발 환경)로서 [AWS가 제공하는 GPU 인스턴스](https://docs.aws.amazon.com/ko_kr/dlami/latest/devguide/gpu.html)을 손쉽게 이용할 수 있습니다. 또한, 개발 프로젝트가 끝나거나, 일시적으로 사용하지 않을 경우에는 Cloud9 개발환경을 terminate나 Hibernate시켜서, 비용을 합리적으로 감소시킬 수 있습니다.


## 개발 환경

[Stable Diffusion 개발환경](https://github.com/kyopark2014/stable-diffusion-model/blob/main/development.md)에서는 GPU를 가지고 있는 EC2를 Cloud9 환경으로 만드는 과정을 설명합니다. 또한 NVIDIA GPU를 위한 CUDA를 설정하고 Docker 환경도 준비합니다. 

## Stable Diffusion 실행

### Library 설치

Stable Diffusion을 실행할때 필요한 라이브러리를 설치합니다. 

```java
pip install torch diffusers transformers accelerate
```

### Text2Image

아래와 같이 실행합니다.

```java
git clone https://github.com/kyopark2014/stable-diffusion-model
python3 stable-diffusion-model/text2image/text2image.py
```

아래와 같이 100%가 되면 Cloud9에서 결과를 확인할 수 있습니다.

![noname](https://user-images.githubusercontent.com/52392004/216795219-6d46c793-6cf2-45cb-8e46-59b676f4fe2e.png)





[stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5)을 참조하여 [text2image.py](https://github.com/kyopark2014/stable-diffusion-model/blob/main/text2image/text2image.py)에서는 "a photo of an astronaut riding a horse on mars"을 이용하여 아래와 같은 이미지를 생성합니다. 

![astronaut_rides_horse](https://user-images.githubusercontent.com/52392004/216675578-137efd06-7c39-419d-a37b-ac3ca274f601.png)

### Image2Image

아래와 같이 실행합니다.

```java
git clone https://github.com/kyopark2014/stable-diffusion-model
python3 stable-diffusion-model/image2image/image2image.py 
```

[image2image.py](https://github.com/kyopark2014/stable-diffusion-model/blob/main/image2image/image2image.py)을 이용하여 원본 이미지를 "A fantasy landscape, trending on artstation"로 변환한 결과는 아래와 같습니다.

- 원본 이미지

<img src="https://user-images.githubusercontent.com/52392004/216759733-f9b362d0-7ed5-4b4f-8fe8-61f91af110aa.jpeg" width="600">



- 변환된 이미지

<img src="https://user-images.githubusercontent.com/52392004/216759738-05a00e84-ac2e-4af9-9352-56b57b9b8b81.png" width="600">



### In-painting

아래와 같이 실행합니다.

```java
git clone https://github.com/kyopark2014/stable-diffusion-model
python3 stable-diffusion-model/in-painting/in-painting.py
```

[in-painting.py](https://github.com/kyopark2014/stable-diffusion-model/blob/main/in-painting/in-painting.py)을 이용하여 mask된 영역을 제거하고 "Face of a yellow cat, high resolution, sitting on a park bench"로 변환한 결과는 아래와 같습니다. 

- 원본 이미지

<img src="https://user-images.githubusercontent.com/52392004/216759803-cc1fc6d1-18ac-4410-bdd8-40cdd763c418.png" width="600">

- Mask 이미지

<img src="https://user-images.githubusercontent.com/52392004/216759809-027e9957-c3da-4772-b5d4-cf33e1fa3a40.png" width="600">


- 변환된 이미지

<img src="https://user-images.githubusercontent.com/52392004/216759815-206b48e5-b3ec-4e2f-aa07-4647e16aae87.png" width="600">




## Reference

[Hugging Face - runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5)


[Text-to-Image generation with Stable Diffusion](https://github.com/huggingface/diffusers#text-to-image-generation-with-stable-diffusion)

[Image-to-Image text-guided generation with Stable Diffusion](https://github.com/huggingface/diffusers#image-to-image-text-guided-generation-with-stable-diffusion)

[In-painting using Stable Diffusion](https://github.com/huggingface/diffusers#in-painting-using-stable-diffusion)


[Stable Diffusion blog](https://huggingface.co/blog/stable_diffusion)

[Hugging Face - fffiloni/sd-img-variations](https://huggingface.co/spaces/fffiloni/sd-img-variations)

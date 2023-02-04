import requests
import torch
from PIL import Image
from io import BytesIO

from diffusers import StableDiffusionPipeline

def imageToimage(device):
    model_id = "runwayml/stable-diffusion-v1-5"

    if device == "cuda":
        pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
    else:
        pipe = StableDiffusionPipeline.from_pretrained(model_id)    

    # or download via git clone https://huggingface.co/runwayml/stable-diffusion-v1-5
    # and pass `model_id="./stable-diffusion-v1-5"`.
    pipe = pipe.to(device)

    # let's download an initial image
    url = "https://raw.githubusercontent.com/CompVis/stable-diffusion/main/assets/stable-samples/img2img/sketch-mountains-input.jpg"

    response = requests.get(url)
    init_image = Image.open(BytesIO(response.content)).convert("RGB")
    init_image = init_image.resize((768, 512))

    prompt = "A fantasy landscape, trending on artstation"

    images = pipe(prompt=prompt, image=init_image, strength=0.75, guidance_scale=7.5).images

    images[0].save("fantasy_landscape.png")


def main():
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print("device: "+ device)

    imageToimage(device)

if __name__ == '__main__':
    main()
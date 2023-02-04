import requests
import torch
from PIL import Image
from io import BytesIO
from diffusers import StableDiffusionImg2ImgPipeline

def imageToimage(device):
    model_id = "runwayml/stable-diffusion-v1-5"

    # load the pipeline
    if device == "cuda":
        pipe = StableDiffusionImg2ImgPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
    else:
        pipe = StableDiffusionImg2ImgPipeline.from_pretrained(model_id)    

    pipe = pipe.to(device)

    # from url
    url = "https://raw.githubusercontent.com/CompVis/stable-diffusion/main/assets/stable-samples/img2img/sketch-mountains-input.jpg"
    prompt = "A fantasy landscape, trending on artstation"

    response = requests.get(url)
    init_image = Image.open(BytesIO(response.content)).convert("RGB")
    init_image = init_image.resize((768, 512))
   
    images = pipe(prompt=prompt, image=init_image, strength=0.75, guidance_scale=7.5).images

    images[0].save("fantasy_landscape.png")

def main():
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print("device: "+ device)

    imageToimage(device)

if __name__ == '__main__':
    main()
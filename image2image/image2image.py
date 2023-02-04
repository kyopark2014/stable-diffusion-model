import requests
import torch
from PIL import Image
from io import BytesIO
from diffusers import StableDiffusionImg2ImgPipeline

from cv2 import imread
from numpy import load
import os
from logging import INFO, StreamHandler, getLogger
logger = getLogger()
logger.setLevel(INFO)

def load_image(image_path):
    # Case insenstive check of the image type.
    img_lower = image_path.lower()
    if (
        img_lower.endswith(
            ".jpg",
            -4,
        )
        or img_lower.endswith(
            ".png",
            -4,
        )
        or img_lower.endswith(
            ".jpeg",
            -5,
        )
    ):
        try:
            image_data = imread(image_path)
        except Exception as e:
            logger.error(
                "Unable to read the image at: {}. Error: {}".format(image_path, e)
            )
            exit(1)
    elif img_lower.endswith(
        ".npy",
        -4,
    ):
        image_data = load(image_path)
    else:
        logger.error("Images of format jpg,jpeg,png and npy are only supported.")
        exit(1)
    return image_data

def imageToimage(device):
    model_id = "runwayml/stable-diffusion-v1-5"

    # load the pipeline
    if device == "cuda":
        pipe = StableDiffusionImg2ImgPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
    else:
        pipe = StableDiffusionImg2ImgPipeline.from_pretrained(model_id)    

    pipe = pipe.to(device)

    # from url
    #url = "https://raw.githubusercontent.com/CompVis/stable-diffusion/main/assets/stable-samples/img2img/sketch-mountains-input.jpg"
    #prompt = "A fantasy landscape, trending on artstation"

    #response = requests.get(url)
    #init_image = Image.open(BytesIO(response.content)).convert("RGB")
    #init_image = init_image.resize((768, 512))


    # from local
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))  
    print('BASE_DIR = ', BASE_DIR)
    fname = "pelican.jpeg"
    prompt = "A fantasy landscape, trending on artstation"
    init_image = load_image(os.path.join(BASE_DIR, fname)).convert("RGB")
    init_image = init_image.resize((768, 512))
    
    
    #url = "pelican.jpeg"
    #prompt = "A fantasy landscape, trending on artstation"
    #response = requests.get(url)
    #init_image = Image.open(BytesIO(response.content)).convert("RGB")
    #init_image = init_image.resize((768, 512))

    images = pipe(prompt=prompt, image=init_image, strength=0.75, guidance_scale=7.5).images

    images[0].save("fantasy_landscape.png")

def main():
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print("device: "+ device)

    imageToimage(device)

if __name__ == '__main__':
    main()
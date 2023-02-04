import PIL
import requests
import torch
from io import BytesIO

from diffusers import StableDiffusionInpaintPipeline

def download_image(url):
    response = requests.get(url)
    return PIL.Image.open(BytesIO(response.content)).convert("RGB")

def inPainting(device):
    img_url = "https://raw.githubusercontent.com/CompVis/latent-diffusion/main/data/inpainting_examples/overture-creations-5sI6fQgYIuo.png"
    mask_url = "https://raw.githubusercontent.com/CompVis/latent-diffusion/main/data/inpainting_examples/overture-creations-5sI6fQgYIuo_mask.png"

    init_image = download_image(img_url).resize((512, 512))
    mask_image = download_image(mask_url).resize((512, 512))

    #pipe = StableDiffusionInpaintPipeline.from_pretrained("runwayml/stable-diffusion-inpainting", torch_dtype=torch.float16)
    if device == "cuda":
        pipe = StableDiffusionInpaintPipeline.from_pretrained("runwayml/stable-diffusion-inpainting", torch_dtype=torch.float16)
    else:
        pipe = StableDiffusionInpaintPipeline.from_pretrained("runwayml/stable-diffusion-inpainting")

    pipe = pipe.to("cuda")

    prompt = "Face of a yellow cat, high resolution, sitting on a park bench"
    images = pipe(prompt=prompt, image=init_image, mask_image=mask_image).images

    images[0].save("in-painting.png")

def main():
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print("device: "+ device)

    inPainting(device)

if __name__ == '__main__':
    main()    
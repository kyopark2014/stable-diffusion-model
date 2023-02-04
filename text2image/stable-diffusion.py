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
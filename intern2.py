


from diffusers import StableDiffusionPipeline
import torch
import matplotlib.pyplot as plt
device = "cuda" if torch.cuda.is_available() else "cpu"


# Load the pipeline
pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16
)
pipe = pipe.to(device)  # Move to GPU

# Your custom prompt
prompt = input("Enter your prompt: ")

# Generate image
image = pipe(prompt).images[0]

# Save (optional)
image.save("output.png")

# Display using matplotlib
plt.imshow(image)
plt.axis("off")
plt.title("Your image")
plt.show()

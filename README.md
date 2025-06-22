# PRODIGY_GA_02
# Stable Diffusion Text-to-Image Generator (Internship Task)

This script generates high-quality images from a text prompt using the **Stable Diffusion v1.5 model** via Hugging Face's `diffusers` library. It's designed to run locally as a standalone Python script on systems with a CUDA-enabled GPU.

---

## 🚀 Features

- Accepts user-defined prompts via command line
- Generates one image using Stable Diffusion v1.5
- Saves the output as `output.png`
- Displays the image using `matplotlib`
- Optimized for GPU usage (`torch.float16` on CUDA)

---

## 📦 Required Packages

Install the following Python libraries before running the script:

```bash
pip install diffusers transformers accelerate torch torchvision matplotlib

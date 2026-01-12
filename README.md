# Text-to-Image Generation with Hugging Face

This project contains code for text-to-image generation using Hugging Face models.

## Files

- **main.py** - Main script for text-to-image generation using Stable Diffusion
- **list_hf_models.py** - Script to list and check Hugging Face models
- **hf_models_list.txt** - Generated text file with model information
- **requirements.txt** - Python dependencies

## Fixed Issues

1. ✅ Fixed typo: `tranformers` → `transformers`
2. ✅ Changed from summarization to text-to-image generation
3. ✅ Added proper CUDA detection and device selection
4. ✅ Added error handling for missing dependencies

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. For CUDA support, install PyTorch with CUDA:
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

## Usage

### Generate Images
```bash
python main.py
```

This will:
- Check CUDA availability
- Load the Stable Diffusion model
- Generate an image from a text prompt
- Save the image as `generated_image.png`

### List Hugging Face Models
```bash
python list_hf_models.py
```

This will:
- List popular text-to-image models
- Show model information (downloads, pipeline, library)
- Save results to `hf_models_list.txt`

## Models Available

The script checks these popular models:
- `runwayml/stable-diffusion-v1-5` (1.5M+ downloads)
- `stabilityai/stable-diffusion-xl-base-1.0` (1.7M+ downloads)
- `CompVis/stable-diffusion-v1-4` (396K+ downloads)
- `runwayml/stable-diffusion-inpainting` (144K+ downloads)

## Notes

- First run will download the model (~4GB), so ensure you have:
  - Sufficient disk space
  - Stable internet connection
  - Valid Hugging Face token (if required)

- For authentication issues, set your token:
```bash
.\set_token.ps1 YOUR_TOKEN_HERE
```

- GPU is recommended but not required (CPU will work, just slower)

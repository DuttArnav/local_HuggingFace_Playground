"""
Text-to-Image Generation using Hugging Face Models
"""

try:
    import torch
    print("[OK] PyTorch imported successfully")
except ImportError:
    print("[ERROR] PyTorch not installed. Install with: pip install torch torchvision torchaudio")
    exit(1)

try:
    from diffusers import StableDiffusionPipeline
    print("[OK] Diffusers imported successfully")
except ImportError:
    print("[ERROR] Diffusers not installed. Install with: pip install diffusers")
    exit(1)

# Check CUDA availability
print("\n" + "="*60)
print("CUDA CHECK")
print("="*60)
print("CUDA Available:", torch.cuda.is_available())
if torch.cuda.is_available():
    print("CUDA Device:", torch.cuda.get_device_name(0))
    print("CUDA Version:", torch.version.cuda)
    print("GPU Memory:", f"{torch.cuda.get_device_properties(0).total_memory / 1024**3:.2f} GB")
    device = "cuda"
    torch_dtype = torch.float16  # Use half precision for faster inference
else:
    print("Using CPU")
    device = "cpu"
    torch_dtype = torch.float32

# Text-to-Image Generation Model
print("\n" + "="*60)
print("LOADING TEXT-TO-IMAGE MODEL")
print("="*60)
print("Model: runwayml/stable-diffusion-v1-5")
print("This may take a few minutes on first run...")

try:
    # Using Stable Diffusion model for text-to-image generation
    pipe = StableDiffusionPipeline.from_pretrained(
        "runwayml/stable-diffusion-v1-5",
        torch_dtype=torch_dtype
    )
    pipe = pipe.to(device)
    print("[OK] Model loaded successfully!")
    
    # Generate image from text
    prompt = "a beautiful sunset over mountains, digital art, highly detailed"
    print(f"\nGenerating image for prompt: '{prompt}'")
    print("This may take 30-60 seconds...")
    
    image = pipe(prompt).images[0]
    
    # Save the image
    output_file = "generated_image.png"
    image.save(output_file)
    print(f"\n[OK] Image saved as '{output_file}'")
    
except Exception as e:
    print(f"\n[ERROR] Error: {e}")
    print("\nTroubleshooting:")
    print("1. Make sure you have enough disk space (model is ~4GB)")
    print("2. Check your internet connection (model will be downloaded)")
    print("3. If using GPU, ensure CUDA is properly installed")
    print("4. Try: pip install diffusers transformers accelerate")
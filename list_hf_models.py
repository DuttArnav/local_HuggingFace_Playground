"""
Script to list and check Hugging Face models
Run this to see available models and their status
"""

from huggingface_hub import list_models, HfApi
import json
from datetime import datetime

def list_popular_models():
    """List popular text-to-image models on Hugging Face"""
    print("=" * 80)
    print("POPULAR TEXT-TO-IMAGE MODELS ON HUGGING FACE")
    print("=" * 80)
    
    api = HfApi()
    
    # Popular text-to-image models
    popular_models = [
        "runwayml/stable-diffusion-v1-5",
        "stabilityai/stable-diffusion-2-1",
        "CompVis/stable-diffusion-v1-4",
        "stabilityai/stable-diffusion-xl-base-1.0",
        "runwayml/stable-diffusion-inpainting",
    ]
    
    results = []
    
    for model_id in popular_models:
        try:
            model_info = api.model_info(model_id)
            results.append({
                "model_id": model_id,
                "author": model_info.author,
                "downloads": model_info.downloads if hasattr(model_info, 'downloads') else "N/A",
                "tags": model_info.tags if hasattr(model_info, 'tags') else [],
                "pipeline_tag": model_info.pipeline_tag if hasattr(model_info, 'pipeline_tag') else "N/A",
                "library_name": model_info.library_name if hasattr(model_info, 'library_name') else "N/A",
            })
            print(f"\n[OK] {model_id}")
            print(f"  Pipeline: {model_info.pipeline_tag if hasattr(model_info, 'pipeline_tag') else 'N/A'}")
            print(f"  Library: {model_info.library_name if hasattr(model_info, 'library_name') else 'N/A'}")
            if hasattr(model_info, 'downloads'):
                print(f"  Downloads: {model_info.downloads:,}")
        except Exception as e:
            print(f"\n[ERROR] {model_id} - Error: {e}")
            results.append({
                "model_id": model_id,
                "error": str(e)
            })
    
    # Save to file
    output_file = "hf_models_list.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("=" * 80 + "\n")
        f.write("HUGGING FACE TEXT-TO-IMAGE MODELS\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 80 + "\n\n")
        
        for result in results:
            f.write(f"Model: {result['model_id']}\n")
            if 'error' in result:
                f.write(f"  Error: {result['error']}\n")
            else:
                f.write(f"  Author: {result['author']}\n")
                f.write(f"  Pipeline: {result['pipeline_tag']}\n")
                f.write(f"  Library: {result['library_name']}\n")
                f.write(f"  Downloads: {result['downloads']}\n")
                if result['tags']:
                    f.write(f"  Tags: {', '.join(result['tags'])}\n")
            f.write("\n")
    
    print(f"\n{'=' * 80}")
    print(f"Results saved to: {output_file}")
    print("=" * 80)
    
    return results

def search_models_by_task(task="text-to-image", limit=10):
    """Search for models by task"""
    print(f"\n{'=' * 80}")
    print(f"SEARCHING FOR {task.upper()} MODELS (Top {limit})")
    print("=" * 80)
    
    try:
        models = list_models(
            sort="downloads",
            limit=limit
        )
        
        # Filter by pipeline tag
        results = []
        count = 0
        for model in models:
            if hasattr(model, 'pipeline_tag') and model.pipeline_tag == task:
                print(f"\n{model.id}")
                print(f"  Downloads: {model.downloads:,}")
                print(f"  Author: {model.author}")
                results.append({
                    "model_id": model.id,
                    "downloads": model.downloads,
                    "author": model.author
                })
                count += 1
                if count >= limit:
                    break
        
        if count == 0:
            print(f"\nNo models found with pipeline_tag='{task}'")
            print("Showing top downloaded models instead:")
            for i, model in enumerate(list(models)[:limit]):
                print(f"\n{model.id}")
                print(f"  Downloads: {model.downloads:,}")
                print(f"  Pipeline: {getattr(model, 'pipeline_tag', 'N/A')}")
        
    except Exception as e:
        print(f"Error searching models: {e}")
        results = []
    
    return results

if __name__ == "__main__":
    try:
        # List popular models
        popular = list_popular_models()
        
        # Search for more text-to-image models
        print("\n")
        search_results = search_models_by_task("text-to-image", limit=5)
        
    except Exception as e:
        print(f"Error: {e}")
        print("Make sure you have huggingface_hub installed: pip install huggingface_hub")

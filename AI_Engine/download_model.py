import argparse
from pathlib import Path
from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL_NAME = "TheBloke/wizardLM-7B-1.0-SuperHOT-8K"  # CPU-capable model if torch supports it


def download_model(model_name: str, output_dir: Path):
    output_dir.mkdir(parents=True, exist_ok=True)
    print(f"Downloading model {model_name} into {output_dir}")
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name, trust_remote_code=True)
    tokenizer.save_pretrained(output_dir)
    model.save_pretrained(output_dir)
    print("Download complete.")


def main() -> int:
    parser = argparse.ArgumentParser(description="Download a local Transformers model for AI_Engine")
    parser.add_argument("--model", type=str, default=MODEL_NAME, help="Hugging Face model name")
    parser.add_argument("--output", type=str, default="AI_Engine/model", help="Local output directory")
    args = parser.parse_args()

    download_model(args.model, Path(args.output))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

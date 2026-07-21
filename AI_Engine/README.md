# DevOps AI Learning Agent

A local terminal-based DevOps tutor built to help you learn Linux, Git, CI/CD, Docker, Kubernetes, cloud fundamentals, and interview preparation.

## Setup

1. Ensure you have Python 3.10+ installed.
2. Install dependencies:

```bash
python -m pip install --upgrade pip setuptools wheel
python -m pip install -r AI_Engine/requirements.txt
```

3. Download or acquire a local transformers-compatible model directory.
   - Example: download a local Hugging Face-style text-generation model into `AI_Engine/model/`.
   - Optionally set the environment variable `DEVOPS_AGENT_MODEL` to the model directory path.

## Running the agent

```bash
python AI_Engine/agent.py
```

Or with explicit model path:

```bash
python AI_Engine/agent.py --model AI_Engine/model.bin
```

## Commands

- `/help` - show help text.
- `/topics` - show core DevOps topics.
- `/plan` - show a sample study plan.
- `/exit` - quit the agent.

## Notes

- If no local model is available, the agent will still run in fallback mode with curated DevOps guidance.
- For best results, use a local open-source model and set `DEVOPS_AGENT_MODEL`.

## Next steps

- Add local markdown-based note retrieval.
- Add a simple web frontend.
- Enhance the prompt with your personal learning goals.

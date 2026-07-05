import argparse
import os
import sys
import textwrap
from pathlib import Path

SYSTEM_PROMPT = """You are a helpful DevOps learning assistant. Answer questions clearly, concisely, and with practical next steps. Focus on Linux, Git, CI/CD, Docker, Kubernetes, cloud fundamentals, scripting, and interview preparation. If the user asks for commands, include examples and explain what the commands do."""

CORE_TOPICS = [
    "Linux shell and commands",
    "Git version control",
    "CI/CD pipelines",
    "Docker containerization",
    "Kubernetes orchestration",
    "Infrastructure as Code",
    "Cloud service basics",
    "Monitoring and logging",
    "Security and access control",
    "DevOps interview preparation",
]

FALLBACK_GUIDANCE = {
    "docker": "Docker is a containerization platform. Start by learning how to build images with Dockerfiles, run containers using `docker run`, and manage volumes and networking. A good first step is `docker build -t myapp .` and then `docker run --rm -it myapp`.",
    "kubernetes": "Kubernetes manages containerized applications across clusters. Learn core concepts like Pods, Deployments, Services, and ConfigMaps. Start with `kubectl apply -f deployment.yaml` and `kubectl get pods`.",
    "git": "Git is version control. Use `git init` to create a repository, `git add .`, `git commit -m 'message'`, and `git push` to update remote branches. Focus on branching, merging, and resolving conflicts.",
    "ci/cd": "CI/CD automates build, test, and deploy workflows. Learn pipeline tools like GitHub Actions, GitLab CI, or Azure Pipelines. Start with a simple YAML file that checks out code, installs dependencies, and runs tests.",
    "linux": "Linux is essential for DevOps. Practice basic commands like `ls`, `cd`, `chmod`, `chown`, `grep`, `awk`, and `sed`. Also learn process management with `ps`, `top`, and `systemctl`.",
}

KUBERNETES_POD_YAML = """apiVersion: v1
kind: Pod
metadata:
  name: basic-pod
spec:
  containers:
    - name: nginx
      image: nginx:latest
      ports:
        - containerPort: 80
"""


def load_local_model(model_path: Path):
    model_path = model_path.expanduser().resolve()
    print(f"DEBUG: loading model from {model_path}")
    if not model_path.exists():
        print("DEBUG: model path does not exist")
        return None, None

    try:
        from transformers import pipeline

        generator_kwargs = {"model": str(model_path)}

        try:
            import accelerate
            use_accelerate = True
        except ImportError:
            use_accelerate = False

        try:
            import torch
            cuda_available = torch.cuda.is_available()
        except Exception:
            cuda_available = False

        if use_accelerate and cuda_available:
            generator_kwargs["device_map"] = "auto"
            generator_kwargs["torch_dtype"] = "auto"
        else:
            generator_kwargs["device"] = -1

        print(f"DEBUG: generator kwargs {generator_kwargs}")
        generator = pipeline("text-generation", **generator_kwargs)
        print("DEBUG: model pipeline created")
        return "transformers", generator
    except Exception as exc:
        print("DEBUG: model load exception:", type(exc).__name__, exc)
        return None, None


def fallback_response(user_text: str) -> str:
    lowered = user_text.lower()
    if "pod" in lowered and "yaml" in lowered:
        return (
            "Here is a simple Kubernetes Pod YAML file:\n\n"
            f"{KUBERNETES_POD_YAML}\n"
            "Apply it with `kubectl apply -f pod.yaml`."
        )
    for key, guidance in FALLBACK_GUIDANCE.items():
        if key in lowered:
            return guidance
    return (
        "I am running in fallback mode and can help with general DevOps study guidance. "
        "Ask me about Docker, Kubernetes, Git, CI/CD, Linux, or interview preparation. "
        "For better results, install a local model and set DEVOPS_AGENT_MODEL."
    )


def is_blank_or_bad_output(text: str, prompt_text: str) -> bool:
    stripped = text.strip()
    if not stripped:
        return True
    if stripped == prompt_text.strip():
        return True
    if len(stripped) < 10:
        return True
    if stripped.replace('\n', '').strip() == '':
        return True
    return False


def format_plan() -> str:
    return textwrap.dedent(
        """
        Sample DevOps Study Plan:

        1. Linux fundamentals: shell commands, file permissions, processes, and networking.
        2. Git workflow: commits, branches, merge conflicts, and remote collaboration.
        3. Docker basics: images, containers, Dockerfiles, volumes, and networking.
        4. CI/CD: build/test automation, pipeline YAML, and deployment strategies.
        5. Kubernetes: pods, deployments, services, config maps, and rolling updates.
        6. Cloud basics: compute, storage, networking, and IAM on your chosen cloud provider.
        7. Monitoring and security: logging, alerts, secrets, and access control.

        Practice with real projects and interview-style questions each week.
        """
    ).strip()


def print_welcome():
    print("\n=== DevOps AI Learning Agent ===\n")
    print("Commands: /help, /topics, /plan, /exit")
    print("Set DEVOPS_AGENT_MODEL or use --model to load a local transformers-compatible model directory.")
    print("If no local model is available, the agent will run in fallback guidance mode.\n")


def print_help():
    print(textwrap.dedent(
        """
        Available commands:
        /help   - show this help text
        /topics - show core DevOps topics
        /plan   - show a sample study plan
        /exit   - exit the agent
        """
    ))


def print_topics():
    print("Core DevOps topics:")
    for topic in CORE_TOPICS:
        print(f"- {topic}")


def prompt_agent(model_type, agent, prompt_text: str) -> str:
    if model_type == "transformers":
        outputs = agent(
            prompt_text,
            max_new_tokens=300,
            do_sample=True,
            temperature=0.7,
            top_p=0.9,
            return_full_text=False,
        )
        answer = outputs[0]["generated_text"].strip()
        if is_blank_or_bad_output(answer, prompt_text):
            return fallback_response(prompt_text)
        return answer

    return fallback_response(prompt_text)


def main() -> int:
    parser = argparse.ArgumentParser(description="Local DevOps AI agent")
    parser.add_argument("--model", "-m", type=str, help="Path to a local model file or model directory")
    args = parser.parse_args()

    model_path = args.model or os.environ.get("DEVOPS_AGENT_MODEL") or "AI_Engine/model.bin"
    print(f"DEBUG: using python executable {sys.executable}")
    print(f"DEBUG: resolved model path {model_path}")
    model_type, model = load_local_model(Path(model_path))

    if model_type:
        print(f"Loaded local model from: {model_path} ({model_type})")
    else:
        print("No usable local model loaded. Running in fallback guidance mode.")

    print_welcome()
    print_help()

    while True:
        try:
            user_input = input("\nYou: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nExiting.")
            return 0

        if not user_input:
            continue

        if user_input.lower() in {"/exit", "exit", "quit", ":q"}:
            print("Good luck with your DevOps learning!")
            return 0
        if user_input.lower() in {"/help", "help"}:
            print_help()
            continue
        if user_input.lower() in {"/topics", "topics"}:
            print_topics()
            continue
        if user_input.lower() in {"/plan", "plan"}:
            print(format_plan())
            continue

        answer = prompt_agent(model_type, model, user_input)
        print(f"\nAgent:\n{answer}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

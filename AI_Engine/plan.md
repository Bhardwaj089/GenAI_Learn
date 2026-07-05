## AI Engine Plan

This folder contains a local DevOps learning agent that helps you study, practice, and prepare for DevOps interviews.

### Goals
- Build a local Python-based AI assistant.
- Use an open-source local model runtime if available.
- Provide DevOps study guidance on Linux, Git, CI/CD, Docker, Kubernetes, cloud fundamentals, and interview prep.
- Keep the experience simple and terminal-based to start.

### Project files
- `agent.py` - main local agent implementation.
- `requirements.txt` - Python dependencies for the agent.
- `README.md` - setup and usage instructions.

### Implementation steps
1. Install dependencies from `requirements.txt`.
2. Download or provide a local LLM model file, then set `DEVOPS_AGENT_MODEL` or pass `--model`.
3. Run `python agent.py` and enter DevOps questions in the terminal.
4. Use commands like `/help`, `/topics`, `/plan`, and `/exit`.

### Success criteria
- The agent starts locally from `AI_Engine`.
- It accepts DevOps questions and returns meaningful guidance.
- It gracefully handles missing model libraries and provides a fallback learning assistant.

### Next improvements
- Add a local knowledge base of DevOps notes and lab exercises.
- Add file-based retrieval from markdown content.
- Add a GUI or web interface later if needed.

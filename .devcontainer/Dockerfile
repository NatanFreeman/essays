# syntax=docker/dockerfile:1
FROM mcr.microsoft.com/devcontainers/base:ubuntu

# 1. Install system dependencies
RUN apt-get update && apt-get install -y \
    python3 python3-pip curl git postgresql postgresql-contrib hugo \
    && rm -rf /var/lib/apt/lists/*

# 2. NOW switch to the vscode user for user-specific tools
USER vscode
ENV HOME=/home/vscode

# 3. Install 'uv' and 'mistral-vibe' as the vscode user
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/home/vscode/.local/bin:${PATH}"

RUN uv tool install mistral-vibe

# 4. Set up the Vibe configuration
RUN mkdir -p /home/vscode/.vibe
RUN cat <<EOF > /home/vscode/.vibe/config.toml
active_model = "kimi-openrouter"

[[providers]]
name = "openrouter"
api_base = "https://openrouter.ai/api/v1"
api_key_env_var = "OPENROUTER_API_KEY"
api_style = "openai"
backend = "generic"

[[models]]
name = "moonshotai/kimi-k2.5"
provider = "openrouter"
alias = "kimi-openrouter"
EOF

# Ensure the PATH is persisted for the shell
RUN echo 'export PATH="/home/vscode/.local/bin:$PATH"' >> /home/vscode/.bashrc
FROM ghcr.io/astral-sh/uv:latest
LABEL org.opencontainers.image.title="Climate Town Discord Bot"
LABEL org.opencontainers.image.description="Discord Bot used within the Climate Town Discord server."
LABEL org.opencontainers.image.source="https://github.com/ClimateTown/discord-bot"

WORKDIR /code

# Copy only dependency file first for better build caching
COPY uv.lock ./
RUN uv venv

COPY . .

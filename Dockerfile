FROM python:3.10
LABEL org.opencontainers.image.title="Climate Town Discord Bot"
LABEL org.opencontainers.image.description="Discord Bot used within the Climate Town Discord server."
LABEL org.opencontainers.image.source="https://github.com/ClimateTown/discord-bot"

WORKDIR /code

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

FROM python:3.10-slim

ENV JUPYTER_PLATFORM_DIRS=1 \
    NO_MKDOCS_2_WARNING=true \
    PIP_NO_CACHE_DIR=1

RUN apt-get update \
    && apt-get install -y --no-install-recommends git curl ca-certificates \
    && curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y --no-install-recommends nodejs \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY package.json package-lock.json ./
RUN npm ci

COPY . .

EXPOSE 8000

CMD ["mkdocs", "serve", "-a", "0.0.0.0:8000"]

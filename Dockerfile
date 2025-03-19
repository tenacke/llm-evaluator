FROM ubuntu:latest AS builder

ARG GIT_TOKEN
RUN apt-get update && apt-get install -y git

RUN git clone https://$GIT_TOKEN@github.com/tenacke/llm-evaluator.git /opt/evallm
RUN rm -rf /opt/evallm/.git

FROM ollama/ollama

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends \
        git \
        wget \
        cmake \
        ninja-build \
        build-essential \
        python3.12 \
        python3-dev \
        python3-pip \
        python3-venv \
        python-is-python3 \
    && apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/* 

WORKDIR /opt/evallm
COPY --from=builder /opt/evallm /opt/evallm

RUN python3 -m pip install --upgrade pip && \
    python3 -m venv venv

RUN venv/bin/pip install --no-cache-dir -r requirements.txt

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

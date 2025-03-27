FROM python:3.12

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends git \
    && apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/* 

RUN git clone --branch --single-branch https://github.com/tenacke/llm-evaluator.git /opt/llm-evaluator

WORKDIR /opt/llm-evaluator

RUN python3 -m pip install --upgrade pip && \
    python3 -m venv venv

COPY requirements.txt ./
RUN venv/bin/pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

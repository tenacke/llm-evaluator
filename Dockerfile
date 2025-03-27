FROM python:3.12

WORKDIR /opt/llm-evaluator

RUN python3 -m pip install --upgrade pip && \
    python3 -m venv venv

COPY requirements.txt ./
RUN venv/bin/pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

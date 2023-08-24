FROM python:3.9

RUN apt-get update && \
    apt-get install -y git && \
    rm -rf /var/lib/apt/lists/*

CMD ["python3"]

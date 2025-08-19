FROM docker.io/pytorch/pytorch:2.3.0-cuda12.1-cudnn8-runtime

RUN apt-get update && apt-get install -y \
    libsndfile1 \
    && rm -rf /var/lib/apt/lists/*

ENV CUDA_HOME=/usr/local/cuda

# Install Python dependencies in a single layer
RUN pip install gradio xformers stable_audio_tools

WORKDIR /app
COPY hello-gradio.py /app

CMD ["python", "hello-gradio.py"]

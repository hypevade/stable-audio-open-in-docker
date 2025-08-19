FROM pytorch/pytorch:2.1.2-cuda11.8-cudnn8-devel

RUN apt-get update && apt-get install -y \
    libsndfile1 \
    curl \
    && rm -rf /var/lib/apt/lists/*

ENV CUDA_HOME=/usr/local/cuda

# Install Python dependencies in a single layer
RUN pip install gradio xformers stable_audio_tools

WORKDIR /app
COPY main.py /app

CMD ["python", "main.py"]

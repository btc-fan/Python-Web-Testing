FROM tensorflow/tensorflow:1.15.5 as base
WORKDIR /app
COPY . .
ENV QT_DEBUG_PLUGINS="1"
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git protobuf-compiler && \
    git clone https://github.com/tensorflow/models --depth=1 --single-branch --branch=master && \
    cd models/research && \
    protoc object_detection/protos/*.proto --python_out=.
WORKDIR /app/captcha_model_training
RUN mkdir decoded_captchas
RUN pip3 install -r requirements.txt
ENV PYTHONPATH "${PYTHONPATH}:/app/models/research:/app/models/research/slim"
ENTRYPOINT ["python3", "runner.py"]
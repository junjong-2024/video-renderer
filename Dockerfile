FROM python:3.12.3-slim-bullseye

WORKDIR /app

RUN apt-get update \
    && apt-get install -y ffmpeg

COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY main.py ./
COPY render_ffmpeg.py ./

CMD ["python", "-u", "main.py"]
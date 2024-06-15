FROM python:3.12.3-slim-bullseye

WORKDIR /app

RUN apt-get update \
    && apt-get install -y ffmpeg

RUN wget http://cdn.naver.com/naver/NanumFont/fontfiles/NanumFont_TTF_ALL.zip
RUN unzip NanumFont_TTF_ALL.zip -d NanumFont
RUN rm -f NanumFont_TTF_ALL.zip
RUN mv NanumFont /usr/share/fonts/
RUN fc-cache -f -v

COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY main.py ./
COPY render_ffmpeg.py ./

CMD ["python", "-u", "main.py"]
FROM python:3.6-alpine

MAINTAINER Juan Carlos Serrano Pérez <juan.carlos.wow.95@gmail.com>

WORKDIR /app/docker

COPY . .

RUN pip install -r requirements.txt && \
    python -m nltk.downloader punkt && \
    python -m nltk.downloader stopwords && \
    python -m nltk.downloader maxent_treebank_pos_tagger

EXPOSE 80

CMD ["python", "app.py"]

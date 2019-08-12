FROM ubuntu:18.04



COPY . app

RUN apt-get update && \
    apt-get install -y build-essential \
                    python \
                    python3 \
                    python-dev \
                    python3-dev \
                    python-pip \
                    python3-pip \
                    openjdk-8-jdk-headless


RUN pip install pyspark

RUN pip install uwsgi && \
    pip install -r app/requirements.txt




EXPOSE 8080 7077 6066 3000 8000

CMD ["uwsgi", "--ini", "app/uwsgi.ini"]
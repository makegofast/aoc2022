FROM python:3

WORKDIR /app

COPY src/docker-entrypoint.sh /
COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

CMD /bin/bash /docker-entrypoint.sh

FROM python:3

WORKDIR /app

COPY src/docker-entrypoint.sh /

CMD /bin/bash /docker-entrypoint.sh

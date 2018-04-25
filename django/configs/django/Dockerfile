FROM python:alpine
MAINTAINER Deys Timofey <nxexox@gmail.com>

ARG uid=1000
ARG username=user

ENV PYTHONBUFFERED=1
ENV TERM=xterm-256color
ENV DJANGO_SETTINGS_MODULE=project.settings

RUN apk add --no-cache bash su-exec libpq freetype lcms2 libjpeg-turbo libwebp tiff zlib && \
    apk add --no-cache --virtual deps build-base postgresql-dev freetype-dev \
                                      lcms2-dev libjpeg-turbo-dev \
                                      libwebp-dev tiff-dev zlib-dev
COPY requirements.txt /tmp
RUN pip install --no-cache-dir -r /tmp/requirements.txt && rm /tmp/requirements.txt && \
    apk del --no-cache --purge deps

COPY wait-for-it.sh docker-entrypoint.sh /usr/local/bin/
RUN adduser -h /home/${username} -D -G wheel -u ${uid} ${username} && \
    chmod u+s /sbin/su-exec && \
    chmod +x /usr/local/bin/wait-for-it.sh /usr/local/bin/docker-entrypoint.sh

RUN mkdir -p /opt/code /opt/logs/
COPY . /opt/code
WORKDIR /opt/code

USER user
EXPOSE 8000
ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["gunicorn", "-c", "gunicorn.production.ini", "project.wsgi:application"]

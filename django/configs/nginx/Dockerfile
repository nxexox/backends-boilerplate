FROM nginx:stable-alpine
MAINTAINER Deys Timofey <nxexox@gmail.com>

ARG environment
ENV ENVIRONMENT=$environment

# Install bash
RUN apk add --update bash && rm -rf /var/cache/apk/*

# Remove preinstalled configs (except mime.types) and static files
RUN find /etc/nginx/* ! -name 'mime.types' -delete
RUN rm -r /usr/share/nginx/html/*

# Copy our own configs
COPY configs/nginx/nginx.conf /etc/nginx/nginx.conf

# Create bin directory for custom scripts
RUN mkdir -p /opt/bin

# Copy waiting script
COPY configs/utils/wait-for-it.sh /opt/bin

# Copy custom entrypoint
COPY configs/nginx/entrypoint.sh /opt/bin

# Make entrypoint and waiting script executable
RUN chmod +x /opt/bin/entrypoint.sh /opt/bin/wait-for-it.sh

# Write access and error logs to stdout and stderr
RUN ln -sf /dev/stdout /var/log/nginx/access.log
RUN ln -sf /dev/stderr /var/log/nginx/error.log

# Mount point for all media from backend
RUN mkdir /usr/share/nginx/media

# Mount point for all static files from backend
RUN mkdir /usr/share/nginx/static

ENTRYPOINT ["entrypoint.sh"]

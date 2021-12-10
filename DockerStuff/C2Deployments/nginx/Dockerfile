#######################################
# build with:
# docker build -t nginx-c2-proxy .
#######################################
# run with:
# docker run -d -p 443:443 --name nginx-c2-proxy nginx-c2-proxy
#######################################
FROM nginx:alpine

RUN apk update && \
  apk add --no-cache openssl && \
  rm -rf "/var/cache/apk/*"

RUN openssl req -x509 -nodes -days 365 -newkey rsa:4096 \
  -keyout /etc/ssl/private/nginx.key \
  -out /etc/ssl/certs/nginx.crt \
  -subj "/C=US/O=Mega Corp"

RUN set -x ; \
  addgroup -g 82 -S www-data ; \
  adduser -u 82 -D -S -G www-data www-data && exit 0

COPY --chown=www-data:www-data index.html /var/www/html/
COPY *.conf /etc/nginx/conf.d/

RUN rm 2>/dev/null /etc/nginx/sites-enabled/default || true
RUN rm 2>/dev/null /etc/nginx/conf.d/default.conf || true

EXPOSE 443

CMD nginx -g "daemon off;"

FROM alpine
RUN apk update && apk add cowsay fortune \
        --update-cache \
        --repository https://alpine.global.ssl.fastly.net/alpine/edge/community \
        --repository https://alpine.global.ssl.fastly.net/alpine/edge/main \
        --repository https://dl-3.alpinelinux.org/alpine/edge/testing

COPY wisecow.sh /app/wisecow.sh
WORKDIR /app
EXPOSE 4499
CMD ["sh","/app/wisecow.sh"]
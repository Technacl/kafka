FROM alpine:latest
ENV  APP_PORT 8004
RUN apk update
CMD echo "Hello fibonachi mixzoy"
RUN apk add --no-cache python3 py3-pip
RUN pip3 install kafka-python
RUN pip3 install kafka
COPY app/main.py ./app/main.py
WORKDIR /app
CMD ["sh", "-c", "python main.py"]

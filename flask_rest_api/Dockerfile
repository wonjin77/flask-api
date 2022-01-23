FROM python:3.8-alpine

WORKDIR /app

# Install native libraries, required for numpy
RUN apk --no-cache add musl-dev linux-headers g++ git

# Upgrade pip
RUN pip install --upgrade pip

RUN pip install flask
RUN pip install flask-restx
RUN pip install requests

EXPOSE 5001

COPY . /app

ENTRYPOINT [ "python" ]

CMD ["./app_rest_api.py" ]
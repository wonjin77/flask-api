FROM python:3.8

WORKDIR /app

RUN apt install git
# Upgrade pip
RUN pip install --upgrade pip

# packages that we need
RUN pip install numpy  --no-cache-dir && \
    pip install pandas --no-cache-dir

RUN pip install flask
RUN pip install requests


EXPOSE 5000

COPY . /app

ENTRYPOINT [ "python" ]

CMD ["./app_ui.py" ]
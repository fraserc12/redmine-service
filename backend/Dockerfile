FROM python:3.8.5-slim
ADD . /src
WORKDIR /src
RUN pip3 install -r requirements.txt
CMD python3 /src/scripts/server.py
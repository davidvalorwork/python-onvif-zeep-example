FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt
RUN apt update -y && apt install vim -y
RUN cd python-onvif-zeep && python setup.py install

ENTRYPOINT ["bash"]
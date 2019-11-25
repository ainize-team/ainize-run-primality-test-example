FROM python:3

COPY . /workspace
WORKDIR /workspace

EXPOSE 80

CMD python ./main.py

FROM python:3
CMD mkdir /opt/source
COPY . /opt/source
WORKDIR /opt/source
RUN pip install -r requirements.txt
ENTRYPOINT ["python","./main.py"]
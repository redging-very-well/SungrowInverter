FROM python:3.9-alpine

WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade -r requirements.txt

COPY influx influx
COPY mqtt mqtt
COPY sungrowinverter sungrowinverter
COPY *.py ./

CMD ["python", "run.py"]

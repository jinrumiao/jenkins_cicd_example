FROM python:3.10-slim

WORKDIR /workspace

COPY . /workspace

RUN pip3 install -r requirements.txt

CMD ["python3", "mlflow_exporter.py"]
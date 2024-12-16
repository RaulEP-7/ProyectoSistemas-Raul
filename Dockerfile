FROM python:3.12-slim
RUN pip install --no-cache-dir requests pymongo
COPY script1.py /
CMD ["python", "./script1.py"]

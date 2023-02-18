FROM python:alpine
WORKDIR /home/data
COPY ./ ./
CMD ["python" ,"python.py"]

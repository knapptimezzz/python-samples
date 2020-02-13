# Specify base container image
FROM python:3.6-slim

# Copy required files (source codes etc.)
COPY deduplication_demo/deduplication_demo.py /src/deduplication_demo.py
COPY deduplication_demo/requirements.txt requirements.txt
COPY protobuf_code/ /src/

# Run required command for building image
RUN pip3 install -r requirements.txt

# Specify a command to exec command when container started.
CMD ["python", "-u", "./src/deduplication_demo.py"]

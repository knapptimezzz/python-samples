# Specify base container image
FROM python:3.6-slim

# Copy required files (source codes etc.)
ADD src /src
ADD requirements.txt requirements.txt

# Run required command for building image
RUN pip3 install -r requirements.txt

# Specify ports to expose
EXPOSE 5672

# Specify working directory
WORKDIR /src

# Specify a command to exec command when container started.
CMD ["python", "-u", "./thresholdapp.py"]

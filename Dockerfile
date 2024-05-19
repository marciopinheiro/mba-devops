# Base image
FROM python:3.12-slim

# Installing necessary components
RUN apt update && apt -y upgrade

# Adjust Time Zone
ENV TZ=America/Sao_Paulo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Add files
COPY ./ /var/www

# Go to working directory
WORKDIR /var/www

# Install python requirements
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080
ENTRYPOINT gunicorn --config gunicorn.conf.py src
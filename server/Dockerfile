# Pull base image
FROM python:3.7

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#Install Dependencies
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r /app/requirements.txt
EXPOSE 8000

#Copy Files
COPY . /app
COPY ./alembic

RUN alembic revision --autogenerate -m "First migration"

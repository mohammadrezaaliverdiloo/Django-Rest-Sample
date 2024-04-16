#Base image
from python:3.11-alpine


# Environments
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# ENV LANGUAGE_CODE 'en-us'


WORKDIR /src

#install here
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .
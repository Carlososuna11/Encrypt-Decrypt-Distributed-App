

# pull official base image
FROM python:3.9.6-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN apk update \
    && apk add \
    postgresql-dev gcc g++ python3-dev musl-dev \
    zlib-dev make   

# install python dependencies
RUN pip install --upgrade pip
RUN pip install --upgrade pip setuptools wheel
COPY ./requirements.txt .
RUN pip install -r requirements.txt
# copy project
COPY . .

CMD ["sleep", "infinity"]
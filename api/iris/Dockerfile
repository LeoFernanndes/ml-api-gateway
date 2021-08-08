# pull official base image
FROM python:3.8

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy requirements file
COPY requirements.txt ./

# install dependencies
RUN pip install -r /usr/src/app/requirements.txt

# copy project
COPY . .
CMD ["uvicorn", "main:app", "--host",  "0.0.0.0", "--reload"]
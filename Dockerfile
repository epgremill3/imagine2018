FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /code \
 && apt-get update \
 && apt-get install -y --no-install-recommends postgresql-client \
 && rm -rf /var/lib/apt/lists/*
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/

# For Elastic Beanstalk
EXPOSE 8000
CMD ["python3", "manage.py", "runserver 0.0.0.0:8000"]

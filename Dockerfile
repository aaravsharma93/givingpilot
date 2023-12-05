FROM python:3.8
#RUN apk update \
#    && apk add --virtual build-deps gcc python3-dev libffi-dev libc-dev linux-headers \
#    && apk add --no-cache jpeg-dev zlib-dev postgresql-dev build-base

RUN apt-get update \
    && apt-get install -y --no-install-recommends libgl1  \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade setuptools pip


ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code
RUN pip install -r requirements.txt
COPY . /code
RUN mkdir logs
RUN cp .prod.env .env
RUN chmod +x /code/prestart_script.sh
ENTRYPOINT [ "/code/prestart_script.sh" ]
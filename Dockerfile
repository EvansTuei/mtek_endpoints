FROM python:3.8-slim-buster

LABEL KOKO analytics "analytics@kokonetworks.com"

RUN pip install gunicorn

#Leverage Docker cache
COPY requirements.txt /opt/requirements.txt

WORKDIR /opt

RUN pip install -r requirements.txt

COPY . /opt

ENV TZ=Africa/Nairobi
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

EXPOSE 8000

CMD gunicorn \
    --workers=12 \
    --timeout=180 \
    --bind 0.0.0.0:8000 \
    run_production:app

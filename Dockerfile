FROM python:3.9-slim-buster

RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential libpq-dev \
    unixodbc-dev \
    unixodbc \
    && rm -rf /var/lib/apt/lists/*

# RUN apt-get update \
#     && apt-get install -y curl apt-transport-https gnupg2 \
#     && curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
#     && curl https://packages.microsoft.com/config/debian/9/prod.list > /etc/apt/sources.list.d/mssql-release.list \
#     && apt-get update \
#     && ACCEPT_EULA=Y apt-get install -y msodbcsql17 mssql-tools

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0
ENV PORT=3000

RUN python -m pip install --upgrade pip

ADD ./requirements.txt /app/requirements.txt

RUN pip install  --no-cache-dir -r requirements.txt
COPY . .

RUN python manage.py collectstatic --noinput

# RUN addgroup app && adduser -S -G app app 
# USER app

CMD gunicorn Auto_Veh_back_end.wsgi:application --bind 0.0.0.0:$PORT  --timeout 600


FROM python:slim

EXPOSE 80

RUN pip install pipenv

RUN mkdir /var/www
COPY . /var/www
WORKDIR /var/www

RUN pipenv install
CMD pipenv run gunicorn -b 0.0.0.0:80 shop.wsgi

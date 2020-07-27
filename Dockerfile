FROM python

EXPOSE 8000

RUN mkdir /var/www
COPY . /var/www
WORKDIR /var/www

RUN pip install pipenv
RUN pipenv install

FROM python:3.6.3

# set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# add deps
ADD ./deps.txt /usr/src/app/deps.txt

# install deps
RUN pip install -r deps.txt

# add app
ADD . /usr/src/app

# run server 
CMD python manage.py runserver -h 0.0.0.0


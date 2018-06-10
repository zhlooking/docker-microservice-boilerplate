# Microservices with Docker, Flask, and React

[![Build Status](https://travis-ci.com/zhlooking/docker-microservice-boilerplate.svg?branch=master)](https://travis-ci.com/zhlooking/docker-microservice-boilerplate)

1. docker-machine create env/tc
2. eval $(docker-machine env dev)
3. docker-compose -up -d --build
4. docker-compose run users-service python manage.py recreate_db
5. docker-compose run users-service python manage.py seed_db
6. docker-compose run users-service python manage.py test
7. get docker-machine active ip // visit http://docker-machine-ip
8. cd client && yarn && yarn run dev && goto http://docker-machine-ip:3009
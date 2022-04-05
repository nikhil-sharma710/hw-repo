NAME ?= nikhilsharma710

all: build run push

images:
	docker images | grep ${NAME}

ps:
	docker ps -a | grep ${NAME}

build:
	docker build -t ${NAME}/hw05:1.0 .

run-redis:
	docker run -d -p 6429:6379 -v $(pwd)/data:/data:rw --name=nikhil-redis redis:6 --save 1 1 -u 876850:816966

run-flask:
	docker run --rm -d -p 5029:5000 --name nikhil-flask ${NAME}/hw05:1.0

stop:
	docker stop nikhil-flask

push:
	docker push ${NAME}/hw05:1.0

pull:
	docker pull ${NAME}/hw05:1.0

kill:
	docker rm -f nikhil-redis


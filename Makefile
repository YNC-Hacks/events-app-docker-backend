build:
	docker-compose up --build -d

stop:
	docker stop $$(docker ps -a -q)

remove:
	docker stop $$(docker ps -a -q)
	docker rm $$(docker ps -a -q);

purge:
	docker stop $$(docker ps -a -q)
	docker rm $$(docker ps -a -q);
	docker rmi $$(docker images -a -q)
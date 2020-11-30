# purge:
# 	docker stop $$(docker ps -a -q);
# 	docker rm $$(docker ps -a -q);
# 	docker rmi $$(docker images -a -q);

# create:
# 	docker-compose build
# 	docker-compose up -d

# createwithlogs:
# 	docker-compose build
# 	docker-compose up

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
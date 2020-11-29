<!-- # Docker Specific - To initialise Postgres Container

1. Build Image
```
docker build -t postgres-db
```

2. Start Container using Image
```
docker run -d --name postgres-db -p 5555:5432 postgres-db
``` -->

# Running Containers

1. Compose the container
```
docker-compose build
```

2. Fire Up Container
```
docker-compose up -d
```

# Maintanence
1. Removing all containers and images

```
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
docker rmi $(docker images -a -q)
```


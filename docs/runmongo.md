# running mongodb in a docker container

for more info : [visit mongo in dockerHub](https://hub.docker.com/_/mongo)

## run manually

just open a terminal and run this command :

```bash
docker run -v /var/mymongodb:/data/db -p 27017:27017 --rm --name mongoserver mongo
```

and keep the terminal window open.

with the above command the databases will be lost after closing the container.
so if you want to store data and re use them, use this instead :

```bash
docker run -v /var/mymongodb:/data/db -p 27017:27017 --rm --name mongoserver mongo
```
and if `/var/mymongodb` directory doesn't exists, create it :
```bash
mkdir /var/mymongodb
```


## run with docker compose

execute this command in the current directory

default admin username : `admin`

default admin password : `example`

```bash
docker-compose up -f ./docker-compose.yml
```
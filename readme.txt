
docker-compose up -d flask_db

docker-compose build

docker-compose up flask_app

docker stop $(docker ps -a -q)

docker rm $(docker ps -a -q)
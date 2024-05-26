docker stop onvif
docker rm onvif
docker rmi davidvalorwork/example-onvif
docker build -t davidvalorwork/example-onvif .
docker run -d --name onvif -t davidvalorwork/example-onvif
docker exec -it onvif bash

# docker push davidvalorwork/example-onvif
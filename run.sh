docker stop onvif
docker rm onvif
docker rmi onvif
docker build -t onvif .
docker run -d --name onvif -t onvif
docker exec -it onvif bash
cls

set versao=%1

docker build --tag cariuska:%versao% .

docker stop Cariuska

docker rm Cariuska

docker run --name Cariuska -d -p 80:80 cariuska:%versao%
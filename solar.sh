#!/bin/bash

echo "stopping existing container"
docker stop inverter &> /dev/null
docker rm inverter &> /dev/null

#export INFLUXDB_APIKEY=$(cat /media/drive/data/generated-secrets/influxdb_admin_apikey)
export INFLUXDB_APIKEY=$(cat /media/drive/data/generated-secrets/influxdb_solar_apikey)
export INFLUXDB_URL=http://10.0.0.10:8086

docker build -t inverter:latest .
docker run --name inverter -d --restart unless-stopped -e INFLUXDB_APIKEY=$INFLUXDB_APIKEY -e INFLUXDB_URL=$INFLUXDB_URL inverter:latest


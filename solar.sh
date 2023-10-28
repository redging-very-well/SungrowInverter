#!/bin/bash

echo "stopping existing container"
docker stop inverter &> /dev/null
docker rm inverter &> /dev/null

export INFLUXDB_APIKEY=$(cat /media/drive/data/generated-secrets/influxdb_solar_apikey)
export INFLUXDB_URL=http://10.0.0.10:8086

export MQTT_HOST="10.0.0.10"
export MQTT_PORT=1883
export MQTT_USERNAME=mqttLocalUser
export MQTT_PASSWORD=$(cat /media/drive/data/generated-secrets/mqtt_password)

docker build -t inverter:latest .
docker run --name inverter -d --restart unless-stopped \
  -e INFLUXDB_APIKEY=$INFLUXDB_APIKEY -e INFLUXDB_URL=$INFLUXDB_URL \
  -e MQTT_HOST=$MQTT_HOST -e MQTT_PORT=$MQTT_PORT -e MQTT_USERNAME=$MQTT_USERNAME -e MQTT_PASSWORD=$MQTT_PASSWORD \
  inverter:latest


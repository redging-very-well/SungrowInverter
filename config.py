import os

inverter_ip = "10.1.1.20"
scan_interval_seconds = 90

influxdb_url = os.environ.get('INFLUXDB_URL', "http://10.0.0.10:8086")
influxdb_apikey = os.environ.get('INFLUXDB_APIKEY', "***")
influxdb_org = "home"
influxdb_bucket = "inverter"

mqtt_url = os.environ.get('MQTT_HOST', "10.0.0.10")
mqtt_port = int(os.environ.get('MQTT_PORT', "1883"))
mqtt_username = os.environ.get('MQTT_USERNAME', "mqttLocalUser")
mqtt_password = os.environ.get('MQTT_PASSWORD', "TODO")
mqtt_publish_topic_root = "/home/power/solar/"
mqtt_keepalive_seconds = 300

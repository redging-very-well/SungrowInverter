import os

inverter_ip = "10.1.1.20"
scan_interval_seconds = 10

influxdb_url = "http://10.0.0.10:8086"
influxdb_apikey = os.environ.get('INFLUXDB_APIKEY', "***")
influxdb_org = "home"
influxdb_bucket = "inverter"

from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
import logging

class InfluxDBPublisher(object):
  def __init__(self, config):

    self.config = config
    self.client = InfluxDBClient(url=config.influxdb_url, token=config.influxdb_apikey, org=config.influxdb_org)
    self.write_api = self.client.write_api(write_options=SYNCHRONOUS)

    logging.info(f"influxdb client setup for host {config.influxdb_url}")


  def publish(self, fields):
    metrics = {
        "measurement": "modbus",
        "tags": {
        },
        "fields": fields,
    }

    self.write_api.write(bucket=self.config.influxdb_bucket, record=metrics)



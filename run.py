from dotenv import load_dotenv
from sungrowinverter import SungrowInverter
from importlib import import_module
from influx import InfluxDBPublisher
from mqtt import MQTTPublisher
import asyncio
import logging
import time

load_dotenv()

logging.basicConfig(level=logging.INFO)

try:
  config = import_module("config")
  logging.info(f"Loaded config")
except ModuleNotFoundError:
  logging.error("Unable to locate config.py")


loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
client = SungrowInverter(config.inverter_ip)
influxPublisher = InfluxDBPublisher(config)
mqttPublisher = MQTTPublisher(config)

while True:
  # Scrape the inverter
  result = loop.run_until_complete(client.async_update())
  if result:

    client.data['import_power'] = 0
    if client.data['export_power'] < 0:
      client.data['import_power'] = abs(client.data['export_power'])
      client.data['export_power'] = 0

    # Get a list of data returned from the inverter.
    logging.debug(client.data)

    influxPublisher.publish(client.data)
    mqttPublisher.publish(client.data)

  else:
    logging.warning("Error fetching data from inverter - trying again soon")
    client = SungrowInverter(config.inverter_ip)

  # Sleep until the next scan
  time.sleep(config.scan_interval_seconds)

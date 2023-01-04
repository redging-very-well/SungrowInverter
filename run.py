from dotenv import load_dotenv
from sungrowinverter import SungrowInverter
from importlib import import_module
from influx import InfluxDBPublisher
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
publisher = InfluxDBPublisher(config)

while True:
  # Scrape the inverter
  result = loop.run_until_complete(client.async_update())
  if not result:
    logging.error("Error fetching data from inverter")
    exit(1)

  # Get a list of data returned from the inverter.
  logging.debug(client.data)

  publisher.publish(client.data)

  # Sleep until the next scan
  time.sleep(config.scan_interval_seconds)
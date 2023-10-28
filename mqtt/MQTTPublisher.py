import paho.mqtt.client as mqtt

import logging

class MQTTPublisher(object):

  def __init__(self, config):

    self.config = config
    self.client = mqtt.Client(client_id="inverter-bridge")
    self.client.on_connect = self.on_connect

    self.client.username_pw_set(config.mqtt_username, config.mqtt_password)
    self.client.connect(config.mqtt_url, config.mqtt_port, keepalive=config.mqtt_keepalive_seconds)

    logging.info(f"MQTT client setup for host {config.mqtt_url}:{config.mqtt_port}")

  def on_connect(client, userdata, flags, rc):
    logging.info(f"Connected with result code: {rc}")

  def publish(self, fields):
    self.client.reconnect()

    batteryLevel = int(fields["battery_level"])
    solarGeneration = fields["total_dc_power"]
    logging.info(f"Sending mqtt values: battery: {batteryLevel}, solarGeneration: {solarGeneration}")

    publishResult = self.client.publish(self.config.mqtt_publish_topic_root + "battery/level", batteryLevel, retain=True)
    publishResult.wait_for_publish()

    publishResult = self.client.publish(self.config.mqtt_publish_topic_root + "generation", solarGeneration, retain=True)
    publishResult.wait_for_publish()

    logging.info("Sent values to mqtt")



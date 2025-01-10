import random
import paho.mqtt.client as mqtt
import time
import json

# MQTT broker settings
broker = "test.mosquitto.org"  # Replace with your MQTT broker address
port = 1883
sensor_topic = "/Mundiapolis/mesurements"  # Single topic for all measurements

# Setup MQTT client
client = mqtt.Client()
client.connect(broker, port, 60)

# Function to generate random temperature and humidity data
def generate_random_data():
    # Simulating temperature between -40°C and 80°C
    temperature = random.uniform(-40.0, 80.0)
    # Simulating humidity between 0% and 100%
    humidity = random.uniform(0.0, 100.0)
    return temperature, humidity

# Function to publish simulated data to MQTT broker
def publish_sensor_data():
    temperature, humidity = generate_random_data()

    # Create a JSON payload with both temperature and humidity
    payload = {
        "temperature": round(temperature, 2),
        "humidity": round(humidity, 2)
    }
    
    # Convert the payload to a JSON string
    payload_json = json.dumps(payload)
    
    # Publish data on the single topic
    print(f"Publishing Sensor Data: {payload_json} on topic {sensor_topic}")
    client.publish(sensor_topic, payload=payload_json, qos=0)

# Main loop
while True:
    publish_sensor_data()
    time.sleep(10)  # Simulate data every 10 seconds
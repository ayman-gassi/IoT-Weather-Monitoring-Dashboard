# IoT Weather Monitoring Dashboard

## Overview
The **IoT Weather Monitoring Dashboard** is a full-stack IoT project designed to collect, process, store, and visualize temperature and humidity data from Arduino sensors. The system uses an MQTT broker, Node-RED for data routing, InfluxDB for storage, and Grafana for visualization, all orchestrated through Docker Compose.

## Features
- **Arduino Sensors**: Reads temperature and humidity data.
- **Python Integration**: Transmits sensor data to the MQTT broker.
- **Node-RED Workflow**: Routes and formats data for InfluxDB.
- **InfluxDB**: Stores time-series data in Docker.
- **Grafana Dashboard**: Visualizes real-time and historical data in an intuitive UI.
- **Docker Compose**: Manages InfluxDB and Grafana for easy deployment.

## Architecture
1. **Arduino**: Collects temperature and humidity data via sensors.
2. **Python Script**: Reads sensor values and sends data to the MQTT broker.
3. **MQTT Broker**: Acts as a message hub for the data.
4. **Node-RED**: Processes and forwards the data to InfluxDB.
5. **InfluxDB**: Stores the data in a time-series database.
6. **Grafana**: Visualizes the data on a customizable dashboard.

## Requirements
- Arduino with DHT11/DHT22 sensor
- Python 3.7+
- Docker & Docker Compose
- MQTT Broker (e.g., Mosquitto)
- Node-RED
- Grafana and InfluxDB (via Docker Compose)

## usage

```bash
docker-compose up -d
```


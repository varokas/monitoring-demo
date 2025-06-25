# Monitoring Demo

A demonstration of OpenTelemetry metrics collection using Python, Prometheus, and Grafana.

## Overview

This project showcases how to:
- Send OpenTelemetry metrics from a Python application
- Collect metrics with Prometheus OTLP receiver
- Visualize metrics in Grafana

## Architecture

- **Python OTLP Demo**: Sends counter and gauge metrics via OTLP HTTP
- **Prometheus**: Collects metrics with OTLP receiver enabled
- **Grafana**: Pre-configured with Prometheus datasource for visualization

## Quick Start

1. Start the monitoring stack:
```bash
docker compose up -d
```

2. Access Grafana at http://localhost:3000
   - Username: `admin`
   - Password: `admin`

## Usage

### Continuous Metrics
The Python demo application automatically sends counter metrics every 10 seconds.

### One-time Metrics
To send a single gauge metric:
```bash
docker compose exec -it python-demo uv run src/onetime.py
```

## Services

- **Grafana**: http://localhost:3000
- **Prometheus**: http://localhost:9090 (internal only)

## Metrics Generated

- `demo_requests_total`: Counter tracking HTTP requests
- `demo_gauge`: Random gauge values (one-time script)

## Cleanup

```bash
docker compose down -v
```
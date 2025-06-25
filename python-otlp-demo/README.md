# Python OTLP Demo

A simple Python project that sends metrics via OTLP to Prometheus.

## Setup

1. Install dependencies:
```bash
uv sync
```

2. Start the monitoring stack:
```bash
docker-compose up -d
```

3. Run the demo:
```bash
cd python-otlp-demo
uv run main.py
```

## What it does

- Sends a sample counter metric `demo_requests_total` via OTLP HTTP
- Metric includes labels: `method=GET`, `endpoint=/hello`
- Exports metrics every 5 seconds to `http://localhost:4318/v1/metrics`

## View metrics

1. Access Grafana: http://localhost:3000 (admin/admin)
2. The Prometheus datasource is pre-configured
3. Query for `demo_requests_total` to see your metrics
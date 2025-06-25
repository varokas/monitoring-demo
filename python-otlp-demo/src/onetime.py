import time
from opentelemetry import metrics
from opentelemetry.exporter.otlp.proto.http.metric_exporter import OTLPMetricExporter
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.sdk.resources import Resource


def main():
    # Configure the resource (identifies this application)
    resource = Resource.create({"service.name": "python-otlp-demo"})
    
    # Create OTLP HTTP exporter - using service name for containerized environment
    otlp_exporter = OTLPMetricExporter(
        endpoint="http://prometheus:9090/api/v1/otlp/v1/metrics",
        headers={}
    )
    
    # Create metric reader with the exporter
    metric_reader = PeriodicExportingMetricReader(
        exporter=otlp_exporter,
        export_interval_millis=5000,  # Export every 5 seconds
    )
    
    # Create meter provider
    meter_provider = MeterProvider(
        resource=resource,
        metric_readers=[metric_reader]
    )
    
    # Set the global meter provider
    metrics.set_meter_provider(meter_provider)
    
    # Create a meter
    meter = metrics.get_meter(__name__)
    
    # Create a counter metric
    request_gauge = meter.create_gauge(
        name="demo_gauge",
        description="demo gauge",
        unit="1"
    )
    
    # Send metrics continuously
    print("Starting to send metrics...")
    import random
    request_gauge.set(random.randint(1, 100), {
        "method": "POST",
    })
        
    metric_reader.collect()
    print("Sent gauge metric")

if __name__ == "__main__":
    main()
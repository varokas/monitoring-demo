import time
from opentelemetry import metrics
from opentelemetry.exporter.otlp.proto.http.metric_exporter import OTLPMetricExporter
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.sdk.resources import Resource


def main():
    print("Hello World!")
    
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
    request_counter = meter.create_counter(
        name="demo_requests_total",
        description="Total number of demo requests",
        unit="1"
    )
    
    # Send metrics continuously
    print("Starting to send metrics...")
    counter = 0
    
    while True:
        counter += 1
        request_counter.add(1, {
            "method": "GET", 
            "endpoint": "/hello",
            "status": "200"
        })
        
        print(f"Sent metric #{counter}")
        time.sleep(10)  # Send a metric every 10 seconds

    


if __name__ == "__main__":
    main()
# boto3_client.py
import boto3
from opentelemetry.instrumentation.boto3 import Boto3Instrumentor

# Instrument boto3
Boto3Instrumentor().instrument()

# boto3 client usage
def get_s3_client():
    return boto3.client('s3')

# Additional boto3 client functions
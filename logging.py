import os, sys, logging
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobClient

def setup_blob_logger(blob_connection_string, container_name, blob_name):
    logger = logging.getLogger('azure.storage.blob')
    logger.setLevel(logging.DEBUG)

    handler = logging.StreamHandler(stream=sys.stdout)
    logger.addHandler(handler)

    blob_client = BlobClient.from_connection_string(blob_connection_string, container_name=container_name, blob_name=blob_name)

    with open("./sample-source.txt", "rb") as data:
        blob_client.upload_blob(data, logging_enable=True)

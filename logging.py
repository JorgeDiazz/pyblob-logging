import os, sys, logging
import datetime
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobClient

logs_file_name = None

def get_blob_logger():
    global logs_file_name

    logger = logging.getLogger('azure.storage.blob')
    logger.setLevel(logging.DEBUG)
    
    logs_file_name = 'logfile-{}-{}-{}.txt'.format(now.year, now.month, now.day)
    now = datetime.datetime.now()
    logging.basicConfig(filename=logfile_name)

    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter(logging.BASIC_FORMAT))
    logger.addHandler(handler)
    
    return logger


def save_logs(blob_connection_string, container_name, blob_path, blob_name):
    global logs_file_name

    blob_client = BlobClient.from_connection_string(blob_connection_string, container_name=container_name, blob_name=os.path.join(blob_path, blob_name))

    with open("./" + logfile_name, "rb") as data:
        blob_client.upload_blob(data, logging_enable=True)

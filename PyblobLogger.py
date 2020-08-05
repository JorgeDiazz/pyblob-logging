import os, logging, time, socket
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobClient

class PyblobLogger:

    DEBUG_LEVEL = logging.DEBUG
    ERROR_LEVEL = logging.ERROR

    logger = None
    ip_address = socket.gethostbyname(socket.gethostname())

    def __init__(self, logger_name, blob_description):
        self.logger = logging.getLogger(logger_name)
        self.blob_description = blob_description

    def setup_logging(self, logs_file_name):
        logging.basicConfig(filename=logs_file_name, format='%(asctime)s - %(name)s - %(levelname)s: %(message)s')

    def get_blob_client(self, logs_file_name):
        blob_connection_string = self.blob_description.connection_string
        container_name = self.blob_description.container_name
        project_path = self.blob_description.project_path

        return BlobClient.from_connection_string(blob_connection_string, 
            container_name=container_name, blob_name=os.path.join(project_path, logs_file_name))

    def upload_logs_to_blob_storage(self, logs_file_name):
        blob_client = self.get_blob_client(logs_file_name)
        with open("./" + logs_file_name, "rb") as logs:
            blob_client.upload_blob(logs, overwrite=True)

    def get_debug_logs_name(self):
        logs_file_name = 'logs_{}_{}.txt'.format(self.ip_address, time.strftime("%Y-%m-%d"))
        return os.path.join('debug/', logs_file_name)

    def get_error_logs_name(self):
        logs_file_name = 'logs_{}_{}.txt'.format(self.ip_address, time.strftime("%Y-%m-%d-%H:%M"))
        return os.path.join('error/', logs_file_name)

    def debug(self, message):
        self.logger.setLevel(self.DEBUG_LEVEL)

        logs_file_name = self.get_debug_logs_name()

        self.setup_logging(logs_file_name)
        self.logger.debug(message)
        self.upload_logs_to_blob_storage(logs_file_name)

    def error(self, message):
        self.logger.setLevel(self.ERROR_LEVEL)

        logs_file_name = self.get_error_logs_name()

        self.setup_logging(logs_file_name)
        self.logger.error(message)
        self.upload_logs_to_blob_storage(logs_file_name)

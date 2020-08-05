import os, logging, time, socket
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobClient

class PyblobLogger:

    DEBUG_LEVEL = logging.DEBUG
    ERROR_LEVEL = logging.ERROR
    LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

    ip_address = socket.gethostbyname(socket.gethostname())

    def __init__(self, logger_name, blob_description):
        self.setup_debug_logger(logger_name)
        self.setup_error_logger(logger_name)
        self.blob_description = blob_description

    def get_debug_logs_name(self):
        logs_file_name = 'logs_{}_{}.txt'.format(self.ip_address, time.strftime("%Y-%m-%d"))
        return os.path.join('debug/', logs_file_name)

    def get_error_logs_name(self):
        logs_file_name = 'logs_{}_{}.txt'.format(self.ip_address, time.strftime("%Y-%m-%d-%H:%M"))
        return os.path.join('error/', logs_file_name)

    def setup_debug_logger(self, logger_name):
        self.debug_logger = logging.getLogger('Debug-' + logger_name)
        self.debug_logger.setLevel(self.DEBUG_LEVEL)

        handler = logging.FileHandler(self.get_debug_logs_name())
        handler.setLevel(self.DEBUG_LEVEL)

        formatter = logging.Formatter(self.LOGGING_FORMAT)
        handler.setFormatter(formatter)

        self.debug_logger.addHandler(handler)

    def setup_error_logger(self, logger_name):
        self.error_logger = logging.getLogger('Error-' + logger_name)
        self.error_logger.setLevel(self.ERROR_LEVEL)

        handler = logging.FileHandler(self.get_error_logs_name())
        handler.setLevel(self.ERROR_LEVEL)

        formatter = logging.Formatter(self.LOGGING_FORMAT)
        handler.setFormatter(formatter)

        self.error_logger.addHandler(handler)

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

    def debug(self, message):
        self.debug_logger.debug(message)

        logs_file_name = self.get_debug_logs_name()
        self.upload_logs_to_blob_storage(logs_file_name)

    def error(self, message):
        self.error_logger.error(message)

        logs_file_name = self.get_error_logs_name()
        self.upload_logs_to_blob_storage(logs_file_name)

# PYBLOB LOGGING
Integrate this library on your project to log into Azure Blob Storage.

## Implementation
	from PyblobLogging import PyblobLogging
	from BlobDescription import BlobDescription
	import os
	import sys

	ROOT_DIR = os.path.dirname(sys.modules['__main__'].__file__)

	blob_description = BlobDescription(storage_connection_str, container_name, path_inside_container, ROOT_DIR)

	# Example:
	# blob_description = BlobDescription('DefaultEndpointsProtocol=https;AccountName=xx;AccountKey=xx/xxx/xx;EndpointSuffix=xx','my-container-name', 'directory1/directory2/', ROOT_DIR) 

	logger = PyblobLogging.get_blob_logger('My Logger Name', blob_description)

	# To log errors
	ex = Exception('Error')
	logger.error('This is an error log :(', ex)

	# To log another type of messages
	logger.debug('This is a debug log :)')


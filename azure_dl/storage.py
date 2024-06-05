from azure_dl import az_credential
from azure.storage.filedatalake import (
	DataLakeServiceClient,
	DataLakeDirectoryClient,
	FileSystemClient
)


def adls_client(storage_account, container):
	account_url = f'https://{storage_account}.dfs.core.windows.net'
	service_client = DataLakeServiceClient(
	account_url, credential=az_credential)
	return service_client.get_file_system_client(container)


def get_files_by_extension(client, directory, extension):
	paths = client.get_paths(path=directory)
	return [path for path in paths if path.name.endswith(extension)]

def get_file(client, path):
	return

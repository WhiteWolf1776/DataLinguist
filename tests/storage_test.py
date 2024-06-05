import pytest
from azure_dl import storage

#move this later
with open("tests/config/dev_storage.cfg", 'r') as f:
	global storage_account
	storage_account = f.readline().strip()
	global storage_container
	storage_container = f.readline().strip()
	global storage_path
	storage_path = f.readline().strip()
	global storage_extension
	storage_extension = f.readline().strip()
	global storage_sub_path1
	storage_sub_path1 = f.readline().strip()
	global storage_sub_path2
	storage_sub_path2 = f.readline().strip()

def testStorage():
	std_client_raw = storage.adls_client(storage_account, storage_container)
	paths = storage.get_files_by_extension(
				std_client_raw, storage_sub_path2, storage_extension)
	print(paths)
	assert len(paths) > 10


def testAvro():
	std_client_raw = storage.adls_client(storage_account, storage_container)
	paths = storage.get_files_by_extension(
					std_client_raw, storage_sub_path1,
					storage_extension)
	assert len(paths) > 1


def testAvroToDelta():
	assert True

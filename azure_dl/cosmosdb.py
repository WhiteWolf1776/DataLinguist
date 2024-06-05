from azure.cosmos import exceptions, CosmosClient, PartitionKey
from azure.mgmt.cosmosdb import CosmosDBManagementClient


def cosmos_client(cosmos_account):
	url = f'https://{cosmos_account}.documents.azure.com:443/'
	client = CosmosClient(url, az_credential)
	for db in client.list_databases():
		print(db)
	return

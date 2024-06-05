from azure.identity import DefaultAzureCredential

az_credential = DefaultAzureCredential(
	exclude_interactive_browser_credential=False)

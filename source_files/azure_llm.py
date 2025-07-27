from azure.identity import DefaultAzureCredential
from autogen_ext.models.openai import AzureOpenAIChatCompletionClient
from autogen_core.models import UserMessage
import os

def get_client() -> AzureOpenAIChatCompletionClient:
    """
    Initializes and returns an AzureOpenAIChatCompletionClient using environment variables for configuration.

    Environment Variables:
        AZURE_DEPLOYMENT_NAME: Name of the Azure OpenAI deployment.
        AZURE_MODEL_NAME: Name of the model to use.
        OPENAI_API_VERSION: API version for the OpenAI service.
        AZURE_OPENAI_ENDPOINT: Endpoint URL for the Azure OpenAI service.
        AZURE_OPENAI_API_KEY: API key for authentication.

    Returns:
        AzureOpenAIChatCompletionClient: Configured client instance for interacting with Azure OpenAI.
    """
    client = AzureOpenAIChatCompletionClient(
        azure_deployment=os.getenv("AZURE_DEPLOYMENT_NAME"),
        model=os.getenv("AZURE_MODEL_NAME"),
        api_version=os.getenv("OPENAI_API_VERSION"),
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        api_key=os.getenv("AZURE_OPENAI_API_KEY")
    )
    return client

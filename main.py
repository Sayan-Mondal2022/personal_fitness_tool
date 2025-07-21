
# Note: Replace **<YOUR_APPLICATION_TOKEN>** with your actual Application token
import requests
import os
from dotenv import load_dotenv 

load_dotenv()
LANGFLOW_API_KEY = os.getenv("LANGFLOW_API_KEY")


url = f"https://api.langflow.astra.datastax.com/lf/9da4e891-86aa-4a39-a91e-c960493c27bf/api/v1/run/8c4721cb-06a0-45ea-bd21-2656b2f0f029"  

# Request payload configuration
payload = {
    "tweaks": {
        "TextInput-SIUbz": {
            "input_value": "question"
        },
        "TextInput-XsYLB": {
            "input_value": "profile"
        }
    }
}

# Request headers
headers = {
    "Content-Type": "askAgent.json",
    "Authorization": LANGFLOW_API_KEY  # Authentication key from environment variable'}
}

try:
    # Send API request
    response = requests.request("POST", url, json=payload, headers=headers)
    response.raise_for_status()  # Raise exception for bad status codes

    # Print response
    print(response.text)

except requests.exceptions.RequestException as e:
    print(f"Error making API request: {e}")
except ValueError as e:
    print(f"Error parsing response: {e}")
    
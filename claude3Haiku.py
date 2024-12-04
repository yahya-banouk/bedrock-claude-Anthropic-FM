import boto3
import json

# Initialize Bedrock Runtime Client
bedrock_runtime_client = boto3.client('bedrock-runtime', region_name='us-east-1')

# Define the model ID
MODEL_ID = "anthropic.claude-3-haiku-20240307-v1:0"

# Define the prompt
prompt = """

Convert this data :
'3478', 'dev', 
to a Json of this attributs 

"""

# Define the payload
payload = {
    "anthropic_version": "bedrock-2023-05-31",
    "max_tokens": 2000,
    "top_k": 500,
    "temperature": 1,
    "top_p": 0.999,
    "messages": [
        {
            "role": "user",
            "content": prompt
        }
    ]
}

# Call the Bedrock API
try:
    response = bedrock_runtime_client.invoke_model(
        modelId=MODEL_ID,
        body=json.dumps(payload),
        accept="application/json",
        contentType="application/json",
    )
    
    # Parse the StreamingBody response
    response_body = response['body'].read().decode('utf-8')  # Read and decode the response
    result = json.loads(response_body)  # Parse the JSON content
    print("Generated JSON Output:")
    print(json.dumps(result, indent=2))
except Exception as e:
    print(f"Error invoking model: {e}")

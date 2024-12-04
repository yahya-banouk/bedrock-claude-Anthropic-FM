import boto3
import json
from fastapi import FastAPI, HTTPException

app = FastAPI()

# Initialize Bedrock Runtime Client
bedrock_runtime_client = boto3.client('bedrock-runtime', region_name='us-east-1')

# Define the Inference Profile ARN
INFERENCE_PROFILE_ARN = "arn:aws:bedrock:us-east-1:078143108430:inference-profile/us.anthropic.claude-3-5-haiku-20241022-v1:0"

# Define the prompt (this will be passed as input)
prompt = """

Convert this data :
'3478', 'dev', 
to a Json of this attributs 

"""

@app.post("/convert")
async def convert_data():
    # Define the payload
    payload = {
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt
                    }
                ]
            }
        ],
        "max_tokens": 2000,
        "anthropic_version": "bedrock-2023-05-31"
    }

    try:
        # Call the Bedrock API
        response = bedrock_runtime_client.invoke_model(
            modelId=INFERENCE_PROFILE_ARN,
            body=json.dumps(payload),
        )

        # Parse the StreamingBody response
        response_body = response['body'].read().decode('utf-8')  # Read and decode the response
        result = json.loads(response_body)  # Parse the JSON content

        # Return the result as JSON
        return result

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error invoking model: {e}")

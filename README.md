# bedrock-claude-Anthropic-FM

This project is a FastAPI application that leverages AWS Bedrock's Claude-3.5 model to convert complex data strings into structured JSON objects. It uses the Bedrock Runtime API for AI-powered data transformation.

---

## Features

- Accepts text-based input with structured data
- Converts the data into JSON format with predefined attributes
- Powered by AWS Bedrock with Anthropic's Claude-3.5 model
- Simple REST API implementation using FastAPI

---

## Prerequisites

Before starting, ensure you have the following:

1. **AWS Credentials** with access to Bedrock then create a user with bedrock fullaccess permission and get the access key add it to you're local CLI using the cmd "AWS configure" .
2. **Python 3.8+** installed on your local machine.
3. **AWS CLI** configured with a profile.

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/bedrock-json-converter.git
   cd bedrock-json-converter

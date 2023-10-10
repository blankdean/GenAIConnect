from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from dotenv import load_dotenv
import os
import requests

# Load environment variables
load_dotenv()

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# OAuth2 token endpoint (dummy implementation)
@app.post("/token")
async def token(form_data: OAuth2PasswordRequestForm = Depends()):
    return {"access_token": form_data.username + "_token", "token_type": "bearer"}

# Endpoint to interact with OpenAI GPT-3
@app.post("/generate-text")
async def generate_text(prompt: str, token: str = Depends(oauth2_scheme)):
    # Get the OpenAI API key from environment variables
    openai_api_key = os.getenv("OPENAI_API_KEY")

    # Check if the OpenAI API key is set
    if openai_api_key is None:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="OpenAI API Key not set")

    headers = {
        "Authorization": f"Bearer {openai_api_key}",
        "Content-Type": "application/json"
    }
    
    data = {
        "prompt": prompt,
        "max_tokens": 150
    }
    
    response = requests.post("https://api.openai.com/v1/engines/davinci/completions", headers=headers, json=data)
    
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    
    return response.json()

# Placeholder for other endpoints
# ...

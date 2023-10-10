from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm 
from dotenv import load_dotenv
from .adapters import AbstractLLM
from .middleware import SensitiveInfoCheck
from .utils import Cache
from .routers import text_analysis, text_generation

app = FastAPI()
app.include_router(text_analysis.router, prefix="/text")
app.include_router(text_generation.router, prefix="/text")

# Load environment variables
load_dotenv()

cache = Cache()

# Connect to our Redis Cache
@app.on_event("startup")
async def startup():
    cache.connect()

@app.middleware("http")
async def sensitive_info_middleware(request, call_next):
    # Instantiate the middleware class
    sensitive_info_check = SensitiveInfoCheck()
    # Process the request and response
    response = await sensitive_info_check.process(request, call_next) # return error if sensitive data found
    return response

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
# OAuth2 token endpoint (dummy implementation)
@app.post("/token")
async def token(form_data: OAuth2PasswordRequestForm = Depends()):
    return {"access_token": form_data.username + "_token", "token_type": "bearer"}
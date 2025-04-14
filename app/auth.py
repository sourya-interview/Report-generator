from fastapi import Header, HTTPException, Depends
from fastapi.security.api_key import APIKeyHeader

API_KEY = "supersecret123"
api_key_header = APIKeyHeader(name="x-api-key",auto_error=False)

def verify_api_key(x_api_key: str = Depends(api_key_header)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")
    
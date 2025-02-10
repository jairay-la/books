from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import os

app = FastAPI()

class BookRequest(BaseModel):
    title: str
    grade: str

# Assuming Flowise is deployed and accessible at this URL
# Replace with the actual URL of your deployed Flowise instance
FLOWISE_API_URL = os.environ.get('lAZFo7LaeVXqo_v0bSXhBKOcvIsRkVobqKY1OtkFUHc', 'http://https://github.com/jairay-la/books/api/v1/prediction/c8f7e207-85cb-4fed-8829-f341ce75b72e')

@app.post("/api/process")
async def process(book: BookRequest):
    try:
        response = requests.post(FLOWISE_API_URL, json=book.dict())
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3000)

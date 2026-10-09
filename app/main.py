#Python package install of FastAPI and Uvicorn
#Creating simple endpoints and to get used to pattern of
#handing JSON 


#From the fast api package we will be using the FastAPI class
from fastapi import FastAPI


#Here we are creating an instance of the application aka app
app = FastAPI(
    title="CryptoV2 & Live Account",
    version="0.1.0"
)

#Register root function as a GET endpoint
@app.get("/")
#With the intention to return information regarding the project in JSON format
def root():
    return {
        "project":"CryptoV2 & Live Account",
        "status": "running"
    }

#Want to make sure the function is properly working and responsive
#AKA a endpoint used to make sure the API is up and responsive
#will a simple return status
@app.get("/health")
def health():
    return {"status": "ok"}






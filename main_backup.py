
from fastapi import FastAPI
from pydantic import BaseModel
from urllib.error import HTTPError
from fastapi.exceptions import HTTPException

# import ai_search
import txtai
from txtai.embeddings import Embeddings

import uvicorn

app = FastAPI()



@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/search/{search_query}")
def search_documents(search_query: str):
    # try:
    #     # result = ai_search.ai_search(search_query)
    #     result = "result"
    #     return result
    # except HTTPError as e:
    #     raise HTTPException(status_code=e.code, detail=e.reason)
    print("called")
    embeddings = txtai.Embeddings({
        "path": "sentence-transformers/all-MiniLM-L6-v2"
    })
    print("called1")

    # embeddings.index(["Correct", "Not what we hoped"])
    embeddings.load("models/vol7_index")
    print("called2")

    result = embeddings.search(search_query, 10)
    print("test search result: ", result)
    return result

@app.post("/search/{search_query}")
def post_search_documents(search_query: str):
    # try:
    #     # result = ai_search.ai_search(search_query)
    #     result = "result"
    #     return result
    # except HTTPError as e:
    #     raise HTTPException(status_code=e.code, detail=e.reason)

    embeddings = txtai.Embeddings()
    embeddings.load("models/vol7_index")
    result = embeddings.search(search_query, 10)
    print("test search result: ", result)
    return result

if __name__ == "__main__":
    app.run()
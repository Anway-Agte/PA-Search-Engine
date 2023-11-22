from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
from urllib.error import HTTPError
from fastapi.exceptions import HTTPException

import ai_search
import txtai
from txtai.embeddings import Embeddings


app = FastAPI()

class Paper(BaseModel):
    index: int
    filename: str
    text: str

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

    embeddings = txtai.Embeddings()
    embeddings.index(["Correct", "Not what we hoped"])
    result = embeddings.search(search_query, 1)

    return result

@app.put("/search/{search_query}")
def post_search_documents(search_query: str):
    # try:
    #     # result = ai_search.ai_search(search_query)
    #     result = "result"
    #     return result
    # except HTTPError as e:
    #     raise HTTPException(status_code=e.code, detail=e.reason)

    embeddings = txtai.Embeddings()
    embeddings.index(["Correct", "Not what we hoped"])
    result = embeddings.search(search_query, 1)

    return result
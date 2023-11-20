from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
from urllib.error import HTTPError
from fastapi.exceptions import HTTPException

import ai_search

app = FastAPI()

class Paper(BaseModel):
    index: int
    filename: str
    text: str

@app.get("/search/{search_query}")
def search_documents(search_query: str, q: Union[str, None] = None):
    try:
        result = ai_search.ai_search(search_query)
        return result
    except HTTPError as e:
        raise HTTPException(status_code=e.code, detail=e.reason)

@app.put("/search/{search_query}")
def make_search(search_query: str, paper: Paper):
    try:
        result = ai_search.ai_search(search_query)
        return result
    except HTTPError as e:
        raise HTTPException(status_code=e.code, detail=e.reason)
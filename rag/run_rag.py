import requests
url = "https://test-ai-search.onrender.com"
headers = {"Content-Type": "application/json"}


def rag(text):
    return requests.get(f"{url}/rag?text={text}").json()["response"]

rag("Who is the current President?")
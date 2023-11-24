from datasets import load_dataset
import requests

ds = load_dataset("ag_news", split="train")

# API endpoint
# url = "https://localhost:5001"
url = "https://test-ai-search.onrender.com"
headers = {"Content-Type": "application/json"}

# Add data
batch = []
for text in ds["text"]:
  batch.append({"text": text})
  if len(batch) == 4096:
    requests.post(f"{url}/add", headers=headers, json=batch, timeout=120)
    batch = []

if batch:
    requests.post(f"{url}/add", headers=headers, json=batch, timeout=120)

# Build index
index = requests.get(f"{url}/index")


def rag(text):
    response = requests.get(f"{url}/rag?text={text}")
    if response.status_code == 200:
        return response.json()["response"]
    else:
        print(response.status_code)
        return None
    # return requests.get(f"{url}/rag?text={text}").json()["response"]

print(rag("Who is the current President?"))
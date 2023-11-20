from txtai.embeddings import Embeddings
# import txtai as t
import json
import os
import urllib3

def ai_search(query_text):
    embeddings = Embeddings({
        "path": "sentence-transformers/all-MiniLM-L6-v2"
    })

    txtai_data = []
    i = 0

    file_list = os.listdir("PA_LENR/Clean data/")
    # http = urllib3.PoolManager()
    # url = "https://github.com/Anway-Agte/PA-Search-Engine/tree/ai-search/PA_LENR/Clean%20data"
    # resp = urllib3.request("GET", url)
    # print(resp.status, resp.data)

    for idx, filename in enumerate(file_list):
        with open("PA_LENR/Clean data/"+filename, 'r') as f:
            text = filename + "\n" + f.read()
            txtai_data.append((idx, text, None))


    embeddings.index(txtai_data)

    res = embeddings.search("query_text", 10)
    # res[0]

    best = res[0]
    print({txtai_data[best[0]]}) # index, filename, text
    print(best[1]) # score

    embeddings.save("models/vol7_index")

    return res


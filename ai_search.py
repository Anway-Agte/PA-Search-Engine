from txtai.embeddings import Embeddings
# import txtai as t
import json
# import os
import urllib3

def ai_search(query_text):
    embeddings = Embeddings({
        "path": "sentence-transformers/all-MiniLM-L6-v2"
    })

    txtai_data = []

    # file_list = os.listdir("PA_LENR/Clean data/")
    # http = urllib3.PoolManager()
    # url = "https://github.com/Anway-Agte/PA-Search-Engine/tree/ai-search/PA_LENR/Clean%20data"
    # resp = urllib3.request("GET", url)
    # print(resp.status, resp.data)

    # for idx, filename in enumerate(file_list):
    #     with open("PA_LENR/Clean data/"+filename, 'r') as f:
    #         text = filename + "\n" + f.read()
    #         txtai_data.append((idx, text, None))
    txtai_idx = 0
    for i in range(3547):
        url = "https://github.com/Anway-Agte/PA-Search-Engine/tree/ai-search/PA_LENR/Clean%20data/Copy%20of%20"+str(i)+".txt"
        try:
            resp = urllib3.request("GET", url)
            print(resp.status, resp.data)
            txtai_data.append((txtai_idx, resp.data, None))
            txtai_idx += 1
        except:
            pass



    embeddings.index(txtai_data)

    res = embeddings.search("query_text", 10)
    # res[0]

    best = res[0]
    print({txtai_data[best[0]]}) # index, filename, text
    print(best[1]) # score

    embeddings.save("models/vol7_index")

    return res


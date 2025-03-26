import requests
import json

async def fetch_inline_search_images(query: str, count: int = 10):
    url = "https://google.serper.dev/images"
    
    payload = json.dumps({
    "q": f"{query}",
    "num": 20
    })
    headers = {
    'X-API-KEY': 'c67ca95163dc03a0427988e7e066f3010e4e95ac',
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    
    results = [img["imageUrl"] for img in  response.json()["images"] ]
    results = list(filter(lambda x:x.endswith(".png") or x.endswith(".jpg"),results ))
    return results[:count]

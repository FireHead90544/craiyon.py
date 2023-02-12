from __future__ import annotations
import aiohttp
import requests
from craiyon.templates import GeneratedImages

class Craiyon:
    '''
    Instantiates a Craiyon session, allows user to generate images from text tokens.
    The model takes some time to generate the images (roughly around 2 minutes).
    So be patient, and don't abuse the api, as I am not the one hosting the model, craiyon itself is.
    '''
    def __init__(self) -> None:
        self.BASE_URL = "https://backend.craiyon.com"
    
    def generate(self, tokens: str) -> GeneratedImages:
        session = requests.Session()
        url = self.BASE_URL + "/generate"
        resp = session.post(url, json={'prompt': tokens})
        return GeneratedImages(resp.json()['images'])

    async def async_generate(self, tokens: str) -> GeneratedImages:
        url = self.BASE_URL + "/generate"
        async with aiohttp.ClientSession() as sess:
            async with sess.post(url, json={"prompt": tokens}) as resp:
                resp = await resp.json()
                return GeneratedImages(resp['images'])
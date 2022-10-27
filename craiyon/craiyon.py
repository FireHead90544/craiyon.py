from __future__ import annotations
import aiohttp
from craiyon.templates import GeneratedImages
import aiofiles

class Craiyon:
    '''
    Instantiates a Craiyon session, allows user to generate images from text tokens.
    The model takes some time to generate the images (roughly around 2 minutes).
    So be patient, and don't abuse the api, as I am not the one hosting the model, craiyon itself is.
    '''
    def __init__(self) -> None:
        self.BASE_URL = "https://backend.craiyon.com"

    async def generate(self, tokens: str) -> GeneratedImages:
        url = self.BASE_URL + "/generate"
        async with aiohttp.ClientSession() as sess:
            async with sess.post(url,json={"prompt": tokens}) as resp:
                return GeneratedImages(await resp.json())

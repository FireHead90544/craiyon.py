from __future__ import annotations
import requests
from craiyon.templates import GeneratedImages

class Craiyon:
    '''
    Instantiates a Craiyon session, allows user to generate images from text tokens.
    The model takes some time to generate the images (roughly around 2 minutes).
    The code is itself blocking, so either use a thread or wait for me to write an async version.
    So be patient, and don't abuse the api, as I am not the one hosting the model, craiyon itself is.
    '''
    def __init__(self) -> None:
        self.BASE_URL = "https://backend.craiyon.com"
        self.session = requests.Session()

    def generate(self, tokens: str) -> GeneratedImages:
        url = self.BASE_URL + "/generate"
        resp = self.session.post(url, json={'prompt': tokens})
        return GeneratedImages(resp.json()['images'])
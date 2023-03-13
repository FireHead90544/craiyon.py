from __future__ import annotations
import aiohttp
import requests
from craiyon.templates import GeneratedImagesV1, GeneratedImagesV2


# V2 version of Craiyon API
class Craiyon:
    '''
    Instantiates a Craiyon session, allows user to generate images from text prompts.
    The model takes some time to generate the images (roughly around 1 minute).
    So be patient, and don't abuse the api, as I am not the one hosting the model, craiyon itself is.
    
    Arguments:        
        - (Not required) | api_token: Useful if you're paying for a subscription on Craiyon's website and want to remove the watermark from the generated images
        
        - (Not required) | model_version: Since Craiyon is constantly updating their V2 model seemingly everyday, you can specify a newer model here.
        Defaults to \"35s5hfwn9n78gb06\" (March 10th Model) if nothing is specified here
        
    '''
    def __init__(self, api_token=None, model_version="35s5hfwn9n78gb06") -> None:
        self.BASE_URL = "https://api.craiyon.com"
        self.DRAW_API_ENDPOINT = "/draw"
        self.model_version = model_version
        self.api_token = api_token
    
    # Generate images with V2
    def generate(self, prompt: str) -> GeneratedImagesV2:
        
        """
        Generates 9 images using the V2 model of Craiyon.
        
        Arguments:
        - (Required) | Prompt: The text prompt that will be used to generate the images

        Returns:
        - Returns a list of direct image links to `.webp` images, from https://img.craiyon.com
        """
            
        url = self.BASE_URL + self.DRAW_API_ENDPOINT
        session = requests.Session()
        resp = session.post(url, json={'prompt': prompt, "token": self.api_token, "version": self.model_version})
        
        resp = resp.json()
                
        # Add protocol, domain and subdomain (https://img.craiyon.com) to each item as those aren't included in the response by default
        images = [f"https://img.craiyon.com/{item}" for item in resp['images']]
        
        return GeneratedImagesV2(images)
    
    # Generate images with V2, asynchronously
    async def async_generate(self, prompt: str) -> GeneratedImagesV2:
        
        """
        Generates 9 images asynchronously using the V2 model of Craiyon.
        
        Arguments:
        - (Required) | Prompt: The text prompt that will be used to generate the images

        Returns:
        - Returns a list of direct image links to `.webp` images, from https://img.craiyon.com
        """
        
        url = self.BASE_URL + self.DRAW_API_ENDPOINT
        async with aiohttp.ClientSession() as sess:
            async with sess.post(url, json={'prompt': prompt, "token": self.api_token, "version": self.model_version}) as resp:
                urls_no_domain = await resp.json()
                # Add protocol, domain and subdomain (https://img.craiyon.com) to each item as those aren't included in the response by default
                images = [f"https://img.craiyon.com/{item}" for item in urls_no_domain['images']]
        
                return GeneratedImagesV2(images)
    
# V1 version of Craiyon API, for backwards compatibility
class CraiyonV1:
    '''
    **NOTICE**: This is the V1 version of Craiyon's model. To use the updated V2 model, use the normal `Craiyon` class instead.
    
    Instantiates a Craiyon session, allows user to generate images from text prompts.
    The model takes some time to generate the images (roughly around 1 minute).
    So be patient, and don't abuse the api, as I am not the one hosting the model, craiyon itself is.
    '''
    
    
    def __init__(self) -> None:
        self.BASE_URL = "https://backend.craiyon.com"
        self.DRAW_API_ENDPOINT = "/generate"
    
    def generate(self, prompt: str) -> GeneratedImagesV1:
        
        """
        Generates 9 images using the V1 model of Craiyon.
        
        Arguments:
        - (Required) | Prompt: The text prompt that will be used to generate the images
        
        Returns:
        - Returns a list of 9 Base64 bytestrings (.jpg)
        """
        
        session = requests.Session()
        url = self.BASE_URL + self.DRAW_API_ENDPOINT
        resp = session.post(url, json={'prompt': prompt})
        return GeneratedImagesV1(resp.json()['images'])

    async def async_generate(self, prompt: str) -> GeneratedImagesV1:
        
        """
        Generates 9 images asynchronously using the V1 model of Craiyon.
        
        Arguments:
        - (Required) | Prompt: The text prompt that will be used to generate the images
        
        Returns:
        - Returns a list of 9 Base64 bytestrings (.jpg)
        """
        
        url = self.BASE_URL + self.DRAW_API_ENDPOINT
        async with aiohttp.ClientSession() as sess:
            async with sess.post(url, json={"prompt": prompt}) as resp:
                resp = await resp.json()
                return GeneratedImagesV1(resp['images'])
from __future__ import annotations
import aiohttp
import requests
from craiyon.templates import GeneratedImages


# v3 version of Craiyon API
class Craiyon:
    '''
    Instantiates a Craiyon session, allows user to generate images from text prompts.
    The model takes some time to generate the images (roughly around 1 minute).
    So be patient, and don't abuse the api, as I am not the one hosting the model, craiyon itself is.
    
    Arguments:        
        - (Not required) | api_token: Useful if you're paying for a subscription on Craiyon's website and want to remove the watermark from the generated images
        
        - (Not required) | model_version: Since Craiyon is constantly updating their v3 model seemingly everyday, you can specify a newer model here.
        Defaults to \"35s5hfwn9n78gb06\" (March 10th Model) if nothing is specified here
    '''
    
    def __init__(self, api_token=None, model_version="35s5hfwn9n78gb06") -> None:
        self.BASE_URL = "https://api.craiyon.com"
        self.DRAW_API_ENDPOINT = "/v3"
        self.model_version = model_version
        self.api_token = api_token

    # Generate images with v3
    def generate(self, prompt: str, negative_prompt: str = "", model_type: str = "none") -> GeneratedImages:
        """
        Generates 9 images using the v3 model of Craiyon.
        
        Arguments:
        - (Required) | prompt: The text prompt that will be used to generate the images

        - (Not Required) | negative_prompt: What you don't want to see in the images
        Defaults to "" (Let the model decide)

        - (Not Required) | model_type: The type of images to be generated
        Defaults to "none" (Let the model decide), available options include "art", "drawing", "photo", "none"

        Returns:
        - Returns a list of direct .webp image links from https://img.craiyon.com and a Description about the generated images
        """

        url = self.BASE_URL + self.DRAW_API_ENDPOINT
        session = requests.Session()
        resp = session.post(url, json={'prompt': prompt, "negative_prompt": negative_prompt, "model": model_type, "token": self.api_token, "version": self.model_version})
        resp = resp.json()

        # Add protocol, domain and subdomain (https://img.craiyon.com) to each item as those aren't included in the response by default
        images = [f"https://img.craiyon.com/{item}" for item in resp['images']]

        return GeneratedImages(images, description=resp["next_prompt"], model="v3")
    
    # Generate images with v3, asynchronously
    async def async_generate(self, prompt: str, negative_prompt: str = "", model_type: str = "none") -> GeneratedImages:
        """
        Generates 9 images asynchronously using the v3 model of Craiyon.
        
        Arguments:
        - (Required) | prompt: The text prompt that will be used to generate the images

        - (Not Required) | negative_prompt: What you don't want to see in the images
        Defaults to "" (Let the model decide)

        - (Not Required) | model_type: The type of images to be generated
        Defaults to "none" (Let the model decide), available options include "art", "drawing", "photo", "none"

        Returns:
        - Returns a list of direct .webp image links from https://img.craiyon.com and a Description about the generated images
        """

        url = self.BASE_URL + self.DRAW_API_ENDPOINT
        async with aiohttp.ClientSession() as sess:
            async with sess.post(url, json={'prompt': prompt, "negative_prompt": negative_prompt, "model": model_type, "token": self.api_token, "version": self.model_version}) as resp:
                resp = await resp.json()
                # Add protocol, domain and subdomain (https://img.craiyon.com) to each item as those aren't included in the response by default
                images = [f"https://img.craiyon.com/{item}" for item in resp['images']]
        
                return GeneratedImages(images, description=resp["next_prompt"], model="v3")


# v2 version of Craiyon API, deprecated (removed completely)
# class CraiyonV2:
#     '''
#     **NOTICE**: This is the v2 version of Craiyon's model. This version is deprecated as the api endpoint is completely removed, so it won't work at all. This code is commented out just in hopes of the api endpoint getting back. To use the latest model, use the normal `Craiyon` class instead.
#
#     Instantiates a Craiyon session, allows user to generate images from text prompts.
#     The model takes some time to generate the images (roughly around 1 minute).
#     So be patient, and don't abuse the api, as I am not the one hosting the model, craiyon itself is.
#    
#     Arguments:        
#         - (Not required) | api_token: Useful if you're paying for a subscription on Craiyon's website and want to remove the watermark from the generated images
#        
#         - (Not required) | model_version: Since Craiyon is constantly updating their v2 model seemingly everyday, you can specify a newer model here.
#         Defaults to \"35s5hfwn9n78gb06\" (March 10th Model) if nothing is specified here
#        
#     '''
#
#     def __init__(self, api_token=None, model_version="35s5hfwn9n78gb06") -> None:
#         self.BASE_URL = "https://api.craiyon.com"
#         self.DRAW_API_ENDPOINT = "/draw"
#         self.model_version = model_version
#         self.api_token = api_token
#    
#     # Generate images with v2
#     def generate(self, prompt: str) -> GeneratedImages:
#         """
#         Generates 9 images using the v2 model of Craiyon.
#        
#         Arguments:
#         - (Required) | prompt: The text prompt that will be used to generate the images
#
#         Returns:
#         - Returns a list of direct image links to `.webp` images, from https://img.craiyon.com
#         """
#            
#         url = self.BASE_URL + self.DRAW_API_ENDPOINT
#         session = requests.Session()
#         resp = session.post(url, json={'prompt': prompt, "token": self.api_token, "version": self.model_version})
#        
#         resp = resp.json()
#                
#         # Add protocol, domain and subdomain (https://img.craiyon.com) to each item as those aren't included in the response by default
#         images = [f"https://img.craiyon.com/{item}" for item in resp['images']]
#        
#         return GeneratedImages(images, model="v2")
#    
#     # Generate images with v2, asynchronously
#     async def async_generate(self, prompt: str) -> GeneratedImages:
#        
#         """
#         Generates 9 images asynchronously using the v2 model of Craiyon.
#        
#         Arguments:
#         - (Required) | prompt: The text prompt that will be used to generate the images
#
#         Returns:
#         - Returns a list of direct image links to `.webp` images, from https://img.craiyon.com
#         """
#        
#         url = self.BASE_URL + self.DRAW_API_ENDPOINT
#         async with aiohttp.ClientSession() as sess:
#             async with sess.post(url, json={'prompt': prompt, "token": self.api_token, "version": self.model_version}) as resp:
#                 urls_no_domain = await resp.json()
#                 # Add protocol, domain and subdomain (https://img.craiyon.com) to each item as those aren't included in the response by default
#                 images = [f"https://img.craiyon.com/{item}" for item in urls_no_domain['images']]
#        
#                 return GeneratedImages(images, model="v2")
#


# v1 version of Craiyon API, for backwards compatibility
class CraiyonV1:
    '''
    **NOTICE**: This is the v1 version of Craiyon's model. To use the latest model, use the normal `Craiyon` class instead.
    
    Instantiates a Craiyon session, allows user to generate images from text prompts.
    The model takes some time to generate the images (roughly around 1 minute).
    So be patient, and don't abuse the api, as I am not the one hosting the model, craiyon itself is.
    '''
 
    def __init__(self) -> None:
        self.BASE_URL = "https://backend.craiyon.com"
        self.DRAW_API_ENDPOINT = "/generate"
    
    def generate(self, prompt: str) -> GeneratedImages:
        
        """
        Generates 9 images using the v1 model of Craiyon.
        
        Arguments:
        - (Required) | prompt: The text prompt that will be used to generate the images
        
        Returns:
        - Returns a list of 9 Base64 bytestrings (.jpg)
        """
        
        session = requests.Session()
        url = self.BASE_URL + self.DRAW_API_ENDPOINT
        resp = session.post(url, json={'prompt': prompt})
        return GeneratedImages(resp.json()['images'], model="v1")

    async def async_generate(self, prompt: str) -> GeneratedImages:
        
        """
        Generates 9 images asynchronously using the v1 model of Craiyon.
        
        Arguments:
        - (Required) | prompt: The text prompt that will be used to generate the images
        
        Returns:
        - Returns a list of 9 Base64 bytestrings (.jpg)
        """
        
        url = self.BASE_URL + self.DRAW_API_ENDPOINT
        async with aiohttp.ClientSession() as sess:
            async with sess.post(url, json={"prompt": prompt}) as resp:
                resp = await resp.json()
                return GeneratedImages(resp['images'], model="v1")
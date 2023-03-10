import base64
from pathlib import Path
import aiofiles
from aiopath import AsyncPath
import requests
import aiohttp


# Handles V2 version of Craiyon API
class GeneratedImagesV2:
    def __init__(self, imagelist: list):
        self.images = imagelist
        
    # Encode a list of Direct Image URLs to B64 Bytestrings
    def encode_base64(self, image_list: list):
        '''
        Takes a list of direct image URLs from https://img.craiyon.com, downloads each image, and encodes them into a bytes object using Base64 encoding
        
        Returns:
        - Returns a list of bytestring objects encoded with Base64
        '''
        
        b64_object_list = []
        
        for url in image_list:
            response = requests.get(url=url)
            if response.status_code == 200:
                # Convert image to bytes
                bytestring = base64.b64encode(response.content)
                b64_object_list.append(bytestring)
                
        return b64_object_list
    
    # Asynchronously encode a list of Direct Image URLs to B64 Bytestrings        
    async def async_encode_base64(self, image_list: list):
        '''
        Asynchronously takes a list of direct image URLs from https://img.craiyon.com, downloads each image, and encodes them into a bytes object using Base64 encoding
        
        Returns:
        - Returns a list of bytestring objects encoded with Base64
        '''
        
        b64_object_list = []
        
        for url in image_list:
            async with aiohttp.ClientSession() as sess:
                async with sess.get(url=url) as resp:
                    if resp.status == 200:
                        # Convert image to bytes
                        resp = await resp.read()
                        bytestring = base64.b64encode(resp)
                        b64_object_list.append(bytestring)
                        
        return b64_object_list
            
    
    # Save Images  
    def save_images(self, path: str=None):
        '''
        Saves the generated images to the given path.
        Defaults to cwd/generated
        
        Filetype saved: `.webp`
        '''
        
        # Get list of bytestring objects
        image_list = GeneratedImagesV2.encode_base64(self, self.images)
        # Make new directory
        path = (Path.cwd() / 'generated') if not path else Path(path)
        path.mkdir(parents=True, exist_ok=True)
        # Save each image to specified path
        for i in enumerate(image_list):
            with open(path / f'image-{i[0]+1}.webp', 'wb') as f:
                f.write(base64.decodebytes(i[1])) # Save file to disk
    
    # Async Save Images
    async def async_save_images(self, path: str=None):
        '''
        Asynchronously saves the generated images to the given path.
        Defaults to cwd/generated.
        
        Filetype saved: `.webp`
        '''
        
        # Get list of bytestring objects
        image_list = await GeneratedImagesV2.async_encode_base64(self, self.images)
        # Make new directory
        path = (AsyncPath.cwd() / 'generated') if not path else AsyncPath(path)
        await path.mkdir(parents=True, exist_ok=True)
        # Save each image to specified path
        for i in enumerate(image_list):
            async with aiofiles.open(path / f'image-{i[0]+1}.webp', 'wb') as f:
                await f.write(base64.decodebytes(i[1])) # Save file to disk


# Handles V1 version of Craiyon API
class GeneratedImagesV1:
    def __init__(self, images: dict):
        self.images = images
        
    def save_images(self, path: str=None):
        '''
        Saves the generated images to the given path.
        Defaults to cwd/generated
        
        Filetype saved: `.jpg`
        '''
        path = (Path.cwd() / 'generated') if not path else Path(path)
        path.mkdir(parents=True, exist_ok=True)
        for i in enumerate(self.images):
            with open(path / f'image-{i[0]+1}.jpg', 'wb') as f:
                f.write(base64.decodebytes(i[1].encode('utf-8')))
    
    async def async_save_images(self, path: str=None):
        '''
        Saves the generated images to the given path.
        Defaults to cwd/generated.
        
        Filetype saved: `.jpg`
        '''
        path = (AsyncPath.cwd() / 'generated') if not path else AsyncPath(path)
        await path.mkdir(parents=True, exist_ok=True)
        for i in enumerate(self.images):
            async with aiofiles.open(path / f'image-{i[0]+1}.jpg', 'wb') as f:
                await f.write(base64.decodebytes(i[1].encode('utf-8')))
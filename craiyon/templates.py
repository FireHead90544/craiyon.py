import base64
from pathlib import Path
import aiofiles
from aiopath import AsyncPath
from craiyon.craiyon_utils import encode_base64, async_encode_base64


# Handles V2 version of Craiyon API
class GeneratedImagesV2:
    def __init__(self, imagelist: list):
        self.images = imagelist
            
    
    # Save Images  
    def save_images(self, path: str=None):
        '''
        Saves the generated images to the given path.
        Defaults to cwd/generated
        
        Filetype saved: `.webp`
        '''
        
        # Get list of bytestring objects
        image_list = encode_base64(self.images)
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
        image_list = await async_encode_base64(self.images)
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
import base64
from pathlib import Path
import aiofiles
from aiopath import AsyncPath

class GeneratedImages:
    def __init__(self, images: dict):
        self.images = images
        
    def save_images(self, path: str=None):
        '''
        Saves the generated images to the given path.
        Defaults to cwd/generated
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
        '''
        path = (AsyncPath.cwd() / 'generated') if not path else AsyncPath(path)
        await path.mkdir(parents=True, exist_ok=True)
        for i in enumerate(self.images):
            async with aiofiles.open(path / f'image-{i[0]+1}.jpg', 'wb') as f:
                await f.write(base64.decodebytes(i[1].encode('utf-8')))
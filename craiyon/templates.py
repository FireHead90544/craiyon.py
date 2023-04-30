import base64
from pathlib import Path
import aiofiles
from aiopath import AsyncPath
from craiyon.craiyon_utils import encode_base64, async_encode_base64


# Handles the images returned from the Craiyon API
class GeneratedImages:
    def __init__(self, images: list, description: str = None, model: str = None):
        self.images = images
        self.description = description
        self.model = model

    def save_images(self, path: str = None):
        """
        Saves the generated images to the given path.
        Defaults to cwd/generated

        Filetype saved: `.jpg` for v1, '.webp' for v3
        """
        images = self.images
        extension = "jpg"
        if self.model in ["v2", "v3"]:
            images = encode_base64(self.images)
            extension = "webp"

        path = (Path.cwd() / "generated") if not path else Path(path)
        path.mkdir(parents=True, exist_ok=True)
        for i in enumerate(images):
            with open(path / f"image-{i[0]+1}.{extension}", "wb") as f:
                if self.model == "v1":
                    f.write(base64.decodebytes(i[1].encode("utf-8")))
                else:
                    f.write(base64.decodebytes(i[1]))

    async def async_save_images(self, path: str = None):
        """
        Saves the generated images to the given path.
        Defaults to cwd/generated.

        Filetype saved: `.jpg`
        """
        images = self.images
        extension = "jpg"
        if self.model in ["v2", "v3"]:
            images = await async_encode_base64(self.images)
            extension = "webp"

        path = (AsyncPath.cwd() / "generated") if not path else AsyncPath(path)
        await path.mkdir(parents=True, exist_ok=True)
        for i in enumerate(images):
            async with aiofiles.open(path / f"image-{i[0]+1}.{extension}", "wb") as f:
                if self.model == "v1":
                    await f.write(base64.decodebytes(i[1].encode("utf-8")))
                else:
                    await f.write(base64.decodebytes(i[1]))
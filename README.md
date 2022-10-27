
# craiyon.py

API Wrapper for [craiyon](https://craiyon.com) (formerly DAL-E-MINI) to generate awesome images from text tokens.

## Badges

Provided By: [shields.io](https://shields.io/)

[![PyPI Version](https://img.shields.io/pypi/v/craiyon.py?style=for-the-badge)](https://pypi.org/project/craiyon.py/)
[![PyPI Downloads](https://img.shields.io/pypi/dm/craiyon.py?color=red&style=for-the-badge)](https://pypi.org/project/craiyon.py/)
[![Apache License 2.0](https://img.shields.io/pypi/l/craiyon.py?color=lime&style=for-the-badge)](https://opensource.org/licenses/)
[![Connect On Discord](https://img.shields.io/discord/710909601356447805?color=yellow&style=for-the-badge)](https://discord.gg/dN66r3D)
[![Code Lines](https://img.shields.io/tokei/lines/github/FireHead90544/craiyon.py?color=orange&style=for-the-badge)](https://github.com/FireHead90544/craiyon.py)
[![Code Size](https://img.shields.io/github/languages/code-size/FireHead90544/craiyon.py?style=for-the-badge)](https://github.com/FireHead90544/craiyon.py)
[![Pull Requests](https://img.shields.io/github/issues-pr/FireHead90544/craiyon.py?style=for-the-badge)](https://github.com/FireHead90544/craiyon.py/pulls)
[![Issues](https://img.shields.io/github/issues/FireHead90544/craiyon.py?color=teal&style=for-the-badge)](https://github.com/FireHead90544/craiyon.py/issues)
[![Contributors](https://img.shields.io/github/contributors/FireHead90544/craiyon.py?style=for-the-badge)](https://github.com/FireHead90544/craiyon.py/graphs/contributors)

## Acknowledgements

 - [Issues](https://github.com/FireHead90544/craiyon.py/issues)
 - [Pull Requests](https://github.com/FireHead90544/craiyon.py/pulls)
 - [View Project On PyPI](https://pypi.org/project/craiyon.py/)

  
## Authors

- [@Rudransh Joshi](https://www.github.com/FireHead90544)

  
## Installation

The easiest way to install craiyon.py is using pip

```shell
  pip install -U craiyon.py
```

Or just manually clone the repository and build the wheel


## Usage / Examples

### 

**Generate and save the images**

```py
from craiyon import Craiyon

generator = Craiyon() # Instantiates the api wrapper
result = generator.generate("Photorealistic image of shrek eating earth")
result.save_images() # Saves the generated images to 'current working directory/generated', you can also provide a custom path
```
![image](https://user-images.githubusercontent.com/55452780/181876989-38872ca2-c3d5-4891-9bd4-cf4e4b26b91e.png)

**Use the images in your code without saving**

```py
from craiyon import Craiyon
from PIL import Image # pip install pillow
from io import BytesIO
import base64

generator = Craiyon() # Instantiates the api wrapper
result = generator.generate("Professional photo of Obama flashing a flag with his last name") # Generates 9 images by default and you cannot change that
images = result.images # A list containing image data as base64 encoded strings
for i in images:
    image = Image.open(BytesIO(base64.decodebytes(i.encode("utf-8"))))
    # Use the PIL's Image object as per your needs
```
![image](https://user-images.githubusercontent.com/55452780/181877028-740bee12-432d-4019-b74e-a17f53b79987.png)

## Async Usage/Examples

###

**Generate and save the images**

```py
from craiyon import Craiyon
import asyncio


async def main():
    generator = Craiyon() # Instantiates the api wrapper
    result = await generator.async_generate("Photorealistic image of shrek eating earth")
    await result.async_save_images() # Saves the generated images to 'current working directory/generated', you can also provide a custom path
    
asyncio.run(main)
```


## Todo

None!

## Contributing

Contributions are always welcome!

- Fork this repository.
- Make the changes in your forked repositry.
- Make sure to fetch upstream before generating a PR.
- Generate a pull request.

Please adhere to the GitHub's `code of conduct` for contributions and contributors.

  
## License

[Apache License 2.0](https://choosealicense.com/licenses/apache-2.0/)

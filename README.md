
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
- [@mdm9300404](https://github.com/mdm9300404)
  
## Installation

The easiest way to install craiyon.py is using pip

```shell
  pip install -U craiyon.py
```

Or just manually clone the repository and build the wheel

## Versioning

The api wrapper has separate classes revolving around each model, i.e, the Craiyon v1 and v3.
The v2 model has been removed from the api, so the model class around it is also deprecated by commenting it out.
A quick comparison is given below:

| Model | Speed | Quality | API_URL | Import Name |
|:-----:|:-----:|:-------:|:-------:|:-----------:|
| v3 | Fast (~50s) | Best | https://api.craiyon.com/v3 | Craiyon |
| v2 (Removed) | Fastest (<45s) | Good | https://api.craiyon.com/draw | CraiyonV2 |
| v1 | Slow (~1m) | Average | https://backend.craiyon.com/generate | CraiyonV1 |


## Usage / Examples

### 

**Generate and save the images**

```py
from craiyon import Craiyon

generator = Craiyon() # Instantiates the api wrapper
result = generator.generate("Photorealistic image of shrek eating earth", negative_prompt="spoon", model_type="art")
print(result.description) # Description about the generated images # >>> Shrek devouring planet Earth with a sinister grin
result.save_images() # Saves the generated images to 'current working directory/generated', you can also provide a custom path
```
![image](https://user-images.githubusercontent.com/55452780/235368810-bbeda283-d0d5-43b4-a1af-d5fdeab7cadb.png)

**Use the images in your code without saving**

```py
from craiyon import Craiyon, craiyon_utils
from PIL import Image # pip install pillow
from io import BytesIO
import base64

generator = Craiyon() # Instantiates the api wrapper
result = generator.generate("Professional photo of Obama flashing a flag with his last name") # Generates 9 images by default and you cannot change that
print(result.description) # >>> Obama holding up a flag with his last name, smiling confidently
images = craiyon_utils.encode_base64(result.images)
for i in images:
    image = Image.open(BytesIO(base64.decodebytes(i)))
    # To convert the .webp images to .jpg or .png, you can proceed like this
    # image.convert("RGB").save("image.jpg", "JPEG") # For ".jpg" images
    # image.convert("RGBA").save("image.png", "PNG") # For ".png" images
    
    # Use the PIL's Image object as per your needs
```
![image](https://user-images.githubusercontent.com/55452780/235368949-05e4d215-5f29-4aea-a059-e6ad62b1ee2c.png)

**Just get the Direct Image URLs**
```py
from craiyon import Craiyon

generator = Craiyon() # Instantiates the api wrapper
result = generator.generate("Photorealistic image of shrek eating earth")

print(result.images) # Prints a list of the Direct Image URLs hosted on https://img.craiyon.com

# Loops through the list and prints each image URL one by one
for url in result.images:
    print(url)
```

## Async Usage / Examples

###

**Generate and save the images**

```py
from craiyon import Craiyon
import asyncio


async def main():
    generator = Craiyon() # Instantiates the api wrapper
    result = await generator.async_generate("Photorealistic image of shrek eating earth")
    await result.async_save_images() # Saves the generated images to 'current working directory/generated', you can also provide a custom path
    
asyncio.run(main())
```



**Use with a Discord bot**
```py
from craiyon import Craiyon, craiyon_utils
import discord
from discord.ext import commands
from io import BytesIO
import base64

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(intents = intents, command_prefix="!")

generator = Craiyon() # Initialize Craiyon() class

@bot.event
async def on_ready():
    print(f"Successfully logged in as {bot.user.name}!")

# Create command
@bot.command()
async def genimage(ctx, *, prompt: str):
    await ctx.send(f"Generating prompt \"{prompt}\"...")
    
    generated_images = await generator.async_generate(prompt) # Generate images
    b64_list = await craiyon_utils.async_encode_base64(generated_images.images) # Download images from https://img.craiyon.com and store them as b64 bytestring object
    
    images1 = []
    for index, image in enumerate(b64_list): # Loop through b64_list, keeping track of the index
        img_bytes = BytesIO(base64.b64decode(image)) # Decode the image and store it as a bytes object
        image = discord.File(img_bytes)
        image.filename = f"result{index}.webp"
        images1.append(image) # Add the image to the images1 list
        
    await ctx.reply(files=images1) # Reply to the user with all 9 images in 1 message
        

bot.run("your_token_here")
```

## Generation parameters

```py
# These parameters are only supported by the v3 model
from craiyon import Craiyon
generator = Craiyon()
result = generator.generate("prompt here", negative_prompt="cap", model_type="art") # The negative prompt and model type are optional parameters
# Negative prompt helps filtering out certain things from the images that will be generated, defaults to empty string ""
# Model type can be "art", "drawing", "photo" and "none", defaults to "none". It does as it's name suggests.

# result.description returns a brief description generated by craiyon about the generated images
# result.images returns the list of images generated (v3 returns the image links, v1 returns the base64 image data)
# result.model returns the model version
```

## Specify custom tokens/model versions

```py

from craiyon import Craiyon # Importing the v3 model

# api_token and model_version are not required, but recommended
generator = Craiyon(api_token="your-token-here", model_version="api-model-version")

# ...rest is the same stuff as above
```

### api_token
* If you bought a paid subscription to Craiyon.com, you would know that the watermark is removed. If you wish to have the watermark removed from the generated images in your application as well, you can specify a token here. 
* To find your token: Open Google Chrome, go to craiyon.com (make sure you're logged in), Press F12, go to the Network tab, make sure the record button looks like a red circle at the top-left. Put your prompt in the text box and press the orange "Draw" button. Two "draw" items should appear on the left, under "name". One of them will have a "Payload" tab next to "Headers" and "Preview", as well as above "General". Click it, and your token is listed there.

### model_version
* Since Craiyon is still training their V2 model, it is improving every day. We recommend putting your own model version here to get the newest and best model they have at the moment.
* To get the model version, follow the steps for the api_token listed above, except copy the "version" instead of the "token". Then, just pass it in as an argument while instantiating the `Craiyon` class and you're ready!
* While this is recommended, it is not required. If you do not pass a custom model version, this value will automatically default to "35s5hfwn9n78gb06", which is Craiyon's newest model as of March 10, 2023.

## Backwards Compatibility
This library is fully backwards-compatible with older versions.

If you were previously using this library before we added support for Craiyon's V3 model and you wish to continue using the old V1 model, simply change the name of the class `Craiyon` to `CraiyonV1`! Otherwise, you can update your application to the V3 model by reading the code samples above. Please note that the v2 model used to work earlier, but Craiyon completely removed their v2 model from the api and there are no traces of it left, so we currently removed the CraiyonV2 class. Please use either the v1 or v3 model instead.


## Todo

- Implement: Upscale
- Fix: v3 Breaking (Urgent)
Please wait for around 3-4 days before the updates can be pushed for these.

## Contributing

Contributions are always welcome!

- Fork this repository.
- Make the changes in your forked repositry.
- Make sure to fetch upstream before generating a PR.
- Generate a pull request.

Please adhere to the GitHub's `code of conduct` for contributions and contributors.

  
## License

[Apache License 2.0](https://choosealicense.com/licenses/apache-2.0/)

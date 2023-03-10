import requests
import aiohttp
import base64


# Encode a list of Direct Image URLs to B64 Bytestrings
def encode_base64(image_list: list):
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
async def async_encode_base64(image_list: list):
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
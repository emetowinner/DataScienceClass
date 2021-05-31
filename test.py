import requests

url = "https://microsoft-computer-vision3.p.rapidapi.com/analyze"

querystring = {"language":"en","descriptionExclude":"Celebrities","visualFeatures":"ImageType","details":"Celebrities"}

payload = "{\r\n    \"url\": \"http://example.com/images/test.jpg\"\r\n}"
headers = {
    'content-type': "application/json",
    'x-rapidapi-key': "dacaae5850mshbcab4ca9a7b2a4dp13a15bjsnd9aaa23a2ee4",
    'x-rapidapi-host': "microsoft-computer-vision3.p.rapidapi.com"
    }

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

print(response.text)
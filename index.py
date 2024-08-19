import requests
from PIL import Image
from io import BytesIO

url = "https://api.thecatapi.com/v1/images/search"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    image_url = data[0]['url']
    
    image_response = requests.get(image_url)
    
    img = Image.open(BytesIO(image_response.content))
    img.show()

else:
    print(f"Erro ao acessar a API: {response.status_code}")
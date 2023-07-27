import requests
import random
from pathlib import Path

response = requests.get(f'https://api.dicebear.com/api/male/{random.random()}.svg')

Path('./avatars').mkdir(exist_ok=True)

with open('./avatars/javatar.svg', 'wb') as file:
    file.write(response.content)

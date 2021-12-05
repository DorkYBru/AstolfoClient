import requests
import os
url = 'https://www.facebook.com/favicon.ico'
r = requests.get(url, allow_redirects=True)

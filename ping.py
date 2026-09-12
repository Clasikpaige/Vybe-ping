import requests

URL = "https://e-sound-686q.onrender.com/"

response = requests.get(URL, timeout=30)

print(f"Status: {response.status_code}")
print(f"Response: {response.text}")

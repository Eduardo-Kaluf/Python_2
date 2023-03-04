import requests as re

params = {
    "regiao": 1,
    "marca": "Renault",
    "preco": "1000-2000"
}
response = re.get("https://www.httpbin.org/post", params=params)

print("HTTP Status -> ", response.status_code)
print("Texto -> ", response.text)
#print("Json ->", response.json())
#print("Json ->", response.json()["headers"]["Host"])
print("Header -> ", response.headers)

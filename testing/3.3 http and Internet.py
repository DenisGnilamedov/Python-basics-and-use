import requests

'''
res = requests.get("https://docs.python.org/3.5/")
print(res.status_code) # 200
print(res.headers['Content-Type']) # text/html
print(res.content) # содержимое
print(res.text)


res_image = requests.get("https://docs.python.org/3.5/_static/py.png")

with open("python.png", "wb") as f:
    f.write(res_image.content) # получить картинку по ссылке и сохранить у себя
'''

res_google = requests.get("https://google.com/search",
                          params={"q": "Python"})

print(res_google.url)
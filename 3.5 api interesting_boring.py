import requests


with open(r'C:\1\dataset_24476_3.txt') as f:
    for i in f:
        num = i.strip()
        api_url = "http://numbersapi.com/" + str(num) + "/math"
        params = {'json': 'true'}
        res = requests.get(api_url, params=params)
        data = res.json()
        if data["type"]:
            print('Interesting')
        else:
            print('Boring')



import requests

muscle = 'abdominals'
api_url = 'https://api.api-ninjas.com/v1/exercises?muscle={}'.format(muscle)
response = requests.get(api_url, headers={'X-Api-Key': 'Ttsv3RpRNd3ryR7qjw+HEQ==NnZkMEKMv7hyYevy'})
if response.status_code == requests.codes.ok:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)
import requests

# post request with token and github repo using json
r = requests.post('http://challenge.code2040.org/api/register', data = {'token': 'e33fa7ab36fcb87205d5f9feb1cad3cb',
'github': 'https://github.com/Shameemah/Code-2040'})
r.text

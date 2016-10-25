import requests

r = requests.post('http://challenge.code2040.org/api/haystack', data = {'token': 'e33fa7ab36fcb87205d5f9feb1cad3cb'})
#receiving json info
info = r.json()
haystack = info['haystack']
needle = info['needle']

#find index of needle
index = haystack.index(needle)

#send index back to server
r = requests.post('http://challenge.code2040.org/api/haystack/validate', data = {'token': 'e33fa7ab36fcb87205d5f9feb1cad3cb', 'needle': index})
r.text

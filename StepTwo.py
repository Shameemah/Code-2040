import requests

#receiving string from endpoint
r = requests.post('http://challenge.code2040.org/api/reverse', data = {'token': 'e33fa7ab36fcb87205d5f9feb1cad3cb'})
# string received from the server
string = r.text
#reversing the string
revString = string[::-1]
#posting reversed string back to end point
r = requests.post('http://challenge.code2040.org/api/reverse/validate', data = {'token': 'e33fa7ab36fcb87205d5f9feb1cad3cb', 'string': revString})

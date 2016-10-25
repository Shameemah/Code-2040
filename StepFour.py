import requests

r = requests.post('http://challenge.code2040.org/api/prefix', data = {'token': 'e33fa7ab36fcb87205d5f9feb1cad3cb'})

#receiving json info
info = r.json()
array = info['array']
prefix = info['prefix']
myArray = []

#find strings with prefix
for index in range(len(array)):
    if array[index].startswith(prefix):
        index += 1
    else:
        myArray.append(array[index])
        print myArray

#send dictionary back to server
r = requests.post('http://challenge.code2040.org/api/prefix/validate', json = {'token': 'e33fa7ab36fcb87205d5f9feb1cad3cb', 'array': myArray})
print r.text

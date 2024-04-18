from requests import put, get
print(put('http://localhost:5000/user/todo1', data={'data': 'A_Remember the milk'}).json())
#{u'todo1': u'Remember the milk'}

print(get('http://localhost:5000/user/todo1').json())
#{u'todo1': u'Remember the milk'}
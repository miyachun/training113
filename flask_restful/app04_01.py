from requests import put, get
print(put('http://localhost:5000/todo1', data={'data': 'A_Remember the milk'}).json())
#{u'todo1': u'Remember the milk'}

print(get('http://localhost:5000/todo1').json())
#{u'todo1': u'Remember the milk'}



print(get('http://localhost:5000/').json())
print(get('http://localhost:5000/a').json())
print(get('http://localhost:5000/b').json())


#put('http://localhost:5000/todo2', data={'data': 'Change my brakepads'}).json()
#{u'todo2': u'Change my brakepads'}
#get('http://localhost:5000/todo2').json()
#{u'todo2': u'Change my brakepads'}
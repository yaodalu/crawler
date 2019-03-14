import json

jsonStr = '{"name":"yl","age":"18","hobby":["eat","sleep"]}'
print(type(jsonStr))

jsonData = json.loads(jsonStr)
print(jsonData["name"])
print(type(jsonData))
print(jsonData["name"])
'''
>>> 
<class 'str'>
yl
<class 'dict'>
yl
>>> 
'''

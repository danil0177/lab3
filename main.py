import json

data = ['Test data',{'Structure':'Any'}]
s = json.dumps(data)
print(s)

print(json.loads(s))
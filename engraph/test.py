import json

datadict = {10:100,100:1000,1000:5000}
obj = json.JSONEncoder().encode(datadict)

print obj

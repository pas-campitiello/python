import json

x = [1, 'simple', 'list', ('aa','bb')]
print(json.dumps(x))

f = open("contentfile.txt", "w")
# note json.dump not dumps
json.dump(x,f)
f.close()

f = open("contentfile.txt", "r")
readContent = json.load(f)
f.close()

print(readContent)

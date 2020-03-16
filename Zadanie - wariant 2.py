import requests
import json
import urllib.request

print('##########')
print('Punkt 1')
print('##########')

with urllib.request.urlopen("https://jsonplaceholder.typicode.com/posts") as posts:
    data1 = json.loads(posts.read().decode())
    print(data1)
    #response = requests.get('https://jsonplaceholder.typicode.com/posts')
    #print(response.text)


with urllib.request.urlopen("https://jsonplaceholder.typicode.com/users") as users:
    data2 = json.loads(users.read().decode())
    print(data2)
    #response = requests.get('https://jsonplaceholder.typicode.com/users')
    #print(response.text)

'''
#inny sposob
posts = 'https://jsonplaceholder.typicode.com/posts'
response = requests.get(posts)
print(response.ok)
print(response.status_code)
print(response.text)

users = 'http://jsonplaceholder.typicode.com/users'
response = requests.get(users)
print(response.ok)
print(response.status_code)
print(response.text)
'''

solditems = requests.get('https://jsonplaceholder.typicode.com/posts') # (your url)
data1 = solditems.json()
with open('data1.json', 'w') as f:
    json.dump(data1, f)

solditems = requests.get('https://jsonplaceholder.typicode.com/users') # (your url)
data2 = solditems.json()
with open('data2.json', 'w') as f:
    json.dump(data2, f)


#?
data1, data2 = json.dumps(data1, sort_keys=True), json.dumps(data2, sort_keys=True)
data1 == data2 # a normal string comparison


a = json.load(open("data1.json"))
b = json.load(open("data2.json"))

final = []

for element in b:
    isThere = False
    for element2 in a:
        if element['id'] == element2["userId"]:
            element2.update(element)
            final.append(element2)
            isThere = True
    if not isThere:
        final.append(element)

with open('final.json', 'w') as f:
    json.dump(final, f)
    #json = json.dumps(final)

print('##########')
print('Punkt 2')
print('##########')
      
from collections import Counter

with open('final.json') as f:
    j = json.load(f)
    c = Counter(player['username'] for player in j)
#print(c)

'''
#inny sposob
from pprint import pprint as pp
c = dict(c)
pp(c)'''

for k, v in c.items():
    print("{} napisal(a) {} postow".format(k, v))

print('##########')
print('Punkt 3')
print('##########')

import collections

with open('final.json') as f:
    content = json.load(f)

#pierwszy sposob
values=[]
for item in content:
    if item not in values:
        values.append(item['title'])
print(set(values))

#drugi sposob
values = set()
for item in content:
    values.add(item['title'])
print(values)

def unique(A): 
   # intilize a null list 
   uniquevalues = [] 
      
   # traversing the list 
   for i in A: 
      # check unique valueis present or not 
      if i not in uniquevalues: 
         uniquevalues.append(i) 
   # print (A) 
   for i in uniquevalues: 
      print (i)

unique(values)

#trzeci sposob
seen = set()
uniq = [x for x in values if x not in seen and not seen.add(x)]
print(uniq)
print(" ")
seen = {}
dupes = []

for x in values:
    if x not in seen:
        seen[x] = 1
    else:
        if seen[x] == 1:
            dupes.append(x)
        seen[x] += 1

print(seen)

print('Sprawdzanie czy wartosci nie sa unikalne')
def duplicate_existence(lst):
	if len(lst) == len(set(lst)):
		return False
	return True
print(duplicate_existence(values))

print('Sprawdzanie czy wartosci sa unikalne')
def duplicate_existence(lst):
	if len(lst) != len(set(lst)):
		return False
	return True
print(duplicate_existence(values))

with open('resultsnew.json', 'w') as f:
    # json cant serialize sets hence conversion to list
    json.dump(list(values), f)

print('##########')
print('Punkt 4')
print('##########')

import sys
import re
from math import sin, cos, sqrt, asin, atan2, radians

def haversine(lat1, lon1, lat2, lon2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    # Radius of earth in kilometers is 6371
    km = 6371* c
    return km
    #print(km + "km")

input_file = open('data2.json')
data = json.load(input_file)  # get the data list
result = []
for element in data:  # iterate on each element of the list
    # element is a dict
    id0 = int(element['id'])
    id1 = float(element['address']['geo']['lat'])  # get the id
    id2 = float(element['address']['geo']['lng'])
    id01=id1
    id02=id2
    print('Latitude: ' + str(id0) + ' ' + element['name'])
    print(id1)  # print it
    print('Longitude: '+ str(id0) + ' ' + element['name'])
    print(id2)  # print it
    #result.append((id0, id1, id2))
    result.append((id1, id2))
    haversine(id1,id2, id01,id02)
print(result)

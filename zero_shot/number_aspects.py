import json 
  
# Opening JSON file 
f = open('zero-shot-blue.json',) 
  
# returns JSON object as  
# a dictionary 
data = json.load(f) 

aspects=set()

for i in data:
    for j in data[i]:
        if j!='none':
            aspects.add(j)

aspects_index = {}

for i,j in enumerate(aspects):
    aspects_index[j]=i



print(aspects_index)

cleaned_data= {}

for i in data:
    cleaned_data[i]={}
    for j in aspects:
        if j in data[i]:
            cleaned_data[i][aspects_index[j]] = data[i][j]
        else:
            cleaned_data[i][aspects_index[j]] = []

for i in cleaned_data:
    print(cleaned_data[i])
    break


with open('zero-shot-sent-cluster-blue.json', 'w') as outfile:
    json.dump(cleaned_data, outfile)
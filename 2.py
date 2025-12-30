
dict1 = {'ten': 10, 'twenty': 20, 'thirty': 30}
dict2 = {'sixty': 30, 'forty': 40, 'fifty': 50}
for i in (dict2):
    if dict2[i] not in dict1.values():
        dict1[i]=dict2[i]

print(dict1)
# This contains five different ways to swap keys and values in a dictionary

from collections import defaultdict

dict1 = {"a" : 1, "b" : 2, "c" : 2}
dict2 = {}

for k, v in dict1.items():
    if v in dict2:
        dict2[v].append(k)
    else:
        dict2[v] = [k]

print (dict2)

print ("\n2nd Way\n")

new_dict = dict([(v, [k for k, v1 in dict1.items() if v1 == v]) for v in set(dict1.values())])

print (new_dict)

print ("\n3rd Way\n")

dict2 = {}

for i in dict1:
    dict2.setdefault(dict1[i], []).append(i)
    
print (dict2)

print ("\n4th Way\n")

dict2 = {}

for k, v in dict1.items():
    dict2[v] = dict2.get(v, []) + [k]
    
print (dict2)

print ("\n5th Way\n")
    
dictresult = defaultdict(list)

{dictresult[v].append(k) for k, v in dict1.items()}

print (dict(dictresult))
#highest,lowest,average marks of studetns

'''students = {
    'rahul':78,
    'nani':95,
    'anjali':88,
    'vijay':67
}

max_scorer = max(students.values())
low_scorer = min(students.values())
average_score = sum(students.values())/len(students)

print(max_scorer,low_scorer,average_score)
m = float('-inf')
key=None
for k,v in students.items():
    if v>m:
        m=v
        key=k
print(key)'''

#count frequency of words in sentence
'''x = 'python is easy python is powerful'.split()

res = {}
for word in x:
    if word in res:
        res[word] =res[word]+1
    else:
        res[word] = 1
print(res)'''

#reverse keys and values
'''student = {
    'a':101,
    'b':102,
    'c':103
}

res = {}
for k,v in student.items():
    res[v] = k

print(res)'''

#convert to list into dictionary
'''l1 = ['name','age','city']
l2 = ['rahul',22,'hyd']
res={}
for k,v in zip(l1,l2):
    res[k] = v
print(res)'''

#sort dictionary by values
'''students = {
    'rahul':78,
    'nani':95,
    'anjali':88,
    'vijay':67
}'''
'''values = sorted(students.values())
res = {}
for val in values:
    for k,v in students.items():
        if val==v:
            res[k]=v
print(res)'''
#secone method
'''lst = list(students.items())
for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i][1]<lst[j][1]:
            lst[i],lst[j] = lst[j],lst[i]
print(dict(lst))'''
#duplicate values
'''data = {
    'a':10,
    'b':20,
    'c':10,
    'd':30,
    'e':20
}
values = list(data.values())
res = set()
for val in values:
    if values.count(val)>1:
        if val not in res:
            res.add(val)
print(res)'''

#group words by starting letter
'''words = ['apple','ant','ball','bat','cat','car']
res = {}
for word in words:
    if word[0] in res:
        res[word[0]].append(word)
    else:
        res[word[0]] = [word]
print(res)'''

#second highest marks
'''students = {
    'a':80,
    'b':95,
    'c':88,
    'd':91,
    'e':75
}'''

'''marks = list(students.values())
f = float('-inf')
s = float('-inf')
for mark in marks:
    if mark>f:
        s = f
        f = mark
    if mark<f and mark>s:
        s = mark
print(s)'''

#merge dictionaries

'''d1 = {
    'a':10,
    'b':20,
    'c':30
}
d2 = {
    'b':15,
    'c':25,
    'd':40
}
res = {}
lst = list(d1.items())+list(d2.items())
for k,v in lst:
    if k in res:
        res[k] = res[k]+v
    else:
        res[k] = v
print(res)'''

#grade calculator
students = {
    'ram':95,
    'rahul':82,
    'kiran':74,
    'anjali':65,
    'vijay':45
}

# values = list(students.values())
'''res = {}
for k,v in students.items():
    if v>90:
        res[k]='A'
    elif v>80:
        res[k]='B'
    elif v>70:
        res[k] = 'C'
    elif v>60:
        res[k]='D'
    else:
        res[k] = 'F'
print(res)'''

#reverse dictionary with duplicate values
'''data = {
    'a':10,
    'b':20,
    'c':10,
    'd':20
}

res = {}
for k,v in data.items():
    if v in res:
        res[v].append(k)
    else:
        res[v]=[k]
print(res)'''

#merge students attendace
'''day1 = {'ram':1,'rahul':1,'anjali':1}
day2 = {'rahul':1,'kiran':1,'ram':1}
lst = list(day1.items()) + list(day2.items())

res = {}
for k,v in lst:
    if k in res:
        res[k] = res[k]+v
    else:
        res[k]=v
print(res)'''




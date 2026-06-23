#findout duplicate and unique users count
'''obj = {'user_count':0,'duplicate_users':[],'unique_users':[]}
users = input('enter input: ').split()

for user in users:
    if users.count(user)>1:
        if user not in obj['duplicate_users']:
            obj['duplicate_users'].append(user)
    if user not in obj['unique_users']:
        obj['unique_users'].append(user)

print(obj['duplicate_users'])
print(len(obj['unique_users']))'''


#same as above question
'''def check_occurences(log):
    obj={'user_count':0,'duplicate_users':[],'unique_users':[],'more_than_three':[]}
    for user in log:
        if log.count(user)>1:
            if user not in obj['duplicate_users']:
                obj['duplicate_users'].append(user)
        if user not in obj['unique_users']:
            obj['unique_users'].append(user)
        
        if log.count(user)>3:
            if user not in obj['more_than_three']:
                obj['more_than_three'].append(user)
        
    print(obj['duplicate_users'])
    print(len(obj['unique_users']))
    print(obj['more_than_three'])
def login_activity():
    n = int(input('How many inputs you want: '))
    lst=[]
    for i in range(n):
        ip = input('Enter ip address: ')
        lst.append(ip)
    
    check_occurences(lst)

login_activity()'''

#employee attendace system
'''x = input().split(' ')
print(len(x))
unique_emp = set(x)
dpl_emp=[]
for emp in unique_emp:
    if x.count(emp)>1:
        dpl_emp.append(emp)
print(dpl_emp)
print(unique_emp)'''

#hospital management
'''x = input('enter patients ids: ').split()
target = input('enter searchable: ')
print('unique patients: ',set(x))
print('unique patient count: ',len(set(x)))
print(target in set(x))'''

#inventory management
'''n = int(input('enter how many inputs: '))
products = []
for i in range(n):
    p = tuple(input('enter product quantity: ').split(' '))
    products.append(p)

oos=[]
q=0
max_prd=''
qty=0
for p in products:
    # print(p[1])
    if p[1]=='0':
        oos.append(p)
    if int(p[1])>q:
        q=int(p[1])
        max_prd=p[0]
    qty+=int(p[1])

print(oos)
print(max_prd)
print(qty)'''

#rotate list by k positions
'''x = [1,2,3,4,5]
k=2
i = k%len(x)
if k%len(x)==0:
    print(x)
else:
    lst=[]
    print(x[-k:]+x[:-k])'''


#find the leader to right
'''x = [16,17,4,3,5,2]
leader = set()
for i in range(len(x)):
    m = max(x[i:])
    leader.add(m)
print(list(leader))'''

#three numbers sum equals k
x = [1,4,45,6,10,8]
k = 22
n=len(x)
# for i in range(n-2):
#     s=i+1
#     e=n-1
#     while s<e:
#         s=x[i]+x[s]+x[e]
#         if s==k:
#             print(i,s,e)
#         elif s<k:
#             s+=1
#         else:
#             e-=1


output = [[]]

for i in x:
    test = []
    for j in output:
        test.append(j+[i])
    for sub in test:
        if len(sub)==3:
            if sum(sub)==k:
                print(tuple(sub))
    # if sum(res)==k:
    #     print(res)
    output.extend(test)
# print(output)
    










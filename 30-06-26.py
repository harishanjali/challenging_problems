#vowels, consonents count
'''vowels=0
consonants = 0
x = 'Programming'.lower()

for char in x:
    if char in {'a','e','i','o','u'}:
        vowels+=1
    else:
        consonants+=1

print('Vowels: ',vowels)
print('Consonants: ',consonants)'''

#reverse a given string
'''x = 'python'
x = list(x)
s=0
e=len(x)-1
while s<e:
    x[s],x[e]=x[e],x[s]
    s+=1
    e-=1
print(''.join(x))'''

#string palidrome
'''x = 'racecar'
if x[::-1]==x:
    print('Palindrome')
else:
    print('Not a palindrome')'''

#remove duplicates from a string
'''x = 'programming'
org = set()
res=''
for char in x:
    if char not in org:
        org.add(char)
        res+=char
print(res)'''

#longest word in sentence
'''x = 'python is a powerful programming language'
res = ''
m=0
for word in x.split(' '):
    if len(word)>m:
        m=len(word)
        res=word
print(res)'''

#anagrams
'''a = 'silent'
b = 'listen'

if len(set(a)^set(b))==0:
    print('anagrams')
else:
    print('not anagram')'''

#replace spaces with hifens
'''x = 'python is easy'
res = '-'.join(x.split(' '))
print(res)'''

#count uppercase,lowercase,digits,special characters
'''x = 'PyThOn@123'
res={'upper':0,'lower':0,'digits':0,'special':0}
for char in x:
    if char.isalpha() and (char==char.upper()):
        res['upper']+=1
    elif char.isalpha() and (char==char.lower()):
        res['lower']+=1
    elif char.isdigit():
        res['digits']+=1
    else:
        res['special']+=1
print(res)'''

#compress string by counting consecutive repeated chars
'''x = 'abbccccdd'
res=''
c=1
for i in range(len(x)-1):
    if x[i]==x[i+1]:
        c+=1
    else:
        res+= x[i]+str(c)
        c=1
else:
    res+=x[i]+str(c)
print(res)'''

#find the largest number among three numbers
'''x = list(map(int,input().split(' ')))
res = max(x)
print('largest_num: ',res)'''

#factorial of a numbers
'''def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
res = fact(5)
print(res)'''

#check whether number is prime or not
'''def is_prime(n):
    if n<2:
        return False
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    else:
        return True
    
res = is_prime(4)
print(res)'''

#sum of all numbers in alist
'''x = [2,5,8,9,12]
x = [i for i in x if i%2==0]
print(sum(x))'''

#second largest number in a list
'''x = [10,50,20,90,40,-1,-2]
s = float('-inf')
f = float('-inf')
for num in x:
    if num>f:
        s = f
        f = num
    if num<f and num>f:
        s = num
print(s)'''

#remove duplicates from a list
'''x = [1,2,2,3,3,4,4,5]
print(list(set(x)))'''

#get output without using the external libraries or functions
x = '    Python Programming 2026 is Awesome!! Python is Easy. 123'
#remove extra spaces
# print(len(x))
def trim_string(x):
    s = 0
    e = len(x)-1
    for i in range(len(x)):
        if x[i]!=' ':
            s = i
            break
    for i in range(len(x)-1,0,-1):
        if x[i]!=' ':
            e = i
            break
    return x[s:e+1]
org_str = trim_string(x)
# print('without spaces: ',org_str)

def to_upper_lower(string):
    upper = ''
    lower = ''
    for char in string:
        if ord(char)>96 and ord(char)<123:
            upper+=chr(ord(char)-32)
        else:
            upper+=char
        if ord(char)>64 and ord(char)<92:
            lower+=chr(ord(char)+32)
        else:
            lower+=char
        
    return upper,lower

# print(to_upper_lower(org_str))

def title_case(x):
    res=''
    for i in range(len(x)):
        if i==0:
            res+=x[i].upper()
        elif x[i]==' ':
            res+= ' '
            res+=x[i+1].upper()
        else:
            if x[i-1]!=' ':
                res+=x[i]
        

    return res

res = title_case(org_str)
# print(res)

#swapcase
def swap_case(x):
    res=''
    for char in x:
        if ord(char)>64 and ord(char)<92:
            res+=chr(ord(char)+32)
        elif ord(char)>96 and ord(char)<123:
            res+=chr(ord(char)-32)
        else:
            res+=char
    return res

res = swap_case(org_str)
# print(res)


def vowels_count(x):
    vowels = {'a','e','i','o','u'}
    c=0
    for char in x:
        if char.lower() in vowels:
            c+=1

    return c

res = vowels_count(org_str)
# print(res)

def digit_count(x):
    c=0
    digits = {str(i) for i in range(10)}
    for char in x:
        if char in digits:
            c+=1
    return c

res = digit_count(org_str)
# print(res)

def is_alphabet(x):
    c=0
    for char in x:
       if ord(char)>64 and ord(char)<92:
            c+=1
       elif ord(char)>96 and ord(char)<123:
            c+=1

    return c

res = is_alphabet(org_str)
# print(res)
def is_special(x):
    c=0
    for char in x:
        if ord(char)>31 and ord(char)<48:
            c+=1
    return c

res = is_special(org_str)
print(res)





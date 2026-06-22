#a theatre has n rows, the first row contains 1 seat,the 
# second row contains 2 seats, and so on , print the seating arrangement using *

'''n = int(input('Enter n number of rows: '))

for i in range(1,n+1):
    print('*'*i)'''

'''n = int(input('ENter no of floors: '))
for i in range(n):
    s = ''
    for j in range(1,n-i+1):
        s+= str(j)
    print(s)'''

#a tourism app displays a mountain where the peak is centered
n = int(input('enter no of rows: '))

#a cricket stadium has rows of seats, odd numbered rows are filled with 1s and even number are filled with 0s
'''n = int(input('Enter no of rows: '))
for i in range(1,n+1):
    if i%2==0:
        print('0'*i)
    else:
        print('1'*i)'''

#a warehouse stores boxes in a square formation.only the boundary contains boxes
'''n = int(input('enter no of rows: '))
for i in range(1,n+1):
    if i==1 or i==n:
        print('*'*n)
    else:
        print('*'+' '*(n-2)+'*')'''

#an elevator displays floor numbers in ascending order and then descending order
'''n = int(input('Enter no of floors: '))
end = n//2+1
for i in range(1,n+1):
    string=''
    if i>n//2+1:
        for j in range(1,end-1+1):
            string+=str(j)
        end-=1
    else:
        for j in range(1,i+1):
            string+= str(j)
    print(string)'''

#a snake moves left to tight in one row and right to left in the next row.
'''n = int(input('enter no of rows: '))
for i in range(1,n+1):
    s = ''
    for j in range(1,i+1):
        s+=str(j)
    if i%2==0:
        s = s[::-1]
    print(s)'''

#record temperatures for n days and find the average temperature
'''n = int(input('Enter n days: '))
avg=None
s=0
for i in range(n):
    u = int(input('enter temperature: '))
    s+=u

print(s/n)'''

'''user_input = input('enter input: ').split(' ')
c=0
s=0
for d in user_input:
    if d=='0':
        c+=1
    else:
        s = c
        c = 0
print(s)'''

'''x = list(map(int,input('enter data: ').split(' ')))
c=0
for n in x:
    if c==3:
        print('Alert')
        break
    if n%2==0:
        c+=1
    else:
        c=0'''

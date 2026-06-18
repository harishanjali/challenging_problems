
#a parking lot records vehicles entering and exitting
#print the maximum vehicles present at any time
'''in_count = 0
out_count = 0
for i in range(int(input('Enter number: '))):
    action = input('Enter(IN/OUT): ')
    if action=='IN':
        in_count+=1
    else:
        out_count+=1

if out_count>in_count:
    print('invalid inputs')
else:
    print(in_count-out_count)'''

#elevator problem
#print total floors travelled
'''floor_count=0
current_floor=0
for i in range(int(input('Enter number: '))):
    floor = int(input('Enter floor: '))
    if floor>current_floor:
        floor_count += floor-current_floor
    else:
        floor_count += current_floor-floor
    
    current_floor = floor

print(floor_count)'''

#calculate boundaries,scoe,dot balls
'''user_input = list(map(int,input('enter ball by ball runs: ').split(' ')))
boundaries = 0
total_score=0
dot_balls = 0
for ball in user_input:
    if ball==4 or ball==6:
        boundaries+=1
    elif ball==0:
        dot_balls+=1

    total_score+=ball

print('Score: ',total_score)
print('Boundaries: ',boundaries)
print('Dot balls: ',dot_balls)'''


#calculate delivery partner earnings
'''earnings = 0
deliveries = int(input('Enter no of deliveries: '))
earnings += deliveries*50
if deliveries>20:
    earnings+= 200
print('Total Earnigs: ',earnings)'''

#calculate toll
#if they enters stop calculate the toll

'''toll = 0
while True:
    vehicle = input('Enter vehicle: ').lower()
    if vehicle=='bike':
        toll += 20
    elif vehicle == 'car':
        toll+=50
    elif vehicle == 'bus':
        toll+=100
    elif vehicle == 'stop':
        break
print('Total Toll: ',toll)'''

#electricity bill calculation
'''units = int(input('Enter number of units consumed: '))
bill = 0
if units<100:
    bill += units*2
elif units>100 and units<=200:
    bill += 100 * 2
    bill += (units-100) * 3
else:
    bill += 100 * 2
    bill += 100 * 3
    bill += (units-200) * 5

print('Electricity Bill is: ',bill)'''

'''hundreads_greater_count=0
while True:
    number = int(input('Enter number: '))
    if number>100:
        hundreads_greater_count+=1
    else:
        hundreads_greater_count=0
    if hundreads_greater_count==3:
        print('Intruder Detected')
        break'''

#calculate bike travelled trips with 20litrs of petrol

'''fuel_consumed=0
trips = 0
while True:
    n = int(input('enter ltrs that consumed in trip: '))
    fuel_consumed+=n
    if fuel_consumed>20:
        print('Trips completed: ',trips)
        print('Fuel Empty')
        break
    trips += 1'''

#print the session at which battery became critical

'''total = 100
sessions = 0
while True:
    number = int(input('Enter percentage: '))
    total -= number
    sessions+=1
    if total<10:
        print('Critical at Session ', sessions)
        break'''

#smallest among numbers
'''smallest = float('+inf')
for i in range(int(input('Enter n range: '))):
    number = int(input('Enter a number: '))
    if number<smallest:
        smallest = number

print('smallest smong is: ',smallest)'''

#smallest among digits in a number
'''n = int(input('ENter a number: '))
smallest = float('+inf')
largest = float('-inf')
while n>0:
    d = n%10
    if d<smallest:
        smallest=d
    if d>largest:
        largest=d
    n = n//10

print(smallest,largest)'''

    

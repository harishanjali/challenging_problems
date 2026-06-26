#count frequency of each tuple
'''data = [(1,2),(3,4),(1,2),(5,6),(3,4),(3,4)]
res = {}
for tup in data:
    if tup in res:
        res[tup] += 1
    else:
        res[tup] = 1

print(res)'''

#find missing characters
'''a = set('abcdefghijklmnopqrstuvwxyz')
b = set('chatgpt')

print(set(sorted(list(a-b))))'''

#employee attendace analyzer
'''data = [("Nani","Mon"), ("Rahul", "Mon"),

("Nani", "Tue"), ("Sneha", "Tue"),

("Rahul", "Wed"), ("Nani", "Wed"),

("Sneha", "Wed"), ("Rahul", "Thu"), ("Rahul", "Fri") ]

res = {'employee_attendace':{},'day_wise':{},'max_attender':{'name':'','present':0},'absent_friday':[]}
for emp,day in data:
    if day in res['day_wise']:
        res['day_wise'][day].append(emp)
    else:
        res['day_wise'][day] = [emp]

    if emp in res['employee_attendace']:
        res['employee_attendace'][emp]+=1
    else:
        res['employee_attendace'][emp]=1

    if res['employee_attendace'][emp]>res['max_attender']['present']:
        res['max_attender']['name'] = emp
        res['max_attender']['present'] = res['employee_attendace'][emp]
print(res)'''

#library book borrowing system
'''data = {"Alice":["Python","SQL","Python"],
	      "Bob":["Java","Python"],
   	      "Charlie":["SQL","C++","Java"],
	      "Diana":["Python","C++"]    
        }
res = {'unique_books':set(),'books_borrowed_count':{},'max_book_borrowers':[]}
m=0
for std,books in data.items():
    res["unique_books"].update({book for book in set(books)})
    for book in books:
        if book in res['books_borrowed_count']:
            res['books_borrowed_count'][book]+=1
        else:
            res['books_borrowed_count'][book] = 1
    if len(books)>=m:
        res['max_book_borrowers'].append({std:books})
        m=len(books)'''

#.University Course Enrollment
'''courses = {"Python":{"Nani","Rahul","Anjali"},
	   "Java":{"Rahul","Sneha"},
	   "SQL":{"Nani","Sneha","Rahul"},
	   "React":{"Anjali","Nani",'Rahul'}   
       }

res = {'students_course_count':{},'students_courses':{},'max_enrollment_course':[],'atleast_2_courses':set(),'all_courses_taken':[]}
m=0
for course,students in courses.items():
    for student in students:
        if student not in res["students_course_count"]:
            res['students_course_count'][student] = 1
        else:
            res['students_course_count'][student] +=1

        if student not in res["students_courses"]:
            res["students_courses"][student] = [course]
        else:
            res["students_courses"][student].append(course)
        
        if res['students_course_count'][student]>=2:
            res["atleast_2_courses"].add(student)
        if res['students_course_count'][student]==4:
            res['all_courses_taken'].append(student)
    if len(students)>=m:
        res['max_enrollment_course'].append(course)
        m=len(students)

        
print(res)'''

#movie ticket booking analysis
'''bookings=[ ("Nani","Avatar","A1"),("Rahul","Leo","B2"),
	    ("Nani","Avatar","A2"),("Sneha","Leo","B5"),
	    ("Rahul","Jawan","C1"),("Nani","Leo","D4")  
        ]

res = {'movie_cutomer_count':{},'seat_count_movie':{},'more_than_2':set(),'most_watched_movie':[]}
m=0
for name,movie,seat in bookings:
    if name in res['movie_cutomer_count']:
        res['movie_cutomer_count'][name]+=1
    else:
        res['movie_cutomer_count'][name]=1
    if movie in res['seat_count_movie']:
        res['seat_count_movie'][movie]+=1
    else:
        res['seat_count_movie'][movie]=1
    if res['seat_count_movie'][movie]>=m:
        res['most_watched_movie'] = movie
        m = res['seat_count_movie'][movie]
    if res['movie_cutomer_count'][name]>1:
        res['more_than_2'].add(name)
print(res)'''

#swap first and last element of tuples
'''x = [(1,2,3),(4,5,6),(7,8,9)]
res = []
for tup in x:
    tup = list(tup)
    tup[0],tup[2]=tup[2],tup[0]
    res.append(tuple(tup))
print(res)'''

#department wise count
'''employee = { "Nani":"IT","Rahul":"HR",
		     "Sneha":"IT","Anjali":"Finance" }

res = {}
for k,v in employee.items():
    if v in res:
        res[v]+=1
    else:
        res[v]=1
print(res)'''

#group digits by number of digits

'''x = [5,12,345,6789,90]
res = {}
for num in x:
    res[len(str(num))] = num
print(res)'''

#replace every element with the greatest element on its right
'''x = [16,17,4,3,5,2]

for i in range(len(x)-2):
    max_next = max(x[i+1:])
    x[i] = max_next
else:
    x.append(-1)
print(x)'''

'''nums = [9,12,3,5,14,10,10]
pivot = 10
res = [10,10]
for num in nums:
    if num<pivot:
        res = [num]+res
    elif num>pivot:
        res = res+[num]

print(res)'''


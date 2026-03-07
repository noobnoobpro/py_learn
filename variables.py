#a= int(input().strip())
a= "five"
# if a%2 !=0:
#     print('odd')
# if a%2 == 0:
#     print('even')

# list = ["apple", "banana", "mango"]
# x,y,z = list
# print(x,y,z)
# print(x+y+z)

# global_variable ="abd"

# def func1():
#     local_variable = "abdullah"
#     print("my name is", global_variable)

# func1()

# new1 = range(5)
# print(new1)


a= """i am alive"""
# print(a[0])
# for i in a:
#     print("elements of string a",i)
# print("length of a is", len(a))

# print("alive" in a )
#print(bool(print("not" not in a)))

# print("a[0]=",a[0] )
# print("a[-2]=",a[-2] )
# print("a[-6:]=",a[-6:] )
# print("a[-6:-4]=",a[-6:-4])
# print(a.split(" "))


# age =25
# # print(f"i am alive since {age:.2f} ") #25.00
# print(2001%4)


# b=5
# print(isinstance(b,int))

# c=1
# print(c^5)

# numbers = [1, 2, 3, 4, 5]

# if (count := len(numbers)) > 3:
#     print(f"List has {count} elements")

# x = [1, 2, 3]
# y = [1, 2, 3]

# print(x == y)
# print(x is y)

# x = ["apple", "banana"]
# y = ["apple", "banana"]
# z = x

# print(x is z)
# print(x is y)
# print(x == y)

# x=1;y=1;z=1;n=2;i=0
# list_store =[]
# new_list=[]
# for i in range(x+1):
#     for j in range(y+1):
#         for k in range (z+1):
#             if i+j+k !=n:
#                 #print(i,j,k)
#                 list_store.append(i)
#                 list_store.append(j)
#                 list_store.append(k)
#     new_list.extend(list_store)            
# print(list_store)
# print(new_list)

# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort()
# print(thislist)

# list1 =[2,3,6,6,5]
# list1.sort()
# new_list=[]
# for i in list1:
#     if i not in new_list:
#         new_list.append(i)

# print(new_list)

# data = [["adi", 50], ["abi", 40], ["anu", 10], ["ram", 60],["sonu",60]]
# lowest_mark = data[0][1]
# second_lowest = float('inf')

# for i in data: 
#     if i[1]<lowest_mark:
#         lowest_mark=i[1]
# for i in data:
#     temp=i[1]
#     if temp!=lowest_mark and temp < second_lowest:
#         second_lowest=temp
# student_names=[]
# for i in data:
#     if i[1]==second_lowest:
#         student_names.append(i[0])
# student_names.sort()
# for i in student_names:
#     print(i)


# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

# (green, *yellow, red) = fruits

# print(green)
# print(yellow)
# print(red)
#--------------------SET----------------------------
if 0: 
    sety= {"a",2,3}
    sety.remove(2)
    #sety.remove(2) #--> error 
    sety.discard(2)
    x= sety.pop()
    # for x in sety:
    #     print(x)
    print(x)
if 0:
    set1={1,2,3,4}
    set2={5,6,7,8}
    set3=set1.union(set2) #adds both irresepective of data type  or use --> set3 = set1 | set2 (only same set type)
    set1.update(set2) # updates set 1 with set 2 elements 
    print(set3) 

    # intersection to find common of both sets 
    set4={1,2,3,4}
    set5={4,5,6,7}
    set7= set4.intersection(set5) # returns 4 ( only common of both )
    #alias 
    set7= set4 & set5 #same as intersection()
    set4.intersection_update(set5) #--> common of both appended to set4 


    # similartly one can do difference 
    set8={1,2,3,4}
    set9={1,2,3,6}
    set10= set8.difference(set9) # stores 4,6 in set 10
    set8.difference_update(set9) # stores 4,6 in set 8

if 0:
    set10={1,2,3,4,5,6}
    set11={1,2,3,4,5}
    set12= set10.symmetric_difference(set11) #element not present in both the sets 
    #alias
    set10.symmetric_difference_update(set11)
    #print(set10 ^ set11)
    print(set12)


#------------FROZENSET---------------
if 0:

    froze_boy= frozenset({1,2,3,4,5,6,7}) # immutable 
    print(type(froze_boy))


#--------DICTIONARY----------------------

if 0:
    thisdict= {"abdullah": 50, "dubdullah": 60, "nayeem":70}
    #print(type(thisdict))
    print(thisdict["abdullah"])


#-------FUNCTIONS--------------
if 0:
    def function(name="default"):
        return name + " shariff"
    print (function("abdullah"))
    print(function()) # prints default
    print(function(name='ab'))

#-------FUNCTIONS WITH NO OF ARGUMENTS UNAWARE ---> *arg --------------
if 0:
    def my_function(*numbers):
        if len(numbers) == 0:
            return None
        max_num = numbers[0]
        for num in numbers:
            if num > max_num:
                max_num = num
            return max_num
    print(my_function(3, 7, 2, 9, 1))


#-------IF NO. OF KEYWORDS UNAWARE USE --> **arg -----
if 0:
    def my_function(**kid): # use when unaware of no of args
        print("his first name is " + kid["firstname"]) #--> because kid becomes a dictionary so we access like kid["argument"]
                   
    my_function(firstname='abd', secondname='shar')

if 0:
    def my_function(title, *args, **kwargs):
        print("Title:", title)
        print("Positional arguments:", args)
        print("Keyword arguments:", kwargs)
    my_function("User Info", "Emil", "Tobias", age = 25, city = "Oslo")

# in case of list
if 0:
    def summer(a,b,c):
        return a+b+c
    numbers=[1,2,3]
    print(summer(1,2,3))
    print(summer(*numbers)) # same as previous line


    #in case of dictionary
if 0:
    def fullnamer(firstname, secondname):
        print("his name is", firstname,secondname)

    dummydict={"firstname":"abd","secondname":"shar" }
    fullnamer(**dummydict)

#------DECORATOR-------------------------------
#using one function to decorate another function using symbol @
if 0:
    def caps(anything):
        def innercaps():
            return anything().upper()
        return innercaps
    @caps #--> decorates my func
    def func():
        return "Abdullah Sheik"
    print(func())


#---------LAMBDA---------------------------
#function that follows the syntax lambda <argument> : <expression>
# whats the beauty? it can take any number of arg 
if bool(0):

    x= lambda a,b :a*b
    print(x(5,6))
    #or
    y= lambda c: c +100
    print(y(100))

if 0:
    def myfunc(n):
        return lambda a : a * n
    mytripler = myfunc(3)
    mydoubler = myfunc(2)
    myquatrupler = myfunc(4)
    print(mytripler(11)) #11*3
    print(mydoubler(11)) #11*2


#----------RECURSION----------------------  
if 0:
    def factorial(n):
        if n==0 or n==1:
            return 1
        else:
            return n*factorial(n-1)

    print(factorial(1))

if 0:
    def fibonacci_th_number(n):
        if n==1:
            #print("inside if")
            return 0
        elif n==2:
            #print("inside elif")
            return 1
        else:
            #print("inside else")
            return fibonacci_th_number(n-1)+fibonacci_th_number(n-2)
    print(fibonacci_th_number(5))
# import sys
# print(sys.getrecursionlimit())

if 0: print(list(range(5)))
#----------MODULES--------------------------------------------------------------------------------- 
if 0:
    #import userdefined as xyz
    from userdefined import dic
    #print(xyz.sum(5,5))
    print(dic["name"])


#-------------REGULAR EXPRESSIONS----------------------------------------
if 1:
    import re
    txt= " i am alive in spain"
    x=re.search("\s",txt) # returns only first occurance
    print("does space exist in my string?= ",bool(x))
    x=re.findall("a",txt) #finds all instance 
    print("amount of times 'a' exist in my string =",len(x))
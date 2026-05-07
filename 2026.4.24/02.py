'''
def order():
    x= int(input ("the first number "))
    y= int(input ("the second number "))
    if x > y :
        print(x)
    else :
        print(y)

order()
'''
'''
for i in range (1,11):
    if i == 5:
        
        print("we are here")
    
    print (i)
    
'''
'''
i=1
while i < 11 :
    print(i) 
    i =i+1  

'''
'''
num1 = int(input("the first number "))
num2 = int(input("the second number ") )
num3 = int(input("the third number "))

if num1 > num2 :
    if num3 >num1 :
        print(num3)
    else :
        print(num1)
elif num3 > num2 :
    print(num3)
else :
    print(num2)


x = int(input())
def camp(x):
    if x < 0:
        return 0
    else:
        return x
print(camp(x))


'''

'''
word = 0
while word != "exit"  :
    word = input("give me a word ")

'''
'''
some_number = 0
for i in range(0,10) :
    print("Look at my number ", some_number)
    some_number += 1
    i += 1
'''
'''
some_number = 50 
i = 10
while i <60 :
    some_number -=i
    i +=5 
    print(some_number)

'''

output = str()
for i in range(10,110,10):
    if i % 30 == 0 :
        output =output +str(i) + "#" + ", " 
    elif i ==100:
        output =output +str(i) 
    else :
        output =output +str(i) + ", "
print(output) 







'''
for i in range (1 , 5) :
    for j in range (1, 5) :
        print ("* ", end = "")
    print()
'''
'''
for i in range (1,5) :
    for j in range (i) :
        print("* " ,end = "")
    print()

'''
'''
for i in range (1,5):
    for j in range (0,4-i):
        print("  ",end = "")
    for j in range (2*i-1) :
        print("* ",end = "")
    print()
'''
'''
def is_prime(n):
    if n == 0 or n ==1 :
        return False
    else:
        for i in range(2,int(n**0.5)+1):
            if n % i  == 0:
                return False            
        return True
n = int(input())
print(is_prime(n))        
'''
'''
tuple = (1,2,3)
print(len(tuple))
'''            
    
# list = [1,2,3]
# list.insert(+1,"9")   
# print(list)

# a,b = [1,2,4],[4,6,9]           
# def joint(a,b) :
#     for item1 in a :
#         for item2 in b:
#             if item1 == item2: 
#                 return True
#     return False
# print(joint(a,b))

# dic = {"a":2,"b": 4.5,"c": "6"}
# def add_one(dic):
#     modified_dic = {}
#     for key,value in dic.items():
#         if type(value) == int or type(value) == float:
#             modified_dic[key]= value + 1
#         else:
#             modified_dic[key] = value
#     return modified_dic
# print(add_one(dic))

# tuple1 = (1,2,3)
# for a in tuple1 :
#     print(a)

# b = 1
# a = b
# a = 2
# print(b)

num = [4,6,1,9]

sorted(num)
print(num)

'''Type Checking: To check the value of particular type()'''

# a = 10
# b = 5.6
# c = "Ram"
# d = [1,2,3,4]
# e =(1,2,3,4)
# f = {1,2,3,4}
# g = {"name" : "Nandu"}
# print(isinstance(a,int))
# print(isinstance(b,float))
# print(isinstance(c,str))
# print(isinstance(d,set))
# print(isinstance(e,set))
# print(isinstance(f,tuple))
# print(isinstance(g,dict))

'''Checking multiple values'''
# x = "ram"
# if isinstance(x, (int,float)):
#     print("Given x is int or float")
# else:
#     print("Given x is string")

'''Checking with classes'''

# class Animal:
#     pass
# class Dog(Animal):
#     pass
# class cat:
#     pass
# d = Dog()
# c = cat()
# print(isinstance(d,Dog))
# print(isinstance(d,Animal))
# print(isinstance(c,cat))
# print(isinstance(c,Dog))

'''Duck Typing:' same method acts as same behaviour , we can use it'''
# class Dog:
#     def sound(self):
#         print("Bow-Bow")
# class cat:
#     def sound(self):
#         print("Meow-Meow")
# def make_sound(animal):
#     animal.sound()
# d = Dog()
# c = cat()
# make_sound(d)
# make_sound(c)

'''example'''
# def process(data):
#     if isinstance(data,int):
#         return data*2
#     elif isinstance(data,str):
#         return data.upper()
#     elif isinstance(data,float):
#         return data*10.5
# print(process(10))
# print(process('vally'))
# print(process(10.56))


'''Interview QUestions'''
# class A:
#     pass
# class B:
#     pass
# obj=B()
# print(type(obj)==B)  #output:True
# print(type(obj)==A)  #output:
# print(isinstance(obj,B))  #output:True
# print(isinstance(obj,A))  #output:
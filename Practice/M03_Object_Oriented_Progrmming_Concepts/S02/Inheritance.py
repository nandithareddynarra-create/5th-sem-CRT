'''Single Inheritance'''
# class A:
#     def display1(self):
#         print("This is Class A display method")
# class B(A):
#     def display2(self):
#         print("This is class B display method")
# b = B()
# b.display1()
# b.display2()

'''MultiLevel Inheritance'''
# class A:
#     def display1(self):
#         print("This is Class A display method")
# class B(A):
#     def display2(self):
#         print("This is class B display method")
# class C(B):
#     def display3(self):
#         print("This is class C display method")
# c = C()
# c.display1()
# c.display2()
# c.display3()

'''Multiple Inheritance'''
class A:
    def display(self):
        print("This is Class A display method")
class B(A):
    def display(self):
        print("This is class B display method")
class C(A,B):
    def display(self):
        print("This is class C display method")
c = C()
c.display()
'''Single Inheritance'''
# class A:
#     def display(self):
#         print("This is class A")
# class B(A):
#     def display1(self):
#         print("This is class B")
# b = B()
# b.display()
# b.display1()

'''Multilevel Inheritance'''
# class A:
#     def display(self):
#         print("This is class A")
# class B(A):
#     def display1(self):
#         print("This is class B")
# class C(B):
#     def display2(self):
#         print("This is class C")
# c = C()
# c.display()
# c.display1()
# c.display2()

'''Multiple Inheritance'''
# class A:
#     def display(self):
#         print("This is A")
# class B:
#     def display1(self):
#         print("This is class B display method")
# class C(A, B):
#     def display2(self):
#         print("This is class C display method")
# c = C()
# c.display()
# c.display1()
# c.display2()

'''Hybrid'''
# class A:
#     def method_a(self):
#         print("This is class A")

# class B(A):
#     def method_b(self):
#         print("This is class B")

# class C(A):
#     def method_c(self):
#         print("This is class C")

# class D(B, C):
#     def method_d(self):
#         print("This is class D")

# d = D()
# d.method_a()
# d.method_b()
# d.method_c()
# d.method_d()

'''Hierarchical Inheritance'''

# class Parent:
#     def display(self):
#         print("This is Parent class")

# class Child1(Parent):
#     def display1(self):
#         print("This is Child1")

# class Child2(Parent):
#     def display2(self):
#         print("This is Child2")

# c1 = Child1()
# c2 = Child2()

# c1.display()
# c1.display1()

# c2.display()
# c2.display2()
# class A:
#     def sum(self):
#         a = 5
#         b = 6
#         print(a+b)
# a = A()        
# class B:
#     def sub(self):
#         x = 6
#         y = 7    
#         print(x-y)
# b = B()
# a.sum()
# b.sub()
# Python Program to depict multiple inheritance
# when method is overridden in both classes

class A:
	def m(self):
		print("1")
	
class B(A):
	def m(self):
		print("2")

class C(A):
	def m(self):
		print("3")
		
class D(B,C):
	pass
	
obj = D()
obj = A()
obj = B()
obj = C()
obj.m()

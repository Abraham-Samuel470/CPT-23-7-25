# class number():
#     even=[]
#     odd=[]
#     def __init__(self,num):
#         self.num=num
#         if num%2==0:
#             number.even.append(num)
#         else:
#             number.odd.append(num)
# n1=number(21)
# n2=number(32)
# n3=number(43)
# n4=number(54)
# n5=number(65)
# print("Even Mutable list " , number.even)
# print("Odd mutable list " , number.odd)

# Global class

# def op(x):
#     return x**3

# class abc():
#     def __init__(self,val):
#         self.val=val

#     def display(self):
#         print("Given value : ", self.val)
#     def modify(self):
#         self.val=op(self.val)
#         print("Modified value --> ", self.val)


# o=abc(3)
# o.display()
# o.modify()
# o.display()

# 
print("****************** Program starts *******************")
print(" ")
class abc():
    def __init__(s,var1,var2):
        s.var1=var1
        s.var2=var2
    def display(s):
        print("var1 " , s.var1)
        print("var2 " , s.var2)



n1=27
n2=36
o=abc(n1,n2)
print("Object.__dict__--> ", o.__dict__)
print("Object.__doc__--> ", o.__doc__)
print("class.__name__ --> " , abc.__name__)
print("Object.__module__ --> " , o.__module__)
print("classBase.__base__ --> " , abc.__bases__)
print(" ")
print("****************** Program ends *********************")

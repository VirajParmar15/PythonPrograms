'''in languages there are some concepts
variabel
data types,strings
built in data types
conditional statements
loops
continue,break
function
-call by value
-call by refrence
-call by address
-overloading
pointer
-in stack
-in heap
array
class
object
constructor
-overloading
inheritance
encapsulation
abstraction
polymoephism
etc
'''

'''
class=code template for creating program objects

name=what is it?
star cookie
attribute=what describe it?
weight,color
behavior=what can it?
decorate(),consumes()

method=a block of code or program procedure that can be called to perform some actions 
and it may return a value
defined as a part of class
'''

class StarCookie:
    def __init__(self,color,weight):
        print("the cookie is ready..")
        self.color=color
        self.weight=weight


star_cookie1 = StarCookie("red",16)
print(star_cookie1.weight)
print(star_cookie1.color)


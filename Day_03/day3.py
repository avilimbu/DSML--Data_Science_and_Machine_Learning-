a= 5 #initializing integer number
b= 6.4 #initializing float number
c= 3+7j  #initializing complex number

print(type(a)) #int
 
print(a==b) #false || boolean value 

d= 17
print(d//a) #3 ||floor divisor:
print(a+d) #20

b =int(b)
print(type(b)) #int

#Using Math Function
import math

floor= math.floor(44.9)
ceil = math.ceil(44.9)
print(f"floor={floor} and ceil= {ceil}")

#finding gcd
math.gcd(4,6,12,8)

#finding round number
round= round(3456.56575,2) #3456.57
print(round)

#finding the minimum & maximum among numbers

minm = min(a,b,d)
maxm= max(a,d,b)
print(f"manimum= {minm} and maximum= {maxm}")

name = 'Avhi' #single quote string
university = "Tribhuvan University"
print(f"{name} studies in {university}")


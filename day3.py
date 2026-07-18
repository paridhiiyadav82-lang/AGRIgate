#despite the number you put, according to the data type you wrap your input around python will treat that number as that data type only. 

number=input("hi pls give us your number ")
print("lets find out the type of our number!")
print("its a ", type(number))

number=int(input("hi pls give us your number "))
print("lets find out the type of our number!")
print("its a ", type(number))

number=float(int(input("hi pls give us your number ")))
print("lets find out the type of our number!")
print("its a ", type(number))

print(56092*39832740943)
print(3/2)
#floor divison = no decimal 
print(3//2)
#exponent
print(3**2)
#remainder
print(3%2)
#bodmas 
print(3*(2+1))
x=3
y=x+3
print(y)
num=5
num*=5
print(num)
print(abs(-5))
print(round(3.76,1))
num1=3
num2=4
print(num1==num2)
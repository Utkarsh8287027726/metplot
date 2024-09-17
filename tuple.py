#tuple store multiple data and data can't be change
#mytuple =  ("Ivan", "Anshu", "Vani", "Ashish", "Vani")
#print(mytuple)
#print(type(mytuple))

#print(mytuple[1])

#mytuple[1] = "utkarsh"
#print(mytuple)
#for value in mytuple:
    #print(value)
    
#dict it can store multiple data in key value pair 
mydict={
    "name":"utkarsh jaiswal",
    "email":"utkarshj345@gmail.com"
}    
print(type(mydict))
print(mydict)

for item in mydict:
    print(mydict[item])
    
    print(mydict.get("email"))
    
mydict["name"] = "Adrash"
print(mydict)    


    #opps
    #class and object
    # class is a collect of blueprint
#class Mohit:
    #age = 20
    #print("I am from Delhi")
    
#mohit = Mohit()    
#print(mohit.age)
#class Person:
 #   def__init__(self, Name, Age)
#self.Name =name
#self.Age =age
        
#def printname(self):
  #print(self.name,self.age)   
  #x = person("Utkarsh","Ashish")
  #x.printname() 
  
  
  
  #age AMD year batani hai class and object 
  
  
  
#project random otpgenertae

import random
def generate_otp(length=6):
    digit = "0123456789"
    otp  = ''.join(random.choice(digit) for _ in range(length))
    return otp
otp = generate_otp()
print("Your OTP is" , otp)
import re
password=input("enter your password:")

try:
   re.match("^.*(?=.{6,16})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[$#@]).*$" ,password)
   
   if  not re.match("(?=.{6,16}$)",password):
          raise ValueError("That is not enough length!")
   if  not re.match("(?=.*[a-z])",password):
          raise ValueError("please enter lowercase!")
   if  not re.match("(?=.*[A-Z])",password):
          raise ValueError("please enter uppercase!")
   if  not re.match("(?=.*[$#@])",password):
          raise ValueError("please enter $#@)!")
except ValueError as ve:
   print(ve)
else:
       print("the password is valid")

 
import random
# we use sample() function which is inbuilt in random , which takes 2 inputs ie  , sequence and length , where sequence contains a list or tuple or sttring or set and length is taken as per user input and using both these we are generating a length of string and join is used to concatenate it to empty string .
passlen = int(input("enter the length of password"))
s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
p = "".join(random.sample(s,passlen ))
print(p)

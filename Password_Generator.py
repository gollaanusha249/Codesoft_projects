import string 
import random 

lowercase_letters = string.ascii_lowercase
uppercase_letters = string.ascii_uppercase 
digits = string.digits 
punctuation_marks = string.punctuation
password_len = int(input("enter length of the password "))
l = []
l_l = input("do u want lowercaseletters(yes/no):")
if l_l == "yes":
    l.extend(lowercase_letters)
u_l = input("do u want uppercaseletters(yes/no):")
if u_l == "yes":
    l.extend(uppercase_letters)
d = input("do u want digits(yes/no):")
if d == "yes":
    l.extend(digits)
p = input("do u want punctuationmarks(yes/no):")
if p == "yes":
    l.extend(punctuation_marks)
l=list(l)

random.shuffle(l)

print("Generated Password is:","".join(l[0:password_len]))
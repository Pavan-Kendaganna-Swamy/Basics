#Check if the string has any a, r, or n characters:
import re

s1 = "The rain in Spain"
p1 = "[arn]"

m1 = re.findall(p1,s1)
if m1:
    print(m1, "q1 : yes")
else:
    print("q1 : no")

# Check if the string has any characters between a and n:
s2 = "The rain in Spain"
p2 = "[a-n]"

m2 = re.findall(p2,s2)
if m2:
    print(m2, "q2 : yes")
else:
    print("q2 : no")

#Check if the string has other characters than a, r, or n:
s3 = "The rain in Spain"
p3 = "[^arn]"

m3 = re.findall(p3,s3)
if m3:
    print(m3, "q3 : yes")
else:
    print("q3 : no")

#Check if the string has any 0, 1, 2, or 3 digits:

s4 = "The rain in Spain"
p4 = "[0-3]"

m4 = re.findall(p4,s4)
if m4:
    print(m4, "q4 : yes")
else:
    print("q4 : no")

#Check if the string has any digits:
s5 = "8 times before 11:45 AM"
p5 = "\d"

m5 = re.findall(p5,s5)
if m5:
    print(m5, "q5 : yes")
else:
    print("q5 : no")

# Check if the string has any two-digit numbers, from 00 to 59:
s6 = "8 times before 11:45 AM"
p6 = "[0-5][0-9]"

m6 = re.findall(p6,s6)
if m6:
    print(m6, "q6 : yes")
else:
    print("q6 : no")

#Check if the string has any characters from a to z lower case, and A to Z upper case:
s7 = "8 times before 11:45 AM"
p7 = "[a-zA-Z]"

m7 = re.findall(p7,s7)
if m7:
    print(m7, "q7 : yes")
else:
    print("q7 : no")

# Check if the string has any + characters:
s8 = "8 times before 11:45 AM"
p8 = "[+]"

m8 = re.findall(p8,s8)
if m8:
    print(m8, "q8 : yes")
else:
    print("q8 : no")
    
    
#q9 : greedy match : [.*]
greedy_pattern = r"\[.*\]" 
greedy_string = "[Extract data [between brackets] using regex]" 
greedy_match = re.findall(greedy_pattern,greedy_string) 
print("q9: ", greedy_match) 
 
#q10 : non greedy : [*?]
 
non_greedy_pattern = r"\[.*?\]" 
non_greedy_string = "[Extract data [between brackets] using regex]" 
non_greedy_match = re.findall(non_greedy_pattern,non_greedy_string) 
print("q10: " ,non_greedy_match)
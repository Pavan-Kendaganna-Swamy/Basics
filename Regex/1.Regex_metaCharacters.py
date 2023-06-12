# q1. any five letter string starting with a and ending with s
import re

string_q1 = "abss"
string_q12 = "abyss"
pattern_q1 = "^a...s$"

q1_match = re.match(pattern_q1, string_q1)
if q1_match:
    print("no")
else:
    print("its abss")
q12_match = re.match(pattern_q1, string_q12)
if q12_match:
    print("yes")

#q2. Search the string to see if it starts with "The" and ends with "Spain":

string_q2 = "The string is starting with the and ends with Spain"
patter_q2 = "^The.*Spain$"

q2_match = re.match(patter_q2,string_q2)
if q2_match:
    print("q2 match")


#Find all lower case characters alphabetically between "a" and "m":

s3 = "the rain in spain"
p3 = "[a-m]"

m3 = re.findall(p3,s3)
print(m3)


#Find all digit characters:

s4 = "That will be 59 dollars"
p4 = "[\d]+"

m4 = re.findall(p4, s4)
print(m4)

#Search for a sequence that starts with "he", followed by two (any) characters, and an "o":
s5 = "hello planet hello"
p5 = "he..o"

m5 = re.search(p5, s5) #prints one
print(m5.group())

m51 = re.findall(p5,s5) #output is a list and prints everything
print(m51)

#Check if the string starts with 'hello':
s6 = "hello planet"
p6 = "^hello"

m6 = re.match(p6, s6)
if m6:
    print("q6 : yes")

#Check if the string ends with 'planet':

s7 = "hello planet"
p7 = "planet$"

m7 = re.findall(p7, s7)
if m7:
    print("q7 : yes")

#Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":
s8 = "hello planet"
p8 = "^he.*o"

m8 = re.findall(p8, s8)
if m8:
    print(m8, "q8 : yes")
#Search for a sequence that starts with "he", followed by 1 or more  (any) characters, and an "o":
s9 = "hello planet"
p9 = "^he.+o"

m9 = re.findall(p9, s9)
if m9:
    print(m9, "q9 : yes")
#Search for a sequence that starts with "he", followed by 0 or 1  (any) character, and an "o":
s10 = "hello planet"
p10 = "^he.?o"

m10 = re.findall(p10, s10)
if m10:
    print(m10, "q10 : yes")
else:
    print(m10, "q10 : no ")

#Search for a sequence that starts with "he", followed excactly 2 (any) characters, and an "o":
s11 = "hello planet"
p11 = "^he.{2}o"

m11 = re.findall(p11, s11)
if m11:
    print(m11, "q11 : yes")

#Check if the string contains either "falls" or "stays":
s12 =  "The rain in Spain falls mainly in the plain and stays!"
p12 = "(falls|stays)"

m12 = re.search(p12, s12)
if m12:
    print(m12.group(), "q12: yes")
    print(re.findall(p12,s12) , "q12 : yes again")
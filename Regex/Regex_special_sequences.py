#Check if the string starts with "The":
import re

s1 = "The rain in Spain"
p1 = "\AThe"

m1 = re.match(p1,s1)
if m1:
    print("q1 : yes")

#Check if "ain" is present at the beginning of a WORD:

s2 = "The rain in Spain"
p2 = r"\bain"

m2 = re.findall(p2,s2)
if m2:
    print(m2, "q2 : yes")
else:
    print("q2 : no")

#Check if "ain" is present at the end of a WORD:
s3 = "The rain in Spain"
p3 = r"ain\b"

m3 = re.findall(p3,s3)
if m3:
    print(m3, "q3 : yes")

#Check if "ain" is present, but NOT at the beginning of a word:
s4 = "The rain in Spain"
p4 = r"\Bain"

m4 = re.findall(p4,s4)
if m4:
    print(m4, "q4 : yes")



#Check if "ain" is present, but NOT at the end of a word:

s5 = "The rain in Spain"
p5 = r"ain\B"

m5 = re.findall(p5,s5)
if m5:
    print(m5, "q5 : yes")
else:
    print("q5 : no")

#Check if the string contains any digits (numbers from 0-9):

s6 = "The rain in Spain"
p6 = "\d"

m6 = re.findall(p6,s6)
if m6:
    print(m6, "q6 : yes")
else:
    print("q6 : no")

#Return a match at every no-digit character:

s7 = "The rain in Spain"
p7 = "\D"

m7 = re.findall(p7,s7)
if m7:
    print(m7, "q7 : yes")
else:
    print("q7 : no")

#Return a match at every white-space character:
s8 = "The rain in Spain"
p8 = "\s"

m8 = re.findall(p8,s8)
if m8:
    print(m8, "q8 : yes")
else:
    print("q8 : no")

#Return a match at every NON white-space character:

s9 = "The rain in Spain"
p9 = r"\S"

m9 = re.findall(p9,s9)
if m9:
    print(m9, "q9 : yes")
else:
    print("q5 : no")

#Return a match at every word character (characters from a to Z, digits from 0-9, and the underscore _ character):
s10 = "The rain in Spain"
p10 = r"\w"

m10 = re.findall(p10,s10)
if m10:
    print(m10, "q10 : yes")
else:
    print("q10 : no")

#Return a match at every NON word character (characters NOT between a and Z. Like "!", "?" white-space etc.)
s11 = "The @ rain in Spain"
p11 = r"\W"

m11 = re.findall(p11,s11)
if m11:
    print(m11, "q11 : yes")
else:
    print("q11 : no")

#Check if the string ends with "Spain":
s12 = "The rain in Spain"
p12 = r"Spain\Z"

m12 = re.findall(p12,s12)
if m12:
    print(m12, "q12 : yes")
else:
    print("q12 : no")
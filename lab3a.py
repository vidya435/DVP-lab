s=input("Enter a sentence:")
w=0
d=0
l=0
u=0
r=s.split()
w=len(r)
for i in s:
    if i.isdigit():
        d=d+1
    elif i.isupper():
        u=u+1
    elif i.islower():
        l=l+1
print("Number of words:",w)
print("Number of digit:",d)
print("Number of uppercase:",u)
print("Number of lowercase:",l)

num=input("Enter the number:")
num_list=list(num)
rev_num=num_list[::-1]
if num_list==rev_num:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")
counter = dict()
for i in num_list:
    if counter.get(i)==None:
         counter[i]=1
else:
    counter[i]=counter[i]+1
print(counter)    
                

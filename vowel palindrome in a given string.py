s=input()
a=[]
for i in range(len(s)):
    if(s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u'):
        a.append(s[i])
i=0
while i<len(a)//2:
    if(a[i]!=a[(len(a)-1)-i]):
        break
    i=i+1
if len(a)==0:
    print("no vowel is present")
elif(i==len(a)//2):
    print("vowel is palindrome")
else:
    print("vowel is not a palindrome")

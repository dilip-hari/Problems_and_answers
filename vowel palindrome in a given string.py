'''
Vowel is palindrome or not in given string.

input1:
good

output1:
vowel is palindrome

explanation:
vowels in the string is 'oo'
it is palindrome and it will print 'vowel is palindrome'

input2:
goode

output2:
vowel is not a palindrome

'''
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

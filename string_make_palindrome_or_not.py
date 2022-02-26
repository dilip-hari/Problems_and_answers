'''
Given string will make palindrome or not:

input format:
s will be the input string

output format:
make palindrome or  not

input1:
aaabbb

output1:
cannot make palindrome

input2:
mom

output2:
make palindrome

input3:
aabaa

output3:
make palindrome

The input have to perform so, many combination and have to check whether the string will print the
make palindrome or cannot make palindrome.

'''
def palindrome_make():
    s=input()
    s2=[]
    flag=0
    i=0
    #remove duplicate
    while i<len(s):
        j=0
        while j<i:
            if s[i]==s[j]:
                break
            j=j+1
        if i==j:
            s2.append(s[i])
        i=i+1
    i=0
    #compare the duplicate removed array with input string.
    while i<len(s2):
        j=0
        count=0
        while j<len(s):
            if s2[i]==s[j]:
                count=count+1
            j=j+1
        if count%2==1:
            flag=flag+1
        if flag==2:
            break
        i=i+1
    if i==len(s2):
        print("make palindrome")
    else:
        print("cannot make palindrome")
palindrome_make()

'''
Middle Print Till Repeat

A string S (without any spaces) whose length is odd is passed as the input. The program must start
printing from the middle character, then its immediate left and right characters. Then it must
print the next immediate left and right characters and so on till one of the characters is repeated.


Boundary Condition(s):
1 <= Length of S <= 101

Input Format:
The first line contains S.

Output Format:
The first line contains a string value.

Example Input/Output1:

Input:
character

Output: 
arca

Explanation:

The middle character is a. Then r, c are printed. Then a, t are to be printed. But when a is printed
it has been repeated already. So we stop.

Example Input/Output 2:
Input:
mango


Output:
nagmo

'''
s=input()
n=len(s)
a=[]
a.append(s[n//2])
m=(n//2)-1
p=(len(s)//2)+1
while m>=0:
    i=0
    while i<len(a):
        if(a[i]==s[m] or a[i]==s[p]):
            break
        i=i+1
    if(i==len(a)):
        a.append(s[m])
        a.append(s[p])
    else:
        if(a[i]==s[m]):
            a.append(s[m])
        else:
            a.append(s[m])
            a.append(s[p])
        break
    m=m-1
    p=p+1
b=''.join(a)
print(b)
    
